#include <cstdio>

int main(){
	int nT;
	scanf("%d", &nT);
	for (int test = 1, n, s, p, ans; test <= nT; test++){
		printf("Case #%d: ", test);
		scanf("%d %d %d", &n, &s, &p);
		ans = 0;
		for (int i = 0, v; i < n; i++){
			scanf("%d", &v);
			if (v % 3 == 1){
				if (v/3 + 1 >= p)
					ans++;
			} else if (v % 3 == 0){
				if (v/3 >= p){
					ans++;
				} else if (s){
					if (v && v/3 + 1 >= p){
						ans++;
						s--;
					}
				}
			} else {
				if (v/3 + 1 >= p){
					ans++;
				} else if (s) {
					if (v/3 + 2 >= p){
						ans++;
						s--;
					}
				}
			}
		}
		printf("%d\n", ans);
	}
	//while(1);
	return 0;
}
