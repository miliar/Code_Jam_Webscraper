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

int a[1 << 10];

int main()
{
	freopen("B-small-attempt1.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(8);

	int tcn, p, x;
	scanf("%d", &tcn);
	for (int tc = 1; tc <= tcn; tc++)
	{
		cin >> p;
		for (int i = 0; i < (1 << p); i++)
		{
			cin >> a[i];
			a[i] = p - a[i];
		}
		for (int i = 1; i < (1 << p); i++)
			cin >> x;

		int r = 0;
		for (int w = (1 << p); w > 1; w /= 2)
		{
			for (int i = 0; i < (1 << p); i += w)
			{
				int fl = 1;
				for (int j = 0; j < w; j++)
					if (a[i + j])
					{
						if (fl) r++;
						fl = 0;
						a[i + j]--;
					}
			}
		}

		printf("Case #%d: %d\n", tc, r);
	}

	return 0;
}
