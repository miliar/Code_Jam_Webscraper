#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
using namespace std;

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (int i((n)-1); i >= 0; --i)
#define ALL(c) (c).begin(), (c).end()

typedef long long int64;
typedef unsigned long long uint64;

template<typename T> int size(const T& c) { return (int)c.size(); }
template<typename T> void remin(T& a, const T& b) { if (b < a) a = b; }
template<typename T> void remax(T& a, const T& b) { if (b > a) a = b; }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }

const char *o(bool b){
	return b? "ON":"OFF";
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int T, N, K;
	scanf("%d", &T);

	FOR(test, 1, T) {
		scanf("%d%d", &N, &K);

		bool snappers[N+1];

		REP(j, N+1){
			snappers[j] = false;
		}
		snappers[0]=true;

		REP(i, K) {
			int m=N;
			FOR(j, 1, N+1) {
				if(snappers[j-1]){
				}else{
					m=j-1;
					break;
				}
			}
			if(m==0){m=1;}
			FOR(j, 1, m) {
				snappers[j]=!snappers[j];
			}
		}

		bool light=true;
		REP(j, N+1) {
			if (!snappers[j]){
				light=false;
				break;
			}
		}

		printf("Case #%d: %s\n", test, o(light)  );
	}

	exit(0);
}
