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
	cout << setiosflags(ios::fixed) << setprecision(8);

	int tcn;
	scanf("%d", &tcn);
	for (int tc = 1; tc <= tcn; tc++)
	{
		i64 n, pd, pg;
		string res = "Possible";
		cin >> n >> pd >> pg;

		i64 gcd = __gcd(pd, i64(100));

		if (100 / gcd > n || (pd && !pg) || (pd < 100 && pg == 100))
		{
			res = "Broken";
		}
	
		printf("Case #%d: %s\n", tc, res.c_str());
	}

	return 0;
}
