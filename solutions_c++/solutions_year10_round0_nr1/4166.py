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

int main()
{
	freopen("A-large.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int T;
	scanf("%d", &T);
	FOR(test, 1, T)
	{
		int N, K;
		scanf("%d%d", &N, &K);
		//printf("N is %d", N);
		//printf("K is %d", K);
		bool on = true;
		REP(i, N)
		{
			//printf("i is %d\n", i);
			//printf("K is %x\n", K);
			if (!(K & int(1)))
			{
				//printf("failed on i = %d",i);
				on = false;
				break;
			}
			else
			{
				K = K >> 1;
			}
		}
		printf("Case #%d: %s\n", test, on ? "ON" : "OFF");
	}

	exit(0);


}