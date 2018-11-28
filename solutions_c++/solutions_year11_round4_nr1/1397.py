//#include <iostream>
#include <fstream>
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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

//ifstream cin("A-small-attempt3.in"); ofstream cout("A-small-attempt3.out");
ifstream cin("A-large.in"); ofstream cout("A-large.out");

int main() {
	int T;
	cin >> T;
	for (int tt=1; tt<=T; tt++) {
		cout << "Case #" << tt << ": ";
		int X, S, R, t, N;
		cin >> X >> S >> R >> t >> N;
		vector < pair <int, int> > V;
		int t1, t2, t3;
		for (int i=0; i<N; i++) {
			cin >> t1 >> t2 >> t3;
			V.push_back (make_pair(t3, t2-t1));
			X -= t2-t1;
		}
		
		sort(V.begin(), V.end());
		double ans = 0;
		double cur = 0;
		double tr = (double)t;
		double tmp = 0;
		
		tmp = min((double)(X) / (double)R, tr);
		ans += tmp;
		tr -= tmp;
		cur += tmp* (double)R;
		tmp = ((double)(X-cur) / (double)S);
		ans += tmp;
		for (int i=0; i<N; i++) {
			cur = 0;
			if (tr > 0) {
				tmp = min((double)(V[i].second) / (double)(R+V[i].first), tr);
				ans += tmp;
				tr -= tmp;
				cur += tmp* (double)(R+V[i].first);
			}
			tmp = (double)(V[i].second - cur) / (double)(S+V[i].first);
			ans += tmp;
		}
		cout << setprecision(14) << ans << endl;

	}
	return 0;
}
