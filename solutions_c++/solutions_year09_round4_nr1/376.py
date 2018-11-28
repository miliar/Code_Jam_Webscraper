#include <stdio.h>
#include <string.h>
char s[100][100];
int pos[100];
int abs(int x) {
	return x>0?x:-x;
}
int main() {
	int ca, i, j, k, t, n;
	int cases = 0, tot;
	scanf("%d", &ca);
	while (ca--) {
		scanf("%d", &n);
		for (i=0;i<n;++i) {
			scanf("%s", s[i]);			
			pos[i] = i;
		}
		tot = 0;
		for (i=0;i<n;++i) {
			int minn = 0x3fffff;
			for (j=0;j<n;++j) {
				if (pos[j] == -1) continue;
				for (k=i+1;k<n;++k) {
					if (s[j][k] == '1') break;
				}
				if (k<n) continue;
				if (abs(pos[j] - i) < minn) {
					minn = abs(pos[j]- i);
					t = j;
				}
			}
			tot += minn;
			for (j=0;j<n;++j) if (pos[j] != -1 && pos[j] < pos[t]) ++pos[j];
			pos[t] = -1;			
		}
		printf("Case #%d: %d\n", ++cases, tot);
	}
	return 0;
}
