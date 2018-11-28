#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>
#include <complex>
#include <set>
#include <map>
using namespace std;

typedef long double ld;
typedef pair<int, int> ii;

int X, S, R, T, N;

ii walks[1024];

int main() {
	int TT;
	cin >> TT;
	for (int tt = 1; tt <= TT; ++tt) {
		cin >> X >> S >> R >> T >> N;
		int left = X;
		for (int i = 0; i < N; ++i) {
			int B, E;
			cin >> B >> E;
			int L = E - B;
			walks[i].second = L;
			cin >> walks[i].first;
			left -= L;
		}
		if (left < 0) {
			cerr << "ERROR!" << endl;
		}
		walks[N].second = left;
		walks[N].first = 0;
		++N;
		sort(walks, walks + N);
		ld total = 0;
		ld tleft = T;
		for (int i = 0; i < N; ++i) {
			if (walks[i].second == 0) continue;
			ld rspeed = walks[i].first + R;
			ld wspeed = walks[i].first + S;
			ld tneed = walks[i].second / rspeed;
			/*
			cout << " w=" << walks[i].first << " dist=" << walks[i].second
				<< " rspeed=" << rspeed
				<< " tleft=" << tleft
				<< " tneed=" << tneed
				<< endl;
			*/
			if (tneed > tleft) {
				ld rdist = rspeed * tleft;
				total += tleft;
				ld wdist = (walks[i].second - rdist);
				ld wtime = wdist / wspeed;
				total += wtime;
				tleft = 0;
			} else {
				tleft -= tneed;
				total += tneed;
			}
			// cout << " total=" << total << endl;
		}
		cout.setf(ios::fixed);
		cout.precision(9);
		cout << "Case #" << tt << ":";
		cout << " " << total;
		cout << endl;
	}
	return 0;
}

