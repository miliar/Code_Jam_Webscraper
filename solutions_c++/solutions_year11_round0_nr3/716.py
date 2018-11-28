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
	freopen("C-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tcn;
	scanf("%d", &tcn);
	for (int tc = 1; tc <= tcn; tc++)
	{
		int n, x, sum = 0, xorsum = 0, mi = 1000000000;
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
		{
			scanf("%d", &x);
			xorsum ^= x;
			sum += x;
			mi = min(mi, x);
		}
	
		printf("Case #%d: ", tc);
		if (xorsum)
			cout << "NO" << endl;
		else
			cout << sum - mi << endl;
	}

	return 0;
}
