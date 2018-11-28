#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <deque>
#include <vector>
#include <algorithm>
using namespace std;

int a[2000];
int b[2000];
int c[2000];
int r1, r2;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int TEST_NUMBER;
	cin >> TEST_NUMBER;

	for (int TEST = 1; TEST <= TEST_NUMBER; TEST++)
	{
		int n;
		memset(c, 0, sizeof c);
		
		r1 = 0;
		r2 = 0;
		
		cin >> n;
		for (int i = 0; i <= n; i++)
		{
			memset(a, 0, sizeof (a));

			int k = i;

			for (int j = 2; j <= i; j++)
				while (k%j == 0)
				{
					a[j]++;
					k /= j;
					if (a[j] > c[j])
						c[j] = a[j];
				}
		}

		
		for (int i = 0; i <= 1000; i++)
			if (c[i] > 0)
				r1++;

		r2 = 1;

		for (int i = 0; i <= 1000; i++)
			if (c[i] > 0)
				r2 += c[i];

		if (n == 1)
		{
			r2 = r1;
		}
		
		cout << "Case #" << TEST << ": " << r2-r1 << endl;
	}

	return 0;
}