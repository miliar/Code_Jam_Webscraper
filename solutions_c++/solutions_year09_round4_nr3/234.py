#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>

using namespace std;


const int INF = 1000000;

bool cmp (vector<int> &a, vector<int> &b) {
	for (size_t i=0; i<a.size(); ++i)
		if (! (a[i] < b[i]))
			return false;
	return true;
}

int n, k, d[20][100000];
vector<int> a[100];

int get_d (int pos, int msk) {
	int & my = d[pos][msk];
	if (my != -1)  return my;
	if (pos == n)  return 0;
	
	my = 1 + get_d (pos+1, msk | (1<<pos));
	for (int i=0; i<pos; ++i)
		if (msk & (1<<i))
			if (cmp (a[i], a[pos]))
				my = min (my, get_d (pos+1, msk ^ (1<<i) | (1<<pos)));

	return my;
}

int main() {
	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);

	int ts;
	cin >> ts;
	for (int tt=0; tt<ts; ++tt) {
		cin >> n >> k;
		for (int i=0; i<n; ++i) {
			a[i].resize (k);
			for (int j=0; j<k; ++j)
				cin >> a[i][j];
		}
		
		sort (a, a+n);

		memset (d, -1, sizeof d);
		int ans = get_d (0, 0);
		printf ("Case #%d: %d\n", tt+1, ans);
	}

}
