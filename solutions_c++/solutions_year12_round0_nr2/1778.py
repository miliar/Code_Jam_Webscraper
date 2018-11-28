#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdint.h>
#include <string>
#include <utility>
#include <vector>

using namespace std;

//#define NDEBUG
#if defined(NDEBUG)
#define DBG_CODE(cb...)
#else
#define DBG_CODE(cb...) cb
#endif
#define WRITE(x) DBG_CODE(cout << x << endl)
#define WATCH(x) DBG_CODE(cout << #x << "=" << x << endl)
#define FORN(i, a, b) for(typeof(b) i = (a); i < (b); i++)
#define ALL(x) x.begin(), x.end()
#define FOREACH(i, c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

int best_not_surprising(const int t)
{
	static const int plus[] = {0, 1, 1};
	return t / 3 + plus[t % 3];
}

int best_surprising(const int t)
{
	static const int mint[] = {3, 4, 2};
	static const int plus[] = {1, 1, 2};
	if(t < mint[t % 3]) return 0;
	return t / 3 + plus[t % 3];
}

int main(){
	int ntc;
	scanf("%d", &ntc);
	FORN(tc, 0, ntc){
		int n, s, p;
		scanf("%d%d%d", &n, &s, &p);
		int counter = 0;
		FORN(i, 0, n){
			int t;
			scanf("%d", &t);
			if(best_not_surprising(t) >= p){
				counter++;
			}else if(s and best_surprising(t) >= p){
				counter++;
				s--;
			}
		}
		printf("Case #%d: %d\n", tc + 1, counter);
	}
}
