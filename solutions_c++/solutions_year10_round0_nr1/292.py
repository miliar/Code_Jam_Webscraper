#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <string>
using namespace std;

#define CLR(a, x) memset(a, x, sizeof(a)) // x = 0|-1, true|false.
#define REP(i, n) for(int i=0; i<(n); i++)
#define FOR(i, a, b) for(int i=(a); i<=(b); i++)
#define FORD(i, b, a) for(int i=(b); i>=(a); i--)
#define FORE(ty, it, data) for(ty::iterator it=data.begin(); it!=data.end(); it++)
#define ALL(x) (x).begin(),(x).end()
#define TWO(X) (1<<(X))
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define EPS 1e-10
const double PI = acos(-1.0);

typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef map<string, int> MSI;

template<typename T> string toString(const T &n) { ostringstream O; O<<n; return O.str(); }

////////////////////////////////////////////////////////////////////////////////////////////////////////

ll func(int N)
{
	ll table[33];
	table[1] = 1;
	FOR(i, 2, N) {
		table[i] = table[i-1]*2 + 1;
	}
	return table[N];
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	scanf("%d\n", &T);
	FOR(tc, 1, T) {
		printf("Case #%d: ", tc);
		int N, K;
		scanf("%d %d", &N, &K);

		ll period = func(N);

		ll rest = K - period;
		if(rest >=0 && rest%(period+1)==0) {
			printf("ON\n");
		}
		else	printf("OFF\n");


		fprintf(stderr, "Case #%d Finished!\n", tc);
	}

	return 0;
}