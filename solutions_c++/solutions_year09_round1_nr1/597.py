#include <stdio.h>
#include <string.h>
#include <algorithm>
char s[1000];


int used[100000];
int a[100];
int base[10], n;

int check(int x) {
	int i;
	for (i=0;i<n;++i) {
		int t = x;
		int tot;
		memset(used, 0, sizeof(used));
		do{
			if (t<100000) used[t] = 1;
			tot = 0;
			while (t) {
				tot += (t%base[i])*(t%base[i]);
				t/=base[i];
			}
			t = tot;			
		} while (!used[t]);
		if (t != 1) {
			//printf("%d fail at %d\m", x, base[i]);
			return false;
		}
	}
	return true;
}
int main() {
	int ca;
	int pos, delta;
	int i, cases = 0;
	scanf("%d\n", &ca);
	while (ca--) {
		gets(s);
		pos = delta = 0;
		memset(a, 0, sizeof(a));
		while (sscanf(s+pos, "%d%n", &i, &delta)!=EOF) {
			a[i] = 1;
			pos += delta;
		}
		n=0;
		for (i=0;i<=10;++i) {
			if (a[i]) {
				base[n++] = i;
			}
		}
		for (i=2;!check(i);++i);
		printf("Case #%d: %d\n", ++cases, i);
	}
	return 0;
}