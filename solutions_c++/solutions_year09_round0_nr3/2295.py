#include <cstdio>
#include <cstring>

#define SZ 19
#define MOD 10000

// TODO: usar MOD

int n, len, t[512][SZ];
char line[512];
char match[] = "welcome to code jam";

int main(void) {
	int i, j;
	fgets(line, sizeof(line), stdin);
	sscanf(line, "%d", &n);
	for(int c = 1; c <= n; c++) {
		fgets(line, sizeof(line), stdin);
		len = strlen(line) - 1;
		for(i = 0; i <= len; i++)
			for(j = 0; j <= SZ; j++)
				t[i][j] = 0;
		for(i = len-1; i >= 0; i--) {
			t[i][SZ-1] = t[i+1][SZ-1];
			if(line[i] == match[SZ-1]) t[i][SZ-1]++;
			t[i][SZ-1] %= MOD;
		}
		for(j = SZ-2; j >= 0; j--)
			for(i = len-1; i >= 0; i--)
				if(line[i] == match[j])
					t[i][j] = (t[i+1][j+1] + t[i+1][j]) % MOD;
				else
					t[i][j] = t[i+1][j];
		printf("Case #%d: %04d\n", c, t[0][0]%MOD);
	}

	return 0;
}
