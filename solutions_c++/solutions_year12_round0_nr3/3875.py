#include <cstdio>
#include <cstring>

int bb[10];
int A, B, ans, bit;
int b[2100000];

void dfs(int cur, int s) {
	if (s > B) return;
	if (cur == 0) {
		if (s >= A) {
			for (int ss = s, i = 1; i < bit; ++i) {
				ss = (ss % 10) * bb[bit] + ss / 10;
				if (ss <= B && ss > s && b[ss] != s) {
					++ans;
					b[ss] = s;
					//if (s == ss) puts("no");
				}
			}
		}
		return;
	}
	for (int i = (cur == bit ? 1 : 0); i <= 9; ++i)
		dfs(cur - 1, s + i * bb[cur]);
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	bb[1] = 1;
	for (int i = 2; i <= 8; ++i)
		bb[i] = bb[i - 1] * 10;
	int T;
	scanf("%d", &T);
	for (int cs = 1; cs <= T; ++cs) {
		memset(b, 0, sizeof(b));
		scanf("%d%d", &A, &B);
		ans = 0;
		bit = 0;
		for (int aa = A; aa > 0; aa /= 10, ++bit);
		dfs(bit, 0);
		printf("Case #%d: %d\n", cs, ans);
	}
	
	return 0;
}
