#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm>
#include <string>
#include <map>

using namespace std;

long long  pd[610][610];
long long  c[610][610];
int n;
long long  MOD = 100003;

void read() {
	scanf("%d", &n);
}

long long  combinacao(int a, int b) {
	if (c[a][b] == -1) {
	    if (a >= b) {
			c[a][b] = (combinacao(a-1,b-1)+combinacao(a-1,b))%MOD;
		} else {
			c[a][b] = 0;
		}
	}
	
	return c[a][b];
}

long long  calc(int n, int pos) {
	if (pd[n][pos] == -1) {
		
		pd[n][pos] = 0;
		for (int i = 1; i < pos; i++) {
			if (pos-i-1 <= n-pos-1) {
				long long temp = calc(pos,i);
				long long comb = combinacao(n-pos-1, pos-i-1);
				temp = (temp*comb)%MOD;
				pd[n][pos] = (pd[n][pos]+temp)%MOD;
			}
		}
	}
	
	return pd[n][pos];
}

void process() {
	long long  tot = 0;
	
	for (int i = 1; i < n; i++) {
		long long  temp = calc(n,i);
		tot = (tot+temp)%MOD;
	}
	
	printf("%lld\n", tot);
}

int main() {
	
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	
	memset(pd, -1, sizeof(pd));
	memset(c, -1, sizeof(c));
	c[0][0] = 1;
	for (int i = 2; i <= 510; i++) {
		pd[i][1] = 1;
		c[i][0] = 1;
	}
	
	int casos;
	scanf("%d", &casos);
	
	for (int i = 1; i <= casos; i++) {
		printf("Case #%d: ", i);
		read();
		process();
	}
	
	return 0;
}

