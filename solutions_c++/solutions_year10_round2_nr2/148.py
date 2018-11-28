/*
Compiled and Tested using Visual C++ 2008 Express Edition.
ONLINE_JUDGE is a macro for the Sphere Online Judge (SPOJ), where G++
compilers are used.
*/

#define _CRT_SECURE_NO_WARNINGS
//#define TEST

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<list>
#include<deque>
#include<vector>
#include<algorithm>
#include<queue>
#include<set>
#include<map>
#include<string>
#include<time.h>
using namespace std;

#ifndef ONLINE_JUDGE
#include<hash_map>
using namespace stdext;
#else
#include<ext/hash_map>
using namespace __gnu_cxx;

namespace __gnu_cxx {
	template<> struct hash<string> {
		size_t operator()(const string& x) const {
			return hash<const char*>() (x.c_str());
		}
	};
}
#endif

int x[60], v[60];
bool obstacle[60];

int main(void) {
#ifndef ONLINE_JUDGE
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
#endif
	int tt, it, n, k, b, t, i, obs, reach, result;
	scanf("%d", &tt);
	for(it = 1; it <= tt; it++) {
		scanf("%d %d %d %d", &n, &k, &b, &t);
		for(i = 0; i < n; i++) {
			scanf("%d", &x[i]);
			x[i] = b - x[i];
		}
		for(i = 0; i < n; i++) {
			scanf("%d", &v[i]);
			obstacle[i] = (t * v[i] < x[i]);
		}
		result = obs = reach = 0;
		for(i = n - 1; i >= 0 && reach < k; i--) {
			if(obstacle[i])
				obs++;
			else {
				result += obs;
				reach++;
			}
		}
		if(reach >= k)
			printf("Case #%d: %d\n", it, result);
		else
			printf("Case #%d: IMPOSSIBLE\n", it);
	}
}
