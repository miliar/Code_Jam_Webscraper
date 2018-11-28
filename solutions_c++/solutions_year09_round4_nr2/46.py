#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


#define SZ size()
#define PB push_back
#define ALL(v) v.begin(),v.end()
#define MP make_pair
#define x first
#define y second

#define LL long long
#define UI unsigned int
#define ULL unsigned long long
#define PI pair<int,int>
#define PD pair<double,double>
#define PLL pair<LL,LL>
#define PULL pair<ULL,ULL>
#define VI vector<int>
#define VD vector<double>
#define VS vector<string>
#define SI set<int>
#define PQ priority_queue
#define VVI vector<vector<int> >
#define IT iterator

#define ABS(x) (((x)>0)?(x):(-(x)))
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define sign(a) ((a)>0)-((a)<0)
#define sqr(a) ((a)*(a))
#define Repi(n) for (int i=0; i<n; i++)
#define Repj(n) for (int j=0; j<n; j++)
#define Repk(n) for (int k=0; k<n; k++)
#define F(i,n) for (int i=0;i<n;i++)

#define INF 20000000
#define EPS 1e-6

#define Time ((double)clock()/CLOCKS_PER_SEC)
#define pause system("pause")


using namespace std;

char a[11][8];
int T,R,C,F;

int dp[11][7][1<<6][1<<6];
int mv[2]={-1,1};

int solve(int x,int y,int cur,int next)
{
    int &ret=dp[x][y][cur][next];
    if (ret!=-1) return ret;
    if (x==R-1) return ret=0;
    
    char b[11][8]; memcpy(b,a,sizeof(a));
    Repj(C)
     if (cur&(1<<j)) b[x][j]='.';
    Repj(C)
     if (next&(1<<j)) b[x+1][j]='.';

    ret=INF;

  //  cout<<" at "<<x<<" "<<y<<" "<<cur<<" "<<next<<"\n";
  //  Repi(R)
  //   cout<<"                "<<b[i]<<"\n";

    int nx,ny,nnext,ncur;
    Repk(2)
     {
            ny=y+mv[k];
            if (ny<0 || ny>=C || b[x][ny]!='.') continue;
            nx=x;
            while (nx<R-1 && b[nx+1][ny]=='.') nx++;
            if (nx==x)
                     ncur=cur,nnext=next;
            else
                 if (nx==x+1)
                     nnext=0,ncur=next;
            else
                     if (nx>x+1)
                      nnext=ncur=0;
            //cout<<"       from "<<x<<" "<<y<<" "<<cur<<" "<<next<<" mv to "<<nx<<" "<<ny<<" "<<ncur<<" "<<nnext<<"\n";
            if (nx-x<=F)
             {
                    ret = min(ret , solve(nx,ny,ncur,nnext));
             }
     }
     
    Repk(2)
     {
            ny=y+mv[k];
            if (ny<0 || ny>=C || b[x][ny]!='.' || b[x+1][ny]=='.') continue;
           // cout<<"       from "<<x<<" "<<y<<" "<<cur<<" "<<next<<" dig "<<ny<<"\n";
            nnext=next;
            nnext|=1<<ny;
            ret = min(ret , 1 + solve(x,y,cur,nnext));
     }
     
  //  cout<<"=== "<<x<<" "<<y<<" "<<cur<<" "<<next<<" = "<<ret<<"\n";
    return ret;
}

int main()
{
    scanf("%d",&T);
    F(xx,T)
     {
            scanf("%d%d%d",&R,&C,&F);
            memset(a,0,sizeof(a));
            Repi(R)
             scanf("%s",a[i]);

            //cout<<"\n\n\n";
           //Repi(R) cout<<a[i]<<"\n";

            memset(dp,-1,sizeof(dp));
            int ans=0;
            ans=solve(0,0,0,0);
            if (ans==INF)
             printf("Case #%d: No\n",xx+1);
            else
             printf("Case #%d: Yes %d\n",xx+1,ans);
     }

    return 0;
}
