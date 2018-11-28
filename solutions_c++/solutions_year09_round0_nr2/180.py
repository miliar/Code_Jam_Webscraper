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

int neigh[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
map<pair<int,int>,int> mp;
int a[200][200];
int d[200][200];

int main()
{
    int i,j,k,x,y,xx,yy,best,bk,m,n,tt,l,t;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&t);
    for (l=0;l<t;l++)
    {
        scanf("%d%d",&m,&n);
        for (i=0;i<m;i++)
            for (j=0;j<n;j++)
                scanf("%d",&a[i][j]);
        mp.clear();
        tt=0;
        for (i=0;i<m;i++)
            for (j=0;j<n;j++)
            {
                x=i;y=j;
                while (1)
                {
                    best=2000000000;
                    bk=-1;
                    for (k=0;k<4;k++)
                    {
                        xx=x+neigh[k][0];
                        yy=y+neigh[k][1];
                        if ((xx>=0)&&(xx<m)&&(yy>=0)&&(yy<n)&&(a[xx][yy]<a[x][y]))
                        {
                            if (a[xx][yy]<best)
                            {
                                best=a[xx][yy];
                                bk=k;
                            }
                        }
                    }
                    if (bk==-1) break;
                    x=x+neigh[bk][0];
                    y=y+neigh[bk][1];
                }
                if (mp.find(make_pair(x,y))==mp.end())
                {
                    mp[make_pair(x,y)]=tt;
                    d[i][j]=tt;
                    tt++;
                }
                else
                {
                    d[i][j]=mp[make_pair(x,y)];
                }
            }
        printf("Case #%d:\n",l+1);
        for (i=0;i<m;i++)
        {
            for (j=0;j<n;j++)
            {
                if (j!=0) printf(" ");
                printf("%c",'a'+d[i][j]);
            }
            printf("\n");
        }
    }

	return 0;
}
