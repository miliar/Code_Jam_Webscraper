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

char st[256];
char c[256][256];
bool d[256][256];
string s;

int main()
{
	freopen("B-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(8);

	int tcn;
	scanf("%d", &tcn);
	for (int tc = 1; tc <= tcn; tc++)
	{
		memset(c, 0, sizeof(c));
		memset(d, 0, sizeof(d));
		int nc, nd, n;

		cin >> nc;
		for (int i = 0; i < nc; i++)
		{
			cin >> s;
			c[(int)s[0]][(int)s[1]] = c[(int)s[1]][(int)s[0]] = s[2];
		}
		cin >> nd;
		for (int i = 0; i < nd; i++)
		{
			cin >> s;
			d[(int)s[0]][(int)s[1]] = d[(int)s[1]][(int)s[0]] = true;
		}

		cin >> n >> s;
		int top = 0;
		for (int i = 0; i < n; i++)
		{
			st[top++] = s[i];
			while (top > 1 && c[(int)st[top - 1]][(int)st[top - 2]])
			{
				top--;
				st[top - 1] = c[(int)st[top]][(int)st[top - 1]];
			}
			for (int j = 0; j < top - 1; j++)
			{
				if (d[(int)st[top - 1]][(int)st[j]])
				{
					top = 0;
					break;
				}
			}
		}
	
		printf("Case #%d: [", tc);
		for (int i = 0; i < top; i++)
		{
			if (i)
				cout << ", ";
			cout << st[i];
		}
		printf("]\n");
	}

	return 0;
}
