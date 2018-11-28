#include <cstdio>

int main(){
	int T, c = 0;
	scanf("%d", &T);
	while (T--){
		int n;
		scanf("%d", &n);
		long long a0 = 2, a1 = 6, a2;
		for (int i=2; i<=n; i++){
			a2 = (6*a1-4*a0+1000)%1000;
			a0 = a1;
			a1 = a2;
		}
		a2 = (a2+1000)%1000-1;
		printf("Case #%d: ", ++c);
		if (a2 < 10) printf("00");
		else if (a2 < 100) printf("0");
		printf("%lld\n", a2);
	}
	return 0;
}
