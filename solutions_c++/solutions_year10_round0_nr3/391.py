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

#define MAXN 1047

ll G[MAXN];
ll P[MAXN]; // next index
ll S[MAXN];

int main() {
	ll T, N, R, K;
	scanf("%lld", &T);
	FORTO(t,1,T) {
		scanf("%lld %lld %lld", &R, &K, &N);
		FOR(i,N) scanf("%lld", &G[i]);
		
		ll j = 0, sum = 0;
		FOR(i,N) {
			while (sum + G[j] <= K) {
				sum += G[j];
				j = (j+1)%N;
				if (i == j) break;
			}
			S[i] = sum;
			sum -= G[i];
			P[i] = j;
		}
		
		ll res = 0, p = 0;
		FOR(i,R) {
			res += S[p];
			p = P[p];
		}
		
		printf("Case #%d: %lld\n", t, res);
	}
	return 0;
}
