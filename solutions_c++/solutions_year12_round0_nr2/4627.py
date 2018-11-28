#include <stdio.h>

int max(int a, int b){
	if(a > b)
		return a;
	return b;
}

int main(){
	int T;
	scanf("%d", &T);
	for(int TT = 1; TT <= T; TT++){
		int n, s, p, x, ret=0;
		scanf("%d%d%d", &n, &s, &p);
		int l1 = max(0, p-1)*2+p;
		int l2 = max(0, p-2)*2+p;
		for(int i = 0; i < n; i++){
			scanf("%d", &x);
			if(x >= l1){
				ret++;
			}else if(x >= l2){
				if(s){
					s--;
					ret++;
				}
			}
		}
		printf("Case #%d: %d\n", TT, ret);
	}
	return 0;
}