/*Author :: Yash*/
#include <iostream>
#include <cassert>
#include <algorithm>
#include <iomanip>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <climits>
#include <iterator>
#include <utility>
#include <functional>
#include <bitset>
#include <cctype>
#include <list>
#include <set>
#include <map>
using namespace std;

#define PB push_back
#define PF push_front
#define PP pop()
#define EM empty()
#define FOR(i,a,b) for(int i = (int )a;i<(int )b;i++)
#define REP(i,n) FOR(i,0,n)

typedef pair<int,int> pi;
typedef pair<int,pi> tri;
typedef vector<pi> vii;
typedef vector<tri> viii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<vi> vvi;

#define MOD 1000000007

int main()
{
	int No;
	scanf("%d",&No);
	for(int kases=1;kases<=No;kases++)
	{
		int n,m,X,Y,Z;
		cin >> n >> m >> X >> Y >> Z;
		X %= Z;
		Y %= Z;
		int A[m];
		REP(i,m) scanf("%d",&A[i]);
		/*for i = 0 to n-1
			  print A[i mod m]
				    A[i mod m] = (X * A[i mod m] + Y * (i + 1)) mod Z*/
		int B[n];
		REP(i,n)
		{
			B[i] = A[i%m];
			A[i%m] = ((long long )X*(long long )(A[i%m]%Z) + ((long long )Y*(long long )(i+1))%Z)%Z;
		}
		int N = n;

		long long  DP[N][N],ans = 0;
		memset(DP,0,sizeof(DP));
		REP(i,N) (DP[0][i] = 1);

		FOR(i,1,N) 
		{
			FOR(j,1,N) 
			{
				FOR(k,i-1,j) 
				{
					if(B[j] > B[k]) DP[i][j] = (DP[i][j]+DP[i-1][k])%MOD;
				}
			}
		}


		for(int i=0;i<N;i++)
			for(int j=i;j<N;j++)
			{
				ans = (ans + DP[i][j])%MOD;
			}
		printf("Case #%d: %lld\n",kases,ans);

	}
	return 0;
}


