#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <climits>
//#define NDEBUG
#include <cassert>
using namespace std;
#define memsetz(NAME) memset(NAME, 0, sizeof(NAME))
typedef long long i64;

int mx[1000], my[1000];
int main()
{
	int T; cin >> T;
	for (int caseNum = 1; caseNum <= (int)T; caseNum++) {
		printf("Case #%d: ", caseNum);
		int n; cin >> n;
		int X = 0;
		for (int i = 0; i < (int)n; i++) {
			cin >> mx[i]/**/ ;
			my[i] = mx[i];
			X += mx[i];
		}
		sort(my, my + n);
		for (int i = 0; i < (int)n; i++) {
			double minv = 1000;
			bool sign = false;
			int tot = 0;
			for (int j = 0; j < (int)n; j++) {
				tot += my[j];
				if (my[j] == mx[i]) sign = true/**/ ;
				int xr = tot;
				int nr = j + 1;
				if (sign) { xr -= mx[i]; nr--;}
				double yc;
				if (nr == 0) continue;
//				cout << xr + X - nr * mx[i] << endl;
//				cout << nr * X + X << endl;
				yc = (double)(xr + X - nr * mx[i]) * 100 / (nr * X + X);
				minv = min(yc, minv);
			}
			minv = max(minv, 0.0);
			printf("%.7lf", minv);
			if (i + 1 == n) puts("");
			else printf(" ");
		}
	}
	return 0;
}
