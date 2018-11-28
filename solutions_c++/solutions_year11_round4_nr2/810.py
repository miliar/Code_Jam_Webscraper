#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

using namespace std;

const long double EPS = 1e-9;
const long double PI = 3.1415926535897932384626433832795;

typedef long double ld;
typedef long long i64;
typedef pair <int, int> PII;

int r, c, d;
string w[512];
int s[512][512];

bool check(int n)
{
//	cout << n << endl;
	for (int i = 0; i + n <= r; i++)
	{
		for (int j = 0; j + n <= c; j++)
		{
			ld x = 0, y = 0, ww = 0;
			for (int ii = 0; ii < n; ii++)
			for (int jj = 0; jj < n; jj++)
			{
				if ((ii == 0 || ii == n - 1) && (jj == 0 || jj == n - 1))
					continue;
				int we = w[i + ii][j + jj] - '0' + 1;
				ww += we;
				x += we * ii;
				y += we * jj;
			}
			x /= ww;
			y /= ww;

//			cout << i << " " << j << " " << x << " " << y << endl;
			if (abs(x - (n - 1) / 2.0) < EPS && abs(y - (n - 1) / 2.0) < EPS)
				return true;
		}
	}
	return false;
}

int main()
{
	freopen("B-small-attempt1.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(8);

	int tcn;
	scanf("%d", &tcn);
	for (int tc = 1; tc <= tcn; tc++)
	{
		cin >> r >> c >> d;
		for (int i = 0; i < r; i++)
			cin >> w[i];

		int res = 0;
		for (int i = min(r, c); i >= 3; i--)
		{
			if (check(i))
			{
				res = i;
				break;
			}
		}
	
	    if (res)
			printf("Case #%d: %d\n", tc, res);
		else
			printf("Case #%d: IMPOSSIBLE\n", tc);
	}

	return 0;
}
