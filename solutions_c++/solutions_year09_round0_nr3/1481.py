#include <cstdlib>
#include <cstdio>
#include <cstring>

#define MAXL 510
#define LENGTH 19

char find[] = "welcome to code jam";
char buf[MAXL+1];
int count[MAXL+1][LENGTH+1];

void solve(int nr) {
	fgets(buf, MAXL+1, stdin);
	int l = strlen(buf);
	for(int i = 0; i <= l; i++)
		for(int j = 0; j <= LENGTH; j++)
			count[i][j] = 0;
	count[l][LENGTH] = 1;
	
	for(int i = LENGTH-1; i >= 0; i--) {
		for(int j = 0; j < l; j++) {
			if(buf[j] == find[i])
				for(int k = j+1; k <= l; k++)
					if(buf[k] == find[i+1]) {
						count[j][i] += count[k][i+1];
						count[j][i] %= 10000;
					}
		}
	}
	
	// last step
	int ret = 0;
	for(int i = 0; i < l; i++)
		if(buf[i] == find[0])
			ret += count[i][0];
	
	printf("Case #%d: %04d\n", nr, ret % 10000);
}

int main() {
	int n;
	scanf("%d\n", &n);
	for(int i = 1; i <= n; i++) {
		solve(i);
	}
}