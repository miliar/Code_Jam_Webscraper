#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <utility>
#include <set>
#include <map>
#include <queue>
using namespace std;

#define mset(A,B) memset(A,B,sizeof(A));
#define mcpy(A,B) memcpy(A,B,sizeof(B));
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
#define FI(I,L,U) for (int I=L;I<U;I++)
#define sqr(x) ((x)*(x))

using namespace std;

int main()
{
   int T;
   cin>>T;
   
   int ans = 0;
   int M,V;

   int G[20000],C[20000];
   int dp[20000][2];

   int INF = 1000000000;
   for (int c = 1;c<=T;c++)
   {
	   cin >>M >> V;
	   for (int i = 1;i<=(M-1)/2;i++)
	   {
		   cin >> G[i] >>C[i];
	   }
	   for (int i = (M-1)/2+1;i<=M;i++)
	   {
		   int value; 
		   cin>>value;
		   dp[i][value]=0;
		   dp[i][1-value]=INF; // impossible
	   }
	   for (int i = (M-1)/2;i>=1;i--)
	   {
		       dp[i][0] = dp[i][1] = INF;
			   for (int i1= 0;i1<2;i1++)
				   if (dp[i*2][i1]!=INF)
				   for (int j1=0;j1<2;j1++)
					   if (dp[i*2+1][j1]!=INF)
					   {
						   int v;

						   int i2 = j1;
						   if (G[i] == 1) v = i1 & i2; else v = i1 | i2;
						   int cost = dp[i*2][i1] + dp[i*2+1][j1];
						   if (cost < dp[i][v]) dp[i][v] = cost;

						   if (C[i] == 1) //change
						   {
						   if (G[i] == 0) v = i1 & i2; else v = i1 | i2;
						   int cost = dp[i*2][i1] + dp[i*2+1][j1] + 1;
						   if (cost < dp[i][v]) dp[i][v] = cost;

						   }
					   }
	   }
	   if (dp[1][V] <INF)
	   printf("Case #%d: %d\n", c , dp[1][V]);
	   else
		   printf("Case #%d: IMPOSSIBLE\n", c);
   }
   return 0;
}
