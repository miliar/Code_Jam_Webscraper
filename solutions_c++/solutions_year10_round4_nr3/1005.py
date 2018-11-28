#include <iostream>

using namespace std;

const int MAX = 110;
int c;
int cur = 0;
int ans = 0;
//int m1[MAX][MAX];
//int m2[MAX][MAX];
bool f;
int r;
int x1, y1, x2, y2;
int n, m;

void func(int **m1, int **m2, int &cur)
{
	cur = 0;
	for (int i = 1; i < n; ++i)
		for (int j = 1; j < m; ++j)
			if (m1[i][j])
				if (!m1[i-1][j] && !m1[i][j-1])
					m2[i][j] = 0;
				else {
					m2[i][j] = 1;
					++cur;
				}
			else
				if (m1[i-1][j] && m1[i][j-1]) {
					m2[i][j] = 1;
					++cur;
				}
				else
					m2[i][j] = 0;
}

int main()
{
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);

	cin >> c;

	int **m1 = new int*[MAX];
	for (int i = 0; i < MAX; ++i)
		m1[i] = new int[MAX];
	int **m2 = new int*[MAX];
	for (int i = 0; i < MAX; ++i)
		m2[i] = new int[MAX];

	for (int ci = 0; ci < c; ++ci) {
		for (int i = 0; i < MAX; ++i)
			for (int j = 0; j < MAX; ++j) {
				m1[i][j] = m2[i][j] = 0;
			}
		cin >> r;
		f = 1;
		n = m = 0;
		ans = 0;
		for (int ni = 0; ni < r; ++ni) {
			cin >> x1 >> y1 >> x2 >> y2;
			n = max(n, x2);
			m = max(m, y2);
			for (int i = x1; i <= x2; ++i)
				for (int j = y1; j <= y2; ++j)
					m1[i][j] = 1;
		}
		cur = 0;
		++n; ++m;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				if (m1[i][j])
					++cur;
		while (cur) {
			if (f)
				func(m1, m2, cur);
			else
				func(m2, m1, cur);
			f = !f;
			++ans;
		}
		cout << "Case #" << ci+1 << ": " << ans << endl;
	}

	return 0;
}