#include <stdio.h>
#include <string.h>

#define m0 510
#define mod 10000

char t[] = "-welcome to code jam";
char s[m0];
int f[m0][m0];

int calc(){
	int lt = (int)strlen(t); lt--;
	int ls = (int)strlen(s); ls--;
	int i, j;

	memset(f, 0, sizeof(f));
	for (i = 0; i <= ls; i++){
		f[i][0] = 1;
	}

	for (i = 1; i <= ls; i++){
		for (j = 1; j <= lt; j++){
			if (i == 3 && j == 2){
				int sss = 1;
			}


			f[i][j] = f[i - 1][j];
			if (s[i] == t[j] && f[i - 1][j - 1] > 0) f[i][j] += f[i - 1][j - 1];

			f[i][j] %= mod;
		}
	}

	return(f[ls][lt]);
}

int main(){
	freopen("C-large.in", "r", stdin);
	freopen("C.out", "w", stdout);

	int i, T;

	scanf("%d\n", &T);

	for (i = 1; i <= T; i++){
		gets(s + 1);
		s[0] = '-';
		printf("Case #%d: %04d\n", i, calc());
	}

	return 0;
}