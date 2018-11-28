#include <iostream>
#include <vector>
using namespace std;

#define N 55

vector<vector<char> > v(N);

int i, j, k,n , m, t, T, x, y, z, r, res;

int ch(vector<char> &x, int n) {
	int i;
	for (i = n + 1; i < x.size(); i ++) {
		if (x[i] == '1') {
			return 0;
		}
	}
	return 1;
}


int main()  {
	freopen("large.in", "r", stdin);
	freopen("large.out", "w", stdout);
	cin >> T;
	for (t =1;t <= T; t ++) {
		cin >> n;
		for (i= 0; i < n; i ++) {
			v[i].clear();
			v[i].resize(n);
		}
		for ( i= 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				cin >> v[i][j];
			}
		}
		res = 0;
		for (i = 0; i < n; i ++) {
			if (!ch(v[i], i)) {
				for (j = i + 1; j < n; j ++) {
					if (ch(v[j], i)) {
						break;
					}
				}
				x = j;
				for (j = x - 1; j >= i; j --) {
					swap(v[j], v[j+1]);
					res ++;
				}
			}
		}
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}




