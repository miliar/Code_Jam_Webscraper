#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void use_file(const char *prefix)
{
	char filename[64];

	if ( NULL == prefix || '\0' == prefix[0] ) return;

	sprintf(filename, "%s.in", prefix);
	freopen(filename, "r", stdin);

	sprintf(filename, "%s.out", prefix);
	freopen(filename, "w", stdout);
}

unsigned int f[2000000];

int main()
{
	int T, kase;
	unsigned int n, a[21], i, j, k, sum, sa, sb;

	use_file("C-small-attempt0");
	scanf("%d", &T);
	for ( kase = 1; kase <= T; kase++ ) {
		scanf("%u", &n);
		for ( i = 0; i < n; i++ ) scanf("%u", &a[i]);
		printf("Case #%d:\n", kase);
		memset(f, 0, sizeof(f));
		for ( i = 1; i < (1<<n); i++ ) {
			j = i; k = 0; sum = 0;
			while ( j ) {
				if ( j&1 ) sum += a[k];
				j >>= 1;
				k++;
			}
			if ( f[sum] ) {
				sa = f[sum]&(f[sum]^i);
				sb = i & (f[sum]^i);
				k = 0;
				while ( sa ) {
					if ( sa&1 ) printf("%u ", a[k]);
					sa >>= 1;
					k++;
				}
				printf("\n");
				k = 0;
				while ( sb ) {
					if ( sb&1 ) printf("%u ", a[k]);
					sb >>= 1;
					k++;
				}
				printf("\n");
				break;
			}
			f[sum] = i;
		}		
	}
	if ( i == (1<<n) ) printf("Impossible\n");

	fprintf(stderr, "Done.\n");
	while(1);

	return 0;
}
