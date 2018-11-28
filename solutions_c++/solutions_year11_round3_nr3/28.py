#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <bitset>

using namespace std;

const int NMAX = 1000 * 1000;
const long long INF = 10000000000000000LL + 1, MAX = 1000000000000000000LL;
long long d[NMAX], a[NMAX];
int dSize;

void CalcDiv(long long m)
{
	dSize = 0;
	for (long long i = 1; i * i <= m; ++i)
	{
		if (m % i)
			continue;
		d[dSize++] = i;
		d[dSize++] = m / i;
	}

	sort(d, d + dSize);
}

long long GetMinDiv(int n, long long l, long long h)
{
	for (int i = 0; i < dSize; ++i)
	{
		bool cont = true;
		for (int j = 0; j < n && cont; ++j)
		{
			if ((a[j] % d[i]) && (d[i] % a[j]))
				cont = false;
		}
		
		if (cont && d[i] >= l && d[i] <= h)
			return d[i];
	}

	return INF;
}

long long GCD(long long a, long long b)
{
	return (b ? GCD(b, a % b) : a);
}

long long GetLCM(int n)
{
	long long res = a[0];
	for (int i = 1; i < n; ++i)
	{
		long long gcd = GCD(res, a[i]);
		res = res / gcd;
		if (MAX / res < a[i])
			return INF;
		res = res * a[i];
	}

	return res;
}

bool Check(long long nmb, long long l, long long h)
{
	return (nmb >= l) && (nmb <= h);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int cntTest;
	cin >> cntTest;

	for (int test = 0; test < cntTest; ++test)
	{
		int n;
		long long l, h;

		cin >> n >> l >> h;
		for (int i = 0; i < n; ++i)
			scanf("%lld", &a[i]);		

		if (l == 1)
		{
			cout << "Case #" << test + 1 << ": 1" << endl;
			continue;
		}

		long long mx = a[0];
		for (int i = 1; i < n; ++i)
			mx = max(mx, a[i]);

		CalcDiv(mx);

		long long res = GetMinDiv(n, l, h);
		long long lcm = GetLCM(n);

		lcm = ((lcm + l - 1) / lcm) * lcm;

		if (!Check(lcm, l, h) && !Check(res, l, h))
		{
			cout << "Case #" << test + 1 << ": NO" << endl;
			continue;
		}

		if (!Check(lcm, l, h))
		{
			cout << "Case #" << test + 1 << ": " << res << endl;
			continue;
		}

		if (!Check(res, l, h))
		{
			cout << "Case #" << test + 1 << ": " << lcm << endl;
			continue;
		}

		cout << "Case #" << test + 1 << ": " << min(lcm, res) << endl;


		


		

		//int res = -1;
		//for (int d = l; d <= h; ++d)
		//{
		//	bool isDiv = true;
		//	for (int i = 0; i < n && isDiv; ++i)
		//		if ((a[i] % d) && (d % a[i]))
		//			isDiv = false;

		//	if (isDiv)
		//	{
		//		res = d;
		//		break;
		//	}
		//}

		/*
		if (res > 0)
			cout << res << endl;
		else
			cout << "NO" << endl;*/
	}

	return 0;
}