/*
	2010-05-22 Google Code Jam Round 1A Question A
*/

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <math.h>

char line [128];
char map [128][128];

char row [128][128];
int rlength [128];

char codes[128];

#define validpos(r, c) (r >= 0 && r < n && c >= 0 && c < n)

//#define DEBUG 1
int main()
{
	codes ['R'] = 1;
	codes ['B'] = 2;

	int kase, serial=0,
		n, k, code;

	gets (line);
	kase = atoi (line);
	while (kase--)
	{
		// BEGIN test case

		memset (map, 0, sizeof (map));
		code = 0;

		gets (line);
		sscanf (line, "%d %d", &n, &k);

		for (int r=0, rlen; r<n; ++r) {
			gets (line);
			rlen = 0;
			for (char *ch=line; *ch != '\0'; ++ch) {
				if (*ch != '.') {
					row [r][rlen++] = toupper(*ch);
				}
			}
			rlength [r] = rlen;
		}

		// apply gravity
		for (int r=0, c, rlen; r<n; ++r) {
			c=n-1;
			rlen = rlength[r];
			while (rlen--) {
				map [c--][n-r-1] = row [r][rlen];
			}
		}

		// check
		char color;
		for (int r=0, c, d, cnt, rr, cc; r<n; ++r) {
			for (c=0; c<n; ++c) {
#ifdef DEBUG
				putchar (map[r][c] ? map[r][c] : '.');
#endif
				color = map[r][c];
				if (color == 0) continue;
				if (code & codes [color]) continue;

				// E
				rr=r; cc=c;
				for (d=1, cnt=1; d<k; ++d) {
					++cc;
					if (validpos(rr, cc) && map [rr][cc] == color)
						cnt++;
				}
				if (cnt == k) { code |= codes [color]; continue; }

				// SE
				rr=r; cc=c;
				for (d=1, cnt=1; d<k; ++d) {
					++rr; ++cc;
					if (validpos(rr, cc) && map [rr][cc] == color)
						cnt++;
				}
				if (cnt == k) { code |= codes [color]; continue; }

				// S
				rr=r; cc=c;
				for (d=1, cnt=1; d<k; ++d) {
					++rr;
					if (validpos(rr, cc) && map [rr][cc] == color)
						cnt++;
				}
				if (cnt == k) { code |= codes [color]; continue; }

				// SW
				rr=r; cc=c;
				for (d=1, cnt=1; d<k; ++d) {
					++rr; --cc;
					if (validpos(rr, cc) && map [rr][cc] == color)
						cnt++;
				}
				if (cnt == k) { code |= codes [color]; continue; }
			}
#ifdef DEBUG
				puts ("");
#endif
		}

		printf ("Case #%d: ", ++serial);
		if (code == 1) puts ("Red");
		else if (code == 2) puts ("Blue");
		else if (code == 3) puts ("Both");
		else puts ("Neither");
		// END test case
	}
	return 0;
}