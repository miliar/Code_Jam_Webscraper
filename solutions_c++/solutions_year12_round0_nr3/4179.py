#include <vector>
#include <list>
#include <algorithm>
#include <cmath>
#include <functional>
#include <cstdlib>
#include <iostream>

using namespace std;

int numLen(int n)
{
	int len = 1;
	for (; n /= 10; len++)
		;
	return len;
}

int rotate (int n, int l = 1)
{
	return (n % (int)pow(10.0, l)) * pow(10.0, numLen(n)-l) + n / (int)pow(10.0, l);
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int cases, A, B, r, y;
	scanf_s("%d", &cases);

	for (int i = 1; i <= cases; i++)
	{
		scanf_s("%d %d", &A, &B);
		y = 0;

		for (int j = A; j <= B; j++)
		{
			if (j < 10)
				continue;

			r = j;
			for (int l = 0; l < numLen(j); l++)
			{
				if (r % 10 == 0)
				{
					r = rotate(r, 2);
					l++;
				}
				else
				{
					r = rotate(r, 1);
				}

				if (j < r && r <= B)
				{
					y++;
					//printf ("%d %d\n", j, r);
				}
			}
		}

		cout << "Case #" << i << ": " << y << endl;
	}

	return 0;
}