#include <iostream>
#include <vector>
using namespace std;

vector<int> q1, q2, q3;
int ans, f[101][102][102], a[100][2], test, n, m;

void relax(int i, int r, int j, int k, int r1, int r2)
{
	for (int o = -r1; o <= r1; ++o)
		for (int p = -r2; p <= r2; ++p)
			if (j + o && k + p && j + o <= m && k + p <= m && !f[i + r][j + o][k + p]) {
				f[i + r][j + o][k + p] = f[i][j][k] + 1;
				q1.push_back(i + r);
				q2.push_back(j + o);
				q3.push_back(k + p);
			}
	return;
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	cin >> test;
	for (int te = 0; te < test; ++te) {
		memset(f, 0, sizeof(f));
		q1.clear();
		q2.clear();
		q3.clear();
		cin >> n; char ch; m = 0;
		for (int i = 0; i < n; ++i) {
			cin >> ch;
			a[i][0] = ch == 'O' ?0 :1;
			cin >> a[i][1];
			if (a[i][1] > m) m = a[i][1];
		}
		f[0][1][1] = 1; int h = 0;
		q1.push_back(0);
		q2.push_back(1);
		q3.push_back(1); 
		while (h < q1.size()) {
			int i = q1[h], j = q2[h], k = q3[h]; ++h;
			if (a[i][0] && (k == a[i][1])) {
				if (i + 1 == n) {ans = f[i][j][k]; break;}
				relax(i, 1, j, k, 1, 0);
			}
			if (!a[i][0] && (j == a[i][1])) {
				if (i + 1 == n) {ans = f[i][j][k]; break;}
				relax(i, 1, j, k, 0, 1);
			}
			relax(i, 0, j, k, 1, 1);
		}
		cout << "Case #" << te + 1 << ": " << ans << endl;
	}
	return 0;
}

