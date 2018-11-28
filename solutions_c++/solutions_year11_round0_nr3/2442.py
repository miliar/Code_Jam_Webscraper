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
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
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

//[a, b) incrementando
#define FORN(i, a, b) for(typeof(b) i = (a); i < (b); i++)
//(a, b] decrementando
#define FORR(i, a, b) for(typeof(a) i = (a) - 1; i >= (b) && i < (a) ; i--)

#define ALL(x) x.begin(), x.end()
#define FOREACH(i, c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define FOREACHR(i, c) for(typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); i++)



int main()
{
	int NTC;
	scanf("%d", &NTC);
	FORN(TC, 0, NTC){
		int n;
		scanf("%d", &n);
		int min = INT_MAX;
		int sum = 0;
		int acc_xor = 0;
		FORN(i, 0, n){
			int v;
			scanf("%d", &v);
			if(v < min) min = v;
			sum += v;
			acc_xor ^= v;
		}
		printf("Case #%d: ", TC + 1);
		if(acc_xor){
			printf("NO\n");
		}else{
			printf("%d\n", sum - min);
		}
	}
}
