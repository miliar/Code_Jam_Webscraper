#include <stdio.h>

int cs, ct;
int n, time, ta, tb;
char r[110][10];
int p[110];
int a[110], b[110];

int main()
{
	int i, x, y, po, pb;
	scanf("%d", &ct);
	for (cs = 1; cs <= ct; cs++) {
		scanf("%d", &n);
		ta = tb = 0;
		for (i = 0; i < n; i++) {
			scanf("%s%d", r[i], &p[i]);
			if (r[i][0] == 'O') a[ta++] = p[i];
			if (r[i][0] == 'B') b[tb++] = p[i];
		}
		po = pb = 1;
		x = y = 0;
		time = 0;
		for (i = 0; i < n;) {
			time++;
			int bj = 0;
			if (r[i][0] == 'O' && a[x] == po) {
				i++;
				x++;
				bj = 1;
			} else 
			if (po != a[x]) {
				if (po > a[x]) po--;
				else po++;
			}

			if (!bj && r[i][0] == 'B' && b[y] == pb) {
				i++;
				y++;
			} else
			if (pb != b[y]) {
				if (pb > b[y]) pb--;
				else pb++;
			}
		}
		printf("Case #%d: %d\n", cs, time);
	}	
	return 0;
}
