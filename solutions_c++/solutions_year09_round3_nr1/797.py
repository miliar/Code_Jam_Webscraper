#include <stdio.h>
#include <string.h>

int T, t;
char s[100];
int minb;
int cnt[256];
int val[256];
int len;
int i;
int v;

int main() {
	scanf("%d", &T);
	for (t = 1; t<= T; t++) {
		scanf("%s", s);
  		
		for (i = 0; i < 256; i++){
			cnt[i] = 0;
			val[i] = -1;
		}

		len = strlen(s);
		for (i = 0; i < len; i++) {
          cnt[(int)s[i]] = 1;
		}

		minb = 0;
		for (i = 0; i < 256; i++)
			minb += cnt[i];

		//printf("%d\n", minb);
		if (minb == 1) minb = 2;

		val[s[0]] = 1; 
		v = 0;
		for (i = 1; i < len; i++) {
			if (val[s[i]] == -1) {				
				val[s[i]] = v; v++;
				if (v == 1) v++;
			}
		}
/*
		for (i = 0; i < len; i++)
			printf("%d", val[s[i]]);
		printf("\n");
*/
		long long int res = 0;
		for (i = 0; i < len; i++)
			res = res * minb + val[s[i]];

		printf("Case #%d: %I64d\n", t, res);
	}
	
	return 0;
}