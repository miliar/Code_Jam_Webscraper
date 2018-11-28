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

#define INF 2000000000
#define EPS 1e-6

#define Time ((double)clock()/CLOCKS_PER_SEC)
#define pause system("pause")

using namespace std;
const int MOD=10007;
int n,m,N,M,P,T,K,H,W,R;
bool a[128][128];
int dp[128][128];
PI mv[2];
int main()
{
	mv[0]=MP(2,1); mv[1]=MP(1,2);
    scanf("%d",&N);
    Repi(N)
     {
			scanf("%d%d%d",&H,&W,&R);int x,y;
			memset(a,0,sizeof(a));
			Repj(R)
			 {
					scanf("%d%d",&x,&y);
					a[x][y]=1;
			 }
			memset(dp,0,sizeof(dp));
			dp[1][1]=1;
			for (int i=1;i<=H;i++)
			 for (int j=1;j<=W;j++)
			  {
					if (a[i][j]) continue;
					Repk(2)
					  {
							x=i-mv[k].x,y=j-mv[k].y;
							if (x<=0 || y<=0) continue;
							dp[i][j]=(dp[x][y]+dp[i][j])%MOD;
					  }
			  }
			printf("Case #%d: %d\n",i+1,dp[H][W]);
	 }
    return 0;
}
