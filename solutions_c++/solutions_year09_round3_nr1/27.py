#include <stdio.h>
#include <memory.h>
#define Bint long long
char str[64], d[64];
Bint r;
Bint process()
{
	int i, j, k;

	memset(d,0,sizeof(d));
	for (i = 0; str[i]; i++) {
		for (j = 0; j < 64; j++) {
			if (d[j] == str[i]) break;
		}
		if (j < 64) continue;
		for (j = i==0; j < 64; j++) {
			if (!d[j]) {
				d[j] = str[i];
				break;
			}
		}
	}
	for (k = 63; k >= 0; k--) {
		if (d[k]) break;
	}
	++k; r = 0;
	for (i = 0; str[i]; i++) {
		for (j = 0; j < k; j++) {
			if (d[j] == str[i]) break;
		}
		r = r*k+j;
	}
	return r;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t, T;
	
	scanf("%d",&T);
	for (t = 1; t <= T; t++) {
		scanf("%s",str);
		printf("Case #%d: %lld\n", t, process());
	}
	return 0;
}