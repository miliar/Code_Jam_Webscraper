#include <iostream>

using namespace std;

const int tmax = 24 * 60 + 60;

int rdtm() {
	int h, m;
	char foo;
	
	cin >> h >> foo >> m;
	
	return h * 60 + m;
}

int main() {
	int nt, it;
	
	cin >> nt;
	for (it = 1; it <= nt; it++) {
		int tt, na, nb, i, v[2][tmax] = {0}, ta, tb, x, xmin;
		
		cin >> tt >> na >> nb;
		for (i = 0; i < na; i++) {
			ta = rdtm(), tb = rdtm();
			v[0][ta]--, v[1][tb + tt]++;
		}
		for (i = 0; i < nb; i++) {
			tb = rdtm(), ta = rdtm();
			v[1][tb]--, v[0][ta + tt]++;
		}
		
		cout << "Case #" << it << ": ";
		for (i = x = xmin = 0; i < tmax; i++) xmin = min(xmin, x += v[0][i]);
		cout << -xmin << ' ';
		for (i = x = xmin = 0; i < tmax; i++) xmin = min(xmin, x += v[1][i]);
		cout << -xmin << '\n';
	}
	
	return 0;
}
