#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DP //printf("win: R %d B %d\n", wins[1], wins[2]);

int n, k;
//int leftx[64];
char a[64][64];
int ac[64];

inline int get(int y, int x) {
	if (y >= n || x >=n || x >= ac[y] || x < 0 || y < 0) return 0;
	return a[y][ac[y] - x - 1];
}

int main(int argc, char const* argv[])
{
	int tc;
	scanf("%d", &tc);
	for (int ti = 0; ti < tc; ti++) {
		scanf("%d%d", &n, &k);
		// memset(leftx, 127, sizeof(leftx[0]) * n);
		memset(ac, 0, sizeof(ac));
		for (int y = 0; y < n; y++) {
			for (int x = 0; x < n; x++) {
				char ch;
				scanf(" %c", &ch); //a[y][x]
				if (ch != '.') //ch = 0;
				{
					// not empty
					a[y][ac[y]++] = (ch == 'R'?1:2);
					//if (x < leftx[y]) leftx[y] = x; 
				}
			}
		}
		// check
		if(0)
		for (int y = 0; y < n; y++) {
			for (int v = 0; v < n ; v++) {
				char ch = get(y, v);
				if (ch == 0) ch = '.';
				putchar(ch);
			}
			puts("");
		}
		// scans
		bool wins[3] = {false, false, false};
		int kc[3] = {-1, 0, 0};
		int lastcolor;
		// for each y
		for (int y = 0; y < n; y++) {
			memset(kc, 0, sizeof(kc));
			lastcolor = get(y, 0);
			kc[lastcolor] ++;
			for (int x = 1; x <= ac[y]; x++) { // last 0 judge
				int color = get(y, x);
				if (color == lastcolor) {
					kc[color] ++;
				} else {
					// judge kc[lastcolor]
					if (kc[lastcolor] >= k) wins[lastcolor] = true;
					kc[lastcolor] = 0;
					kc[color] = 1;
					lastcolor = color;
				}
			}
		}
		DP;
		// for each x
		if (wins[1] && wins[2]) goto end;
		for (int x = 0; x < n; x++) { // last 0 judge
			memset(kc, 0, sizeof(kc));
			lastcolor = get(0, x);
			kc[lastcolor] ++;
			for (int y = 1; y <= n; y++) {
				int color = get(y, x);
				if (color == lastcolor) {
					kc[color] ++;
				} else {
					// judge kc[lastcolor]
					if (kc[lastcolor] >= k) wins[lastcolor] = true;
					kc[lastcolor] = 0;
					kc[color] = 1;
					lastcolor = color;
				}
			}
		}
		DP;
		// for /
		if (wins[1] && wins[2]) goto end;
		for (int d = 1-n; d < n; d++) { 
			int x = 0, y;
			if (d > 0) {
				x = d;
				y = 0;
			} else {
				y = -d;
				x = 0;
			}
			memset(kc, 0, sizeof(kc));
			lastcolor = get(y, x);
			kc[lastcolor] ++;
			for (y++, x++; y <= n && x <= n; y++, x++) {
				int color = get(y, x);
				if (color == lastcolor) {
					kc[color] ++;
				} else {
					// judge kc[lastcolor]
					if (kc[lastcolor] >= k) wins[lastcolor] = true;
					kc[lastcolor] = 0;
					kc[color] = 1;
					lastcolor = color;
				}
			}
		}
		DP;
		// for \ ...
		if (wins[1] && wins[2]) goto end;
		for (int d = 1-n; d < n; d++) { 
			int x = 0, y;
			if (d > 0) {
				x = d;
				y = 0;
			} else {
				y = -d;
				x = n - 1;
			}
			memset(kc, 0, sizeof(kc));
			lastcolor = get(y, x);
			kc[lastcolor] ++;
			for (y++, x--; y <= n && x >= -1; y++, x--) {
				int color = get(y, x);
				if (color == lastcolor) {
					kc[color] ++;
				} else {
					// judge kc[lastcolor]
					if (kc[lastcolor] >= k) wins[lastcolor] = true;
					kc[lastcolor] = 0;
					kc[color] = 1;
					lastcolor = color;
				}
			}
		}
		DP;
end:
		printf("Case #%d: ", ti + 1);
		if (wins[1] && wins[2]) puts("Both");
		else if (wins[1] && !wins[2]) puts("Red");
		else if (!wins[1] && !wins[2]) puts("Neither");
		else if (!wins[1] && wins[2]) puts("Blue");
	}
	return 0;
}
