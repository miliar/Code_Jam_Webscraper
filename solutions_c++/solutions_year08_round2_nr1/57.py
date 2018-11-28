// solution by Peter Ondruska

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <climits>
#include <cstring>

#include <iostream>
#include <iomanip>
#include <sstream>
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
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long int ll;
typedef long double ld;
typedef pair<ld,ld> PDD;
typedef pair<ll,ll> PLL;

#define FOR(i,n)      for(int i=0;i<n;i++)
#define FORTO(i,a,b)  for(int i=a;i<=b;i++)
#define FORD(i,n)     for(int i=n-1;i>=0;i--)
#define FORDTO(i,a,b) for(int i=b;i>=a;i--)
#define FOREACH(it,t) for(typeof(t.begin()) it=t.begin(); it!=t.end(); ++it)

#define DEBUG(x) cout<<'>'<<#x<<':'<<x<<endl
#define $ size()
#define ALL(x) (x).begin(),(x).end()
#define PB push_back

//template<class T> T min(T a, T b) { return a < b ? a : b; }
//template<class T> T max(T a, T b) { return a > b ? a : b; }

typedef struct {
	int x, y;
} Point;

Point P[123456];

int main() {
	int C;
	scanf("%d", &C);
	FORTO(c,1,C) {
		ll T[3][3] = { { 0, 0, 0 }, {0, 0, 0}, {0, 0, 0} };
		ll N, A, B, C, D, X, Y, M;
		scanf("%lld %lld %lld %lld %lld %lld %lld %lld", &N, &A, &B, &C, &D, &X, &Y, &M);
		FOR(i,N) {
			T[X%3][Y%3]++;
			P[i].x = X, P[i].y = Y;
			X = (A*X + B) % M;
			Y = (C*Y + D) % M;
		}
		ll R = 0;
		FOR(x1,3) FOR(y1,3)
			FOR(x2,3) FOR(y2,3) {
				int x3 = (6-x1-x2)%3;
				int y3 = (6-y1-y2)%3;
				ll a = T[x1][y1];
				ll b = T[x2][y2];
				ll c = T[x3][y3];
				
				if (x1 == x2 && y1 == y2) b--;
				if (x2 == x3 && y2 == y3) c--;
				if (x1 == x3 && y1 == y3) c--;
				
				R += a * b * c;
			}
		printf("Case #%d: %lld\n", c, R/6);
	}
	return 0;
}
