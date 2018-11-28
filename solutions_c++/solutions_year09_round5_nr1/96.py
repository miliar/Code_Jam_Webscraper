#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 

using namespace std;

int neigh[4][2]={{0,1},{1,0},{0,-1},{-1,0}};
set<vector<pair<int,int> > > st;
vector<pair<int,int> > zhan[1000000];
short isdang[1000000];
int d[1000000];
char a[20][20];

int isd(vector<pair<int,int> > a)
{
    int aa[6][6];
    int used[6];
    int zhan[6];
    int top,bottom;
    int i,j,k;
    memset(aa,0,sizeof(aa));
    memset(used,0,sizeof(used));
    for (i=0;i<a.size();i++)
        for (j=i+1;j<a.size();j++)
            if ((abs(a[i].first-a[j].first)+abs(a[i].second-a[j].second))<=1)
            {
                aa[i][j]=1;
                aa[j][i]=1;
            }
    top=0;bottom=1;
    zhan[0]=0;
    used[0]=1;
    while (top<bottom)
    {
        for (i=0;i<a.size();i++)
            if ((used[i]==0)&&(aa[zhan[top]][i]==1))
            {
                used[i]=1;
                zhan[bottom]=i;
                bottom++;
            }
        top++;
    }
    if (top==a.size()) return 0;
    else return 1;
}

int main()
{
    int i,j,k,m,n,l,t,x1,y1,x2,y2,top,bottom,ans,b1;
    vector<pair<int,int> > s,tt,aa;
    //freopen("pa.in","r",stdin);
    freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);    
    scanf("%d",&t);
    for (l=0;l<t;l++)
    {
        scanf("%d%d",&m,&n);
        for (i=0;i<m;i++)
            scanf("%s",a[i]);
        st.clear();
        s.clear();
        tt.clear();
        for (i=0;i<m;i++)
            for (j=0;j<n;j++)
            {
                if (a[i][j]=='o')
                    s.push_back(make_pair(i,j));
                if (a[i][j]=='x')
                    tt.push_back(make_pair(i,j));
                if (a[i][j]=='w')
                {
                    s.push_back(make_pair(i,j));
                    tt.push_back(make_pair(i,j));
                }
                if (a[i][j]!='#') a[i][j]='.';
            }
        sort(s.begin(),s.end());
        sort(tt.begin(),tt.end());
        ans=-1;
        st.insert(s);
        zhan[0]=s;
        isdang[0]=0;
        d[0]=0;
        if (s==tt) ans=0;
        top=0;bottom=1;
        while (top<bottom)
        {
            if (ans!=-1) break;
            for (k=0;k<zhan[top].size();k++)
                a[zhan[top][k].first][zhan[top][k].second]='#';
            for (k=0;k<zhan[top].size();k++)
            {
                a[zhan[top][k].first][zhan[top][k].second]='.';
                for (i=0;i<4;i++)
                {
                    aa=zhan[top];
                    x1=aa[k].first+neigh[i][0];
                    y1=aa[k].second+neigh[i][1];
                    x2=aa[k].first-neigh[i][0];
                    y2=aa[k].second-neigh[i][1];
                    if ((x1>=0)&&(x1<m)&&(y1>=0)&&(y1<n)&&(a[x1][y1]=='.')&&(x2>=0)&&(x2<m)&&(y2>=0)&&(y2<n)&&(a[x2][y2]=='.'))
                    {
                        aa[k].first=x1;
                        aa[k].second=y1;
                        sort(aa.begin(),aa.end());
                        b1=isd(aa);
                        if ((st.find(aa)==st.end())&&((b1==0)||(isdang[top]==0)))
                        {
                            if (aa==tt) ans=d[top]+1;
                            st.insert(aa);
                            zhan[bottom]=aa;
                            isdang[bottom]=b1;
                            d[bottom]=d[top]+1;
                            bottom++;
                        }
                    }
                }
                a[zhan[top][k].first][zhan[top][k].second]='#';
            }
            for (k=0;k<zhan[top].size();k++)
                a[zhan[top][k].first][zhan[top][k].second]='.';
            top++;
        }
        printf("Case #%d: %d\n",l+1,ans);
    }
	return 0;
}

