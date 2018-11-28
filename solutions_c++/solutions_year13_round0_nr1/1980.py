#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<ctype.h>
#include<string.h>
#include<iostream>
#include<vector>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<algorithm>
#include<sstream>
#include<time.h>

#define mp          make_pair
#define pb          push_back
#define popcount(a) __builtin_popcount(a)
#define contain(x,item) (x).find(item)!=(x).end()
#define FOR(i,a,b)  for(__typeof(a) i=(a);i<b;i++)
#define REV(i,a,b) for(__typeof(a) i=a;i>=0;i--)
#define PI          (2*acos(0))
#define clr(a)       a.clear()
#define SZ(a)       (int)a.size()
#define EQ(a,b)     (fabs(a-b)<ERR)
#define all(a)      (a).begin(),(a).end()
#define reall(a)    (a).rbegin(),(a).rend()
#define FOREACH(it,x)for(__typeof((x.begin())) it=x.begin();it!=x.end();it++)
#define fs          first
#define sc          second
#define mem(a,b)    memset(a,b,sizeof(a))

#define oo          1<<30
#define ERR         1e-7
#define lookalike   scanf("%*d")

using namespace std;

typedef long long ll;
template<class T1> void deb(T1 e){cout<<e<<endl;}
template<class T1,class T2> void deb(T1 e1,T2 e2){cout<<e1<<" "<<e2<<endl;}

////int rrr[]={1,0,-1,0};int ccc[]={0,1,0,-1};                      //4 Direction
////int rrr[]={1,1,0,-1,-1,-1,0,1};int ccc[]={0,1,1,1,0,-1,-1,-1};  //8 direction
////int rrr[]={2,1,-1,-2,-2,-1,1,2};int ccc[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
////int rrr[]={2,1,-1,-2,-1,1};int ccc[]={0,1,1,0,-1,-1};           //Hexagonal Direction

#define MAX 3200000000

int grid[5][5];

int main()
{
    freopen("tt.txt", "r", stdin);
    freopen("ttt.txt", "w", stdout);

    int t,cas=0;
    scanf("%d",&t);
    while(t--)
    {
        char c;bool fl=0;
        FOR(i,0,4)FOR(j,0,4)
        {
            scanf(" %c",&c);
            grid[i][j]=c;
            if(c=='X') grid[i][j]='A';
            else if(c=='O')grid[i][j]='B';
            if(c=='.') fl=1;
        }

        int id=-1;int a[2];
        for(int i=0;i<4;i++)
        {
            a[0]=0,a[1]=0;
            for(int j=0;j<4;j++)
            {
                if(grid[i][j]=='T') a[0]++,a[1]++;
                else if(grid[i][j]=='.') break;
                else a[grid[i][j]-'A']++;
            }
            if(a[0]==4) {id=1;break;}
            else if(a[1]==4) {id=0;break;}

            a[0]=0,a[1]=0;
            for(int j=0;j<4;j++)
            {
                if(grid[j][i]=='T') a[0]++,a[1]++;
                else if(grid[j][i]=='.') break;
                else a[grid[j][i]-'A']++;
            }
            if(a[0]==4) {id=1;break;}
            else if(a[1]==4) {id=0;break;}
        }
        if(id==-1)
        {
            a[0]=0,a[1]=0;
            int j=0;
            for(int i=0;i<4;i++,j++)
            {
                if(grid[i][j]=='T') a[0]++,a[1]++;
                else if(grid[i][j]=='.') break;
                else a[grid[i][j]-'A']++;

            }
            if(a[0]==4) {id=1;}
            else if(a[1]==4) {id=0;}

            if(id==-1)
            {
                a[0]=0,a[1]=0;
                int j=3;
                for(int i=0;i<4;i++,j--)
                {
                    if(grid[i][j]=='T') a[0]++,a[1]++;
                    else if(grid[i][j]=='.') break;
                    else a[grid[i][j]-'A']++;
                }
                if(a[0]==4) {id=1;}
                else if(a[1]==4) {id=0;}
            }
        }

        if(id==1) printf("Case #%d: X won\n",++cas);
        else if(id==0) printf("Case #%d: O won\n",++cas);
        else if(id==-1 and fl==0)printf("Case #%d: Draw\n",++cas);
        else printf("Case #%d: Game has not completed\n",++cas);
    }
    return 0;
}

