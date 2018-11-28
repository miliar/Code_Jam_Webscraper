#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>

#define MAXN 110
int T, N, pos;
char color;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &T);
	for(int ri = 1; ri <= T; ++ri) {
		
		scanf("%d", &N);
		
		int ans, step, flag, i, j;
		i = j = flag = 1;
		step = ans = 0;

		for(int k = 1; k <= N; ++k) {
			scanf("\n%c%d", &color, &pos);
			if(flag == 1 && color == 'O') {
				ans += 1 + abs(i - pos);
				step += abs(i - pos) + 1;
			}
			if(flag == 0 && color == 'B') {
				ans += 1 + abs(j - pos);
				step += abs(j - pos) + 1;
			}
			if(flag == 0 && color == 'O') {
				if(step >= abs(i - pos)) {
					++ans;
					flag = step = 1;
				} else {
					step = abs(i - pos) - step;
					++step;
					ans += step;
					flag = 1;
				}
			}
			if(flag == 1 && color == 'B') {
				if(step >= abs(j - pos)) {
					++ans;
					step = 1;
				} else {
					step = abs(j - pos) - step;
					++step;
					ans += step;
				}
				flag = 0;
			}
			color == 'O' ? i = pos : j = pos;
		}
		printf("Case #%d: %d\n", ri, ans);
	}
	return 0;
}