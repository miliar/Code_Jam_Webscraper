#include <algorithm>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <string>
#include <cctype>
#include <cmath>
#include <set>
#include <map>

using namespace std;

int N, M, A;

void read_data () {
	cin >> N >> M >> A;
}

void solve () {
	for (int x3 = 1; x3 <= N; ++x3)
		for (int x2 = 0; x2 <= x3; ++x2)
			for (int y2 = 0; y2 <= M; ++y2)
				for (int y3 = 0; y3 <= M; ++y3)
					if (abs (x2*y3 - x3*y2) == A) { cout << "0 0 " << x2 << " " << y2 << " " << x3 << " " << y3 << endl; return; }

	cout << "IMPOSSIBLE" << endl;
}

int main () {
	freopen ("B-small-attempt0.in", "r", stdin);

	int Ct;
	cin >> Ct;

	for (int t = 0; t < Ct; ++t) {
		printf ("Case #%d: ", t+1);

		read_data ();
		solve ();
	}

	return 0;
}
