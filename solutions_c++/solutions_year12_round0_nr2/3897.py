#include <stdio.h>

int main(){
	int n, s, p, T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++){
		scanf("%d%d%d", &n, &s, &p);
		int cnt=0;
		for(int i=0; i<n; i++){
			int total;
			scanf("%d", &total);
			if(total/3+(total%3>0) >= p){
				cnt++;
			}else if(total == 3*(p-1) && s > 0){
				if(p-1 > 0){
					cnt++;
					s--;
				}
			}else if(total == 3*(p-2)+2 && s > 0){
				cnt++;
				s--;
			}
		}
		printf("Case #%d: %d\n", t, cnt);
	}
	return 0;
}
