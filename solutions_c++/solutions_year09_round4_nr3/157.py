#include <vector>
#include <string>
#include <iostream>
using namespace std;
template <class T> void out(T A[], int n) {for (int i = 0; i<n; i++) cout << A[i] << ' '; cout << endl;}  

const int mx = 120;
int ts, no;
int n, g[mx][mx], a[mx][30], k, ans;
int p[mx], b[mx];

int path(int u)
{
	for (int i=0; i<n; i++)
	{
		if (g[u][i] && !b[i])
		{
			b[i] = 1;
//			cout << u << ' ' << i << ' ' << p[i] << endl;
			if (p[i] == -1 || path(p[i]))
			{
				p[i] = u;
				return 1;
			}
		}
	}
	return 0;
}

main() {
	freopen("c1.in", "r", stdin);
	freopen("3.out", "w", stdout);

	cin >> ts;
	for (int no=0; no<ts; no++) {
		cout << "Case #" << no+1 << ": ";
		cin >> n >> k;
		for (int i=0; i<n; i++)
		{
			for (int j=0; j<k; j++)
			{
				cin >> a[i][j];
			}
		}
		memset(g, 0, sizeof(g));
		for (int i=0; i<n; i++)
		{
			p[i] = -1;
		}
		for (int i=0; i<n; i++)
		{
			for (int j=0; j<n; j++)
			{
				int ok = 1;
				for (int kk=0; kk<k; kk++)
				{
					if (a[i][kk] >= a[j][kk])
					{
						ok = 0; break;
					}
				}
				if (ok)
				{
					g[i][j] = 1;
				}
			}
		}
/*		for (int i=0; i<n; i++)
		{
			out(g[i], n);
		}*/
		int ans = 0;
		for (int i=0; i<n; i++)
		{
			memset(b, 0, sizeof(b));
			if (path(i))
			{
				ans ++;
//				cout << i << endl;
			}
		}
		cout << n-ans << endl;
	}
}
