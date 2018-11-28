#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <numeric>

using namespace std;

// Airport Walkways

int main()
{
	int cases;
	cin >> cases;

	for (int caseno = 1; caseno <= cases; caseno++) {
		int X, S, R, N;
		double t;
		cin >> X >> S >> R >> t >> N;
		vector <pair <int, int> > c;
		for (int i = 0; i < N; i++) {
			int B, E, w;
			cin >> B >> E >> w;
			c.push_back(make_pair(w, E - B));
			X -= E - B;
		}
		c.push_back(make_pair(0, X));
		sort(c.begin(), c.end());
		double ret = 0;
		for (int i = 0; i < c.size(); i++) {
			double r = min(t, (double)c[i].second / (R + c[i].first));
			t -= r;
			ret += r + (c[i].second - r * (R + c[i].first)) / (S + c[i].first);
		}
		cout << "Case #" << caseno << ": " << setprecision(10) << ret << endl;
	}

	return 0;
}
