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

ld x[1024];
bool u[1024];
int a[1024];

void calc(int n)
{
	int a[n];
	bool u[n];
	for (int i = 0; i < n; i++)
		a[i] = i;

	int fact = 1;
	for (int i = 2; i <= n; i++)
		fact *= i;

	ld sum = 1.0;
	int bigs = 0;
	while (next_permutation(a, a + n))
	{
		memset(u, 0, sizeof(u));
		ld res = 0.0;
		for (int i = 0; i < n; i++)
		{
			if (u[i])
				continue;
			int k = 0, j = i;
			while (!u[j])
			{
				k++;
				u[j] = true;
				j = a[j];
			}
			if (k == n)
				bigs++;
			else
				res += x[k];
		}
		sum += res / fact;
	}
	x[n] = sum / (1.0 - ld(bigs) / fact);
}


int main()
{
	freopen("D-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(6);

	memset(x, 0, sizeof(x));
	for (int i = 2; i <= 1000; i++)
	{
//		calc(i);
		x[i] = i;
	}

	int tcn;
	cin >> tcn;
	for (int tc = 1; tc <= tcn; tc++)
	{
		int n;
		cin >> n;

		for (int i = 1; i <= n; i++)
			cin >> a[i];
		ld res = 0.0;
		memset(u, 0, sizeof(u));
		for (int i = 1; i <= n; i++)
		{
			if (u[i])
				continue;
			int k = 0, j = i;
			while (!u[j])
			{
				k++;
				u[j] = true;
				j = a[j];
			}
			res += x[k];
		}
	
		cout << "Case #" <<  tc << ": " << res << endl;
	}

	return 0;
}
