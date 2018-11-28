#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <algorithm>
using namespace std;

char num [128];

int main()
{
	int kase, serial = 0,
		len,
		pos, exg;
	char ch;

	scanf ("%d", &kase);
	while (kase--)
	{
		//	start a test case

		num [0] = '0';
		scanf ("%s", & (num [1]));

		len = strlen (num);

		pos = len-1;

		while (pos > 1 && num [pos-1] >= num [pos])
			--pos;
		--pos;

		exg = pos + 1;
		for (int i=exg; i < len; ++i) {
			if (num [i] > num [pos] && num [i] < num [exg]) {
				exg = i;
			}
		}

		ch = num [pos];
		num [pos] = num [exg];
		num [exg] = ch;

		sort (num + pos + 1, num + len);

		if (num [0] == '0')
			printf ("Case #%d: %s\n", ++serial, num+1);
		else
			printf ("Case #%d: %s\n", ++serial, num);

		//	end a test case
	}
	return 0;
}