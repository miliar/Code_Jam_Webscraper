// solution by Peter Ondruska

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <climits>
#include <cstring>

#include <iostream>
#include <sstream>
#include <complex>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <stack>
#include <bitset>
#include <utility>
#include <numeric>
#include <functional>
#include <algorithm>
using namespace std;

typedef pair<int,int> PII;
typedef long long ll;

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORTO(i,a,b)  for(int i=(a);i<=(b);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)
#define FORDTO(i,a,b) for(int i=(a);i>=(b);i--)
#define FOREACH(it,t) for(typeof(t.begin()) it=t.begin(); it!=t.end(); ++it)

#define DEBUG(x) cout<<'>'<<#x<<':'<<x<<endl
#define SIZE(X) int(X.size())

#define MAX (1<<10)

#define INF 1000000000000LL

#define CLEAR(X) memset(X,0,sizeof(X))

ll DP[2*MAX][11];

ll M[MAX];

int main() {
	ll T;
	scanf("%lld", &T);
	FORTO(t,1,T) {
		ll P;
		scanf("%lld", &P);
		ll S = (1<<P);
		CLEAR(DP);
		CLEAR(M);
		
		FORD(i,S) {
			scanf("%lld", &M[i]);
			FORTO(j,0,M[i]) DP[S+i][j] = 0;
			FORTO(j,M[i]+1,P) DP[S+i][j] = INF;
		}
		
		FORDTO(i,S-1,1) {
			ll cost;
			scanf("%lld", &cost);
			ll a = 2*i+0, b = 2*i+1;
			FORTO(j,0,P) {
				// nevynecham
				DP[i][j] = DP[a][j]+DP[b][j] + cost;
				
				// vynecham
				if (j < P)
					DP[i][j] = min(DP[i][j],DP[a][j+1]+DP[b][j+1]);
			}
		}
		
		printf("Case #%d: %lld\n", t, DP[1][0]);
	}
	return 0;
}
