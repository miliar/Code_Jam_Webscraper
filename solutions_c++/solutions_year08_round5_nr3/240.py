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

int n,m,N,M,P,T,K;
int dp[16][1<<11];
char s[123][234];
int rock[16];

int main()
{
    scanf("%d",&T);
    Repi(T)
     {
			scanf("%d%d",&N,&M);
			Repi(N)
			 scanf("%s\n",s[i]);
		//	Repi(N)
		//	 cout<<s[i]<<endl;
			memset(dp,0,sizeof(dp));
			memset(rock,0,sizeof(rock));
			Repi(N)
			 Repj(M)
			  if (s[i][j]=='x')
			   rock[i]|=1<<j;
		//	Repi(N)
		//	 cout<<bitset<7>(rock[i])<<endl;
			
			dp[0][0]=1;
			int best=0;
			Repi(N)
			 Repj(1<<M)
			 {
			 // cout<<"in "<<i<<" "<<bitset<6>(j)<<" = "<<dp[i][j]<<endl;
			  if (dp[i][j])
			   {
					Repk(1<<M)
					 if (!(k&rock[i]))
					  {
							bool ok=1;
							Repi(M-1)
							 if ((k&(1<<i)) && (k&(1<<i+1)))
							  { ok=0; break; }
							if (!ok) continue;
							Repi(M-1)
							 if ((j&(1<<i+1)) && (k&(1<<i)))
							  { ok=0; break; }
							if (!ok) continue;
							for (int i=1;i<M;i++)
							 if ((j&(1<<i-1)) && (k&(1<<i)))
							  { ok=0; break; }
							if (!ok) continue;
							
						//	cout<<"   from "<<i<<" "<<bitset<6>(j)<<" to "<<bitset<6>(k)<<" <=> "<<dp[i+1][k]<<" >?= "<<dp[i][j]<<" + "<<__builtin_popcount(k)<<endl;
							dp[i+1][k]=max(dp[i+1][k],dp[i][j]+__builtin_popcount(k));
							if (i+1==N) best=MAX(best,dp[i+1][k]);
					  }
		       }
			 } 
		    printf("Case #%d: %d\n",i+1,best-1);
	 }
    
    return 0;
}
