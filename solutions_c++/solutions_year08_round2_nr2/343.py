#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <map>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <vector>
#include <queue>
#include <cassert>
#include <cmath>

using namespace std;

typedef long long ll;
typedef vector<int> vi;

typedef pair<int, int> pii;

#define all(s) s.begin(), s.end()

int gcd (int a, int b)
{
	return a == 0 ? b : gcd(b % a, a);
}

int main()
{
//#ifdef _DEBUG
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
//#endif

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test)
	{
		int a, b, pr;
		cin >> a >> b >> pr;
		int n = b - a + 1;
		int ans = n;
		
		vi p(n);
		for (int i = 0; i < n; ++i)
			p[i] = i;

		for (int i = a; i <= b; ++i)
			for (int j = i + 1; j <= b; ++j)
			{
				int num1 = i - a, num2 = j - a;
				while (num1 != p[num1]) num1 = p[num1];
				while (num2 != p[num2]) num2 = p[num2];
				if (num1 == num2) continue;

				int g = gcd(i, j);
				if (g < pr)
					continue;
				
				int best = 1;
				for (int k = 2; k * k <= g; ++k)
					while (g % k == 0)
						g /= k,
						best = max(best, k);

				best = max(best, g);

				if (best >= pr)
				{
					ans--;
					if (rand() & 1)
						p[num1] = num2;
					else
						p[num2] = num1;
				}
			}

		printf("Case #%d: %d\n", test, ans);
	}

}