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

bool a[512][512];
bool b[512][512];

int main()
{
	freopen("C-small-attempt0.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(8);

	int tcn, n, m;
	scanf("%d", &tcn);
	for (int tc = 1; tc <= tcn; tc++)
	{
		memset(a, 0, sizeof(a));
		cin >> n;
		while (n--)
		{
			int x1, x2, y1, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			for (int i = x1; i <= x2; i++)
				for (int j = y1; j <= y2; j++)
					a[i][j] = 1;
		}
		n = m = 0;
		for (int i = 0; i < 256; i++)
			for (int j = 0; j < 256; j++)
				if (a[i][j]) m++;

		while (m)
		{
			memset(b, 0, sizeof(b));
			for (int i = 1; i < 256; i++)
				for (int j = 1; j < 256; j++)
				{
					if (a[i][j])
						b[i][j] = (a[i - 1][j] || a[i][j - 1]);
					else
						b[i][j] = (a[i - 1][j] && a[i][j - 1]);
					if (a[i][j] && !b[i][j]) m--;
					if (!a[i][j] && b[i][j]) m++;
				}
			memcpy(a, b, sizeof(b));
			n++;
		}
	
		printf("Case #%d: %d\n", tc, n);
	}

	return 0;
}
