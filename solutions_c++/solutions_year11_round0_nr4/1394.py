#include<cstdio>

int main(){
	int t;
	scanf("%d", &t);
	for(int j = 1; j <= t; j++){
		int n;
		scanf("%d", &n);
		int wyn = 0;
		int a;
		for(int i = 1; i <= n; i++){
			scanf("%d", &a);
			if(i!=a)
				wyn++;
		}
		printf("Case #%d: %d.000000\n", j, wyn);
	}
	return 0;
}
