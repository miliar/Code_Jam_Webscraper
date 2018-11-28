#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

int main() {

	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int T;
	int bb = 1;
	scanf("%d", &T);
	while (T--) {
		int n;
		scanf("%d", &n);
		int orz = 0;
		int mmin = INT_MAX;
		int sum = 0;
		for (int i = 0; i < n; ++i) {
			int t;
			scanf("%d", &t);
			orz = orz ^ t;
			mmin = min(mmin, t);
			sum += t;
		}
		printf("Case #%d: ", bb++);
		if (orz) {
			puts("NO");
		} else {
			printf("%d\n", sum - mmin);
		}
	}

	return 0;
}

