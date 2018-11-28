#include<stdio.h>

int main(){
	int test, n;
	int ans, num;
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);

	scanf("%d", &test);
	for(int i=1; i<=test; i++){
		scanf("%d", &n);
		ans = 0;
		for(int j=1; j<=n; j++){
			scanf("%d", &num);
			if(num != j)
				ans ++;
		}
		printf("Case #%d: %.6lf\n", i, (double)ans);
	}
	return 0;
}
