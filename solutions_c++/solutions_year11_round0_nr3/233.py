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

int main(void)
{
	ios_base::sync_with_stdio(false);

	UI t; cin >> t;
	for(UI i=0;i<t;++i) {

		UI n; cin >> n;
		vector<UI> v(n); for(auto &val:v){cin>>val;}
		tuple<UI, UI, UI> tup(0, 0, v[0]); // xorsum, sum, min
		tup = accumulate(RNG(v), tup, [](tuple<UI,UI,UI> t, UI n) {
			return make_tuple(get<0>(t) ^ n, get<1>(t) + n, min(get<2>(t), n));
		});
		cout << "Case #" << i+1 << ": ";
		if(get<0>(tup) != 0) {
			cout << "NO" << endl;
		} else {
			cout << get<1>(tup) - get<2>(tup) << endl;
		}
	}

	return 0;
}
