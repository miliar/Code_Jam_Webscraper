#include <iostream>
#include <sstream>

#include <iterator>

#include <algorithm>
#include <numeric>
#include <utility>
#include <limits>

#include <string>

#include <vector>
#include <deque>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>

#include <tuple>
#include <initializer_list>

#include <cmath>

typedef unsigned long long ULL;
typedef long long LL;
typedef unsigned long UL;
typedef unsigned int UI;
typedef unsigned short US;
typedef unsigned char UC;

#define RNG(v) (v).begin(), (v).end()

using namespace std;

inline UI absdiff(UI a, UI b) { return a > b ? a - b : b - a; }

int main(void)
{
	ios_base::sync_with_stdio(false);

	UI t; cin >> t;
	for(UI i=0;i<t;++i) {
		UI p[2] = { 1, 1 }, t[2] = { 0, 0 };
		UI cur = 0, prev = 0;

		UI n; cin >> n;
		for(UI j=0;j<n;++j) {
			char c; UI r; cin >> c >> r; cur = c == 'B' ? 0 : 1;
			t[cur] = max(t[prev] + 1, t[cur] + absdiff(p[cur], r) + 1);
			p[cur] = r; prev = cur;
		}
		cout << "Case #" << i+1 << ": " << t[cur] << endl;
	}
	return 0;
}
