#include <iostream>
#include <string>
#include <vector>

using namespace std;


const int INF = 1000000000;

int main() {
	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);

	int ts;
	cin >> ts;
	for (int tt=1; tt<=ts; ++tt) {

		int k;
		cin >> k;
		int n = 2 * k - 1;
		
		vector<int> c (n);
		int old_sz = 0;
		for (int i=0; i<n; ++i) {
			c[i] = i<k ? i+1 : n-i;
			old_sz += c[i];
		}

		vector < vector<int> > a (n);
		for (int i=0; i<n; ++i) {
			a[i].resize (c[i]);
			for (int j=0; j<c[i]; ++j)
				scanf ("%d", &a[i][j]);
		}

		int ans = INF;

		for (int iter=0; iter<2; ++iter) {
		
			int k2 = k*3 + iter,
				n2 = k2*2-1;

			vector<int> c2 (n2);
			for (int i=0; i<n2; ++i)
				c2[i] = i<k2 ? i+1 : n2-i;

			vector < vector<int> > a2 (n2);
			for (int i=0; i<n2; ++i)
				a2[i].resize (c2[i]);

			for (int cx=0; cx+n<=n2; ++cx)
				for (int cy=0; cy<c2[cx]; ++cy) {

					for (int i=0; i<n2; ++i)
						for (int j=0; j<c2[i]; ++j)
							a2[i][j] = -1;

					bool ok = true;
					int cxi=cx, cxj=cy;
					for (int i=0; i<k && ok; ++i) {
						for (int j=0; j<c[i] && ok; ++j)
							if (cxj+j >= c2[cxi])
								ok = false;
							else
								a2[cxi][cxj+j] = a[i][j];

						if (i+1 < k) {
							++cxi;
							if (cxi >= k2)
								--cxj;
							if (cxj < 0)
								ok = false;
						}
					}
					for (int i=k-1; i<n && ok; ++i) {
						for (int j=0; j<c[i] && ok; ++j)
							if (cxj+j >= c2[cxi])
								ok = false;
							else
								a2[cxi][cxj+j] = a[i][j];
						++cxi;
						if (cxi < k2)
							++cxj;
					}

					if (!ok)
						continue;
					
					for (int it=0; it<2; ++it) {

						for (int i=0; i<k2 && ok; ++i)
							for (int j=0; j<c2[i] && ok; ++j) {
								int & x = a2[i][j],
									& y = a2[n2-1-i][j];
								if (x != -1 || y != -1)
									if (x != -1 && y != -1 && x != y)
										ok = false;
									else {
										int sel = x != -1 ? x : y;
										x = y = sel;
									}
							}
						if (!ok)
							break;
						
						for (int i=0; i<n2 && ok; ++i)
							for (int j=0; j<c2[i]/2 && ok; ++j) {
								int & x = a2[i][j],
									& y = a2[i][c2[i]-1-j];
								if (x != -1 || y != -1)
									if (x != -1 && y != -1 && x != y)
										ok = false;
									else {
										int sel = x != -1 ? x : y;
										x = y = sel;
									}
							}
						if (!ok)
							break;

					}
					if (!ok)
						continue;

					int sz = k2,
						delta = 0;
					for (;;) {
						bool any = false;
						for (int i=delta; i<n2-delta; ++i) {
							if (delta > c2[i]-1-delta)
								continue;
							any |= a2[i][delta] != -1;
							any |= a2[i][c2[i]-1-delta] != -1;
						}
						if (any)
							break;
						--sz, ++delta;
					}

					int cur_sz = 0;
					for (int i=delta; i<n2-delta; ++i)
						for (int j=delta; j<c2[i]-delta; ++j)
							cur_sz++;

					ans = min (ans, cur_sz - old_sz);
					ans = ans;
				}

		}

		printf ("Case #%d: %d\n", tt, ans);
		cerr << tt << endl;
	}


}

