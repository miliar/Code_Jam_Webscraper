/* A. Saving the Universe */

#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int getFirst (string, string [], int, int);
int strcm (string, string);

int main ()
{
	/**/FILE *input  = freopen ("A.in", "r", stdin);/**/
	/**/FILE *output = freopen ("A.txt", "w", stdout);/**/

	int cases, cases_r=0;

	scanf("%d", &cases);

	while (cases_r++<cases)
	{
		int eng, i, que, camb=0, got=0;

		scanf("%d", &eng);

		string e[eng];

		i=0;

		getchar();

		while (i<eng)
		{
			getline(cin, e[i]);
			i++;
		}
		scanf("%d", &que);

		string q[que];

		i=0;

		getchar();

		while (i<que)
		{
			getline(cin, q[i]);
			i++;
		}

		i=0;

		while (i<que && !got)
		{
			int k=0, min=0, best=0;

			while (k<eng && !got)
			{
				int cur = getFirst(e[k], q, i, que);

				if (cur>min)
				{
					min  = cur;
					best = k;
				}
				if (cur == -1)
					got = 1;
				k++;
			}
			if (!got)
			{
				i = min;
				camb++;
			}
		}

		printf("Case #%d: %d\n", cases_r, camb);
	}
	return 0;
}

int getFirst(string e, string q[], int min, int que)
{
	int found = 0;

	while (min<que && !found)
	{
		if (e == q[min])
			found = 1;
		else
			min++;
	}

	if (min==que)
		return -1;

	return min;
}
