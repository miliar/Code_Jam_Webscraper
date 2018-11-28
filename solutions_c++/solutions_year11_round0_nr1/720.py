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

int main()
{
	freopen("A-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tcn;
	scanf("%d", &tcn);
	for (int tc = 1; tc <= tcn; tc++)
	{
		int to = 0, tb = 0, po = 1, pb = 1, t = 0, n, p;
		string r;
		cin >> n;
		for (int i = 0; i < n; i++)
		{
			cin >> r >> p;
			if (r == "O")
			{
				t += max(abs(p - po) - (t - to), 0) + 1;
				po = p;
				to = t;
			}
			else if (r == "B")
			{
				t += max(abs(p - pb) - (t - tb), 0) + 1;
				pb = p;
				tb = t;
			}
			else
			{
				cerr << "Wrong robot" << endl;
				return 0;
			}
		}
	
	
		printf("Case #%d: %d\n", tc, t);
	}

	return 0;
}
