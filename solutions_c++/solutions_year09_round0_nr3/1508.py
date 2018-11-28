#include <cstdio>
#include <cstring>

const int N = 509;
const int DS = 29;
const int MOD = 10000;

char dest[] = "welcome to code jam";
int ds = 19;
int n;
char s[N];
int memo[N][DS];

int f(int pos, int curr){
	int pre = 0;
	if (curr == ds) pre++;

	if (pos == n) return pre;

	if (curr == ds) return 1;

	if (memo[pos][curr] != -1) return memo[pos][curr];

	if (curr < ds && s[pos] == dest[curr]) pre = (pre % MOD + f(pos + 1, curr + 1) % MOD) % MOD;

	return memo[pos][curr] = (pre % MOD + f(pos + 1, curr) % MOD) % MOD;
}

int main(){
	int tests;
	scanf("%d ", &tests);

	for (int t = 0; t < tests; t++){
		gets(s);
		n = strlen(s);

		//printf("%d: %s\n", n, s);

		memset(memo, -1, sizeof(memo));

		int ans = f(0, 0), tmp = ans;

		int d = 0;

		while (tmp > 0){
			tmp /= 10;
			d++;
		}

		d = 4 - d; if (d == 4) d--;

		printf("Case #%d: ", t + 1);

		while (d--) printf("0");

		printf("%d\n", ans);
	}

	return 0;
}
