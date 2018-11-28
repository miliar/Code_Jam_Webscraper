
#include <cstdio>

int main(){
	

	int t; scanf("%d", &t);

	for(int x=1; x<=t; ++x){
		int n; scanf("%d", &n);
		int sum = 0;
		int min = 2147483647;
		int all = 0;
		int tmp;
		for(int i=0; i<n; ++i){
			scanf("%d", &tmp);
			sum ^= tmp;
			all += tmp;
			if(tmp < min){
				min = tmp;
			}
		}
		if(sum != 0){
			printf("Case #%d: NO\n", x);
		}else{
			printf("Case #%d: %d\n", x, all-min);
		}
	}
	return 0;
}
