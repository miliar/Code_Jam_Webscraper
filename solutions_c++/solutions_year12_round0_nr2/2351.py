#include <cstdio>

int main(){
	int ans, T, n, s, p, tmp;

	scanf("%d", &T);
	for (int t = 1; t <= T; t++){
		scanf("%d%d%d", &n, &s, &p);
		
		ans = 0;
		for (int i = 0; i < n; i++){
			scanf("%d", &tmp);
			if (tmp >= p * 3 - 2)
				ans++;
			else if (tmp >= p * 3 - 4 && p > 1 && s > 0)
				s--, ans++;
		}
		
		printf("Case #%d: %d\n", t, ans);
	}
}
