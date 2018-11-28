#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>
#include <complex>
#include <set>
#include <map>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<ll, ll> ii;

int R, C, D;

ll mass[512][512];
ll left_mass[512][512];
ll rect_mass[512][512];

// moment
ii moment[512][512];
ii left_mom[512][512];
ii rect_mom[512][512];

ii get_mom(int r, int c) {
	if (r < 0 || c < 0) return ii(0, 0);
	return rect_mom[r][c];
}

ll get_mass(int r, int c) {
	if (r < 0 || c < 0) return 0;
	return rect_mass[r][c];
}

bool checker(int r, int c, int k) {
	ld r1 = r + k * 0.5;
	ld c1 = c + k * 0.5;
	ld sumr = 0, sumc = 0;
	for (int i = 0; i <= k; ++i) {
		for (int j = 0; j <= k; ++j) {
			if (i == 0 && j == 0) continue;
			if (i == k && j == 0) continue;
			if (i == 0 && j == k) continue;
			if (i == k && j == k) continue;
			ld rz = r + i;
			ld cz = c + j;
			ld rdist = rz - r1;
			ld cdist = cz - c1;
			sumr += rdist * mass[r + i][c + j];
			sumc += cdist * mass[r + i][c + j];
		}
	}
	// cout << " r=" << r << " c=" << c << " k=" << k << " sr=" << sumr << " sc=" << sumc << endl;
	return (sumr == 0 && sumc == 0);
}

bool run(int r, int c, int k) {
	ii Ao = get_mom(r-1, c-1);
	ii Bo = get_mom(r-1, c+k);
	ii Co = get_mom(r+k, c-1);
	ii Do = get_mom(r+k, c+k);
	ll Am = get_mass(r-1, c-1);
	ll Bm = get_mass(r-1, c+k);
	ll Cm = get_mass(r+k, c-1);
	ll Dm = get_mass(r+k, c+k);
	// D + A - C - B
	ll x = Do.first + Ao.first - Co.first - Bo.first
		- moment[r][c].first - moment[r][c+k].first - moment[r+k][c].first - moment[r+k][c+k].first;
	ll y = Do.second + Ao.second - Co.second - Bo.second
		- moment[r][c].second - moment[r][c+k].second - moment[r+k][c].second - moment[r+k][c+k].second;
	ll m = Dm + Am - Cm - Bm - mass[r][c] - mass[r][c+k] - mass[r+k][c] - mass[r+k][c+k];
	x *= 2;
	y *= 2;

	/*
	   cout << " r=" << r << " c=" << c << " k=" << k
	   << " x=" << x << " y=" << y << " m=" << m << endl;
	 */

	if (m == 0) {
		if (x != 0) return false;
		if (y != 0) return false;
		return true;
	} else {
		if (x % m != 0) return false;
		if (y % m != 0) return false;
	}

	ll ax = 0;
	ll ay = 0;

	if (m != 0) {
		ax = x / m;
		ay = y / m;
	}

	ll wx = 2 * r + k;
	ll wy = 2 * c + k;

	/*
	   cout << " wx=" << wx << " wy=" << wy
	   << " k=" << k
	   << " x=" << x << " y=" << y << " m=" << m
	   << " ax=" << ax << " ay=" << ay
	   << endl;
	 */

	if (ax == wx && ay == wy) {
		return true;
	}
	return false;
}

int main() {
	int TT;
	cin >> TT;
	for (int tt = 1; tt <= TT; ++tt) {
		cin >> R >> C >> D;
		for (int r = 0; r < R; ++r) {
			string line;
			cin >> line;
			if (line.size() != C) {
				cerr << "ERROR!" << endl;
			}
			for (int c = 0; c < C; ++c) {
				mass[r][c] = ((ll)line[c]) + 0 - '0';
				moment[r][c] = ii(mass[r][c] * r, mass[r][c] * c);
			}
		}
		for (int c = 0; c < C; ++c) {
			rect_mom[0][c] = ii(0, 0);
			rect_mass[0][c] = 0;
		}
		for (int r = 0; r < R; ++r) {
			left_mom[r][0] = ii(0, 0);
			left_mass[r][0] = 0;
			for (int c = 0; c < C; ++c) {

				if (c > 0) {
					left_mom[r][c] = left_mom[r][c-1];
					left_mass[r][c] = left_mass[r][c-1];
				}
				left_mom[r][c].first += moment[r][c].first;
				left_mom[r][c].second += moment[r][c].second;
				left_mass[r][c] += mass[r][c];
				if (r > 0) {
					rect_mom[r][c] = rect_mom[r-1][c];
					rect_mass[r][c] = rect_mass[r-1][c];
				}
				rect_mom[r][c].first += left_mom[r][c].first;
				rect_mom[r][c].second += left_mom[r][c].second;
				rect_mass[r][c] += left_mass[r][c];
			}
		}
		/*
		   for (int r = 0; r < R; ++r) {
		   for (int c = 0; c < C; ++c) {
		   cout << rect_mass[r][c] << " ";
		   }
		   cout << endl;
		   }
		 */
		int best_k = 1;
		for (int r = 0; r < R; ++r) {
			for (int c = 0; c < C; ++c) {
				int k = best_k;
				while (true) {
					++k;

					// check if k is valid
					if (r + k >= R || c + k >= C) break;

					// cout << " c=" << c << " r=" << r << " k=" << k << endl;

					bool b1 = run(r, c, k);

					/*
					bool b2 = checker(r, c, k);
					if (b1 != b2) {
						cout << "ERROR " << b1 << " " << b2 << endl;
					}
					*/

					if (b1) {
						best_k = max(best_k, k);
					}

				}
			}
		}
		cout << "Case #" << tt << ": ";
		if (best_k == 1) {
			cout << "IMPOSSIBLE";
		} else {
			cout << best_k+1;
		}
		cout << endl;
	}
	return 0;
}

