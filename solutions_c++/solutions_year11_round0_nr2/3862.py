#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <iostream>
using namespace std;

char s[14],com[4], opp[4];
char res[14];
int ll;

int main() {
	freopen("B-small-attempt7.in", "r", stdin);
	freopen("B-out_f.txt", "w", stdout);

	int t, i, j, c, d, n, len;
	scanf ("%d", &t);

	for (int ii = 1; ii <= t; ++ii) {
		ll = -1;
		
		scanf ("%d", &c);
		if (c) scanf ("%s", com);
		scanf ("%d", &d);
		if (d) scanf ("%s", opp);
		scanf ("%d", &n);
		scanf ("%s", s);
		
		len = strlen(s);
		res[++ll] = s[0];
		bool _flag;
		
		for (i = 1; i < len; ++i) {
			_flag = true;

			if (c == 1 && (res[ll] == com[0] && s[i] == com[1] ||
				res[ll] == com[1] && s[i] == com[0])) {
				res[ll] = com[2];
				_flag = false;
			}

		    if (_flag == true && d == 1 && s[i] == opp[1]) {
				_flag = false;
				bool flag = true;
				for (j = 0; j <= ll; ++j) {
					if (res[j] == opp[0]) {
						ll = -1;
						flag = false;
						break;
					}
				}
				if (flag)
					res[++ll] = s[i];
			}

			if (_flag == true && d == 1 && s[i] == opp[0]) {
				_flag = false;
				bool flag = true;
				for (j = 0; j <= ll; ++j) {
					if (res[j] == opp[1]) {
						ll = -1;
						flag = false;
						break;
					}
				}
				if (flag)
					res[++ll] = s[i];
			}

			if (_flag == true) {
				res[++ll] = s[i];
			}
		}
		printf("Case #%d: [", ii);
		for (i = 0; i <= ll; ++i) {
			printf("%c", res[i]);
			if (i != ll)	printf(", ");
		}
		printf("]\n");
	}
	return 0;
}