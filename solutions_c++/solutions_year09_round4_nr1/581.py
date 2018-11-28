//	!

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

#include <algorithm>
using namespace std;

char line [100];

int pos [50];
char map [50][50];

int main()
{
	gets (line);
	int kase = atoi (line), serial = 0;
	int n, soln;
	bool swapped;

	while (kase--)
	{
		gets (line);
		n = atoi (line);
		for (int r=0, c; r<n; ++r) {
			gets (line);
			for (c=n-1; c>=0; --c)
				if (line [c] == '1')
					break;
			pos [r] = c;
		}

		soln = 0;
		do
		{
			swapped = false;
			for (int i=0; i<n; ++i) {
				if (pos [i] > i) {

					int k=i;
					while (pos [k] > i) ++k;

					for (; k>i; --k) {
						swap (pos [k], pos [k-1]);
						++soln;
					}

					swapped = true;
					break;
				}
			}
		}
		while (swapped);
		printf ("Case #%d: %d\n", ++serial, soln);
	}
	return 0;
}