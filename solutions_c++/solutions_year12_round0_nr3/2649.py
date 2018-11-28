#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <cassert>
#include <map>
#include <string.h>
#include <ctime>
#include <iostream>

using namespace std;

const char* FILE_NAME_IN = "input.txt";
const char* FILE_NAME_OUT = "output.txt";

const int size = 10 *  1000 * 1000 + 5;
const int inf = 1000 * 1000 * 1000 + 5;
double const eps = 1e-8;

int pow10[9] = {1, 10, 100, 1000, 10 * 1000, 100 * 1000, 1000 * 1000, 10 * 1000 * 1000, 100 * 1000 * 1000};

bool used[size];

int main ()
{
	freopen(FILE_NAME_IN, "r", stdin);
	freopen(FILE_NAME_OUT, "w", stdout);

	int a, b, i, it, t, oldi, ans, j, k, c;

	scanf("%d", &t);
	
	for (it = 0; it < t; it++)
	{
		printf("Case #%d: ", it + 1);
		ans = 0;
		scanf("%d %d", &a, &b);
		for (i = a; i <= b; i++)
		{
			for (k = 0; k < 9; k++)
				if (pow10[k] > i)
					break;
			oldi = i;
			for (j = 0; j < k; j++)
			{
				c = i % 10;
				i /= 10;
				i += pow10[k - 1] * c;
				if (i > oldi && i <= b && !used[i])
				{
					used[i] = true;
					ans++;
				}
			}
			for (j = 0; j < k; j++)
			{
				c = i % 10;
				i /= 10;
				i += pow10[k - 1] * c;
				used[i] = false;
			}
			i = oldi;
		}
		printf("%d\n", ans);
	}
	
	return 0;
}