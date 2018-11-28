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
#include <list>
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

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	uint64 T, k, R, N;
	scanf("%lld", &T);

	uint64 g;
	list<uint64> gl;
  list<uint64>::iterator it;
	FOR(test, 1, T) {
		scanf("%lld%lld%lld", &R, &k, &N);

		gl.clear();
		REP(i, N) {
			scanf("%lld", &g);
			gl.push_back(g);
		}

		uint64 sum;
		uint64 Euros=0;
    uint64 c;
		REP(i, R) {
			sum=c=0;
			while(true){
				if (c++ < N && sum + gl.front() <= k){
					sum += gl.front();
					gl.push_back(gl.front());
					gl.pop_front();
				}else{
					Euros += sum;
					break;
				}
			}
		}
		
		printf("Case #%d: %lld\n", test, Euros );
	}

	exit(0);
}
