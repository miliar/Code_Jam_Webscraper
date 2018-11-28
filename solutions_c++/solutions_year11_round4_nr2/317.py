#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


int r, c;
long long a[511][511];
long long b[511][511];
long long st[511][511];
long long mm[511][511];
long long d;


void Load()
{
	cin >> r >> c >> d;
	int i, j;
	for (i = 1; i <= r; i++) {
		scanf("\n");
		for (j = 1; j <= c; j++) {
			char h;
			scanf("%c", &h);
			a[i][j] = 2*i*(d + (int)h - (int)'0');
			b[i][j] = 2*j*(d + (int)h - (int)'0');
			st[i][j] = (d + (int)h - (int)'0');
			mm[i][j] = (d + (int)h - (int)'0');
		}
	}
}

void Solve()
{
	int i, j;
	for (i = 1; i <= r; i++) {
		for (j = 1; j <= c; j++) {
			a[i][j] += a[i-1][j];
			b[i][j] += b[i-1][j];
			mm[i][j] += mm[i-1][j];
		}
	}
	for (i = 1; i <= r; i++) {
		for (j = 1; j <= c; j++) {
			a[i][j] += a[i][j-1];
			b[i][j] += b[i][j-1];
			mm[i][j] += mm[i][j-1];
		}
	}
	int k;
	int maxk = 0;

	for (k = 3; k <= min(r,c); k++) {
		for (i = 1; i + k - 1 <= r; i++) {
			for (j = 1; j + k - 1 <= c; j++) {
            	long long sx, sy, sm;
				if (k == 5 && i == 1 && j == 1)
						i = j;
            	sx = a[i+k-1][j+k-1] - a[i+k-1][j-1] - a[i-1][j+k-1] + a[i-1][j-1] - 2*i*(st[i][j] + st[i][j+k-1]) - 2*(i+k-1)*(st[i+k-1][j] + st[i+k-1][j+k-1]);
            	sy = b[i+k-1][j+k-1] - b[i+k-1][j-1] - b[i-1][j+k-1] + b[i-1][j-1] - 2*j*(st[i][j] + st[i+k-1][j]) - 2*(j+k-1)*(st[i][j+k-1] + st[i+k-1][j+k-1]);
				sm = mm[i+k-1][j+k-1] - mm[i+k-1][j-1] - mm[i-1][j+k-1] + mm[i-1][j-1] - (st[i][j] + st[i+k-1][j]) - (st[i][j+k-1] + st[i+k-1][j+k-1]);
            	if (sx == (2*i+k-1)*sm && sy == (2*j+k-1)*sm)
            		if (maxk < k) maxk = k;


/*				long long ssx = 0, ssy = 0, ssm = 0;
				int ii, jj;
				for (ii = i; ii < i + k; ii++ )
					for (jj = j; jj < j + k; jj++ )
					{
						if ((ii == i || ii == i+k-1) && (jj == j || jj == j+k-1)) continue;
						ssx += 2*ii*st[ii][jj];
						ssy += 2*jj*st[ii][jj];
						ssm += st[ii][jj];
					}
					if (sx != ssx || sy != ssy || sm != ssm) {
						cerr << "botva\n";
					}
*/
			}

		}

	}
	if (maxk == 0) cout << "IMPOSSIBLE\n";
	else cout << maxk << "\n";
}

int main()
{
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cout << "Case #" << tt << ": ";
		Solve();
	}
	return 0;
}
