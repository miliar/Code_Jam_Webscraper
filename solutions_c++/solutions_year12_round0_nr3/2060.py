#include <stdio.h>
int use[2000010];
int main(){
	int c, a, b;
	scanf("%d", &c);
	for(int i=1;i<=c;++i){
		scanf("%d%d", &a, &b);
		int cnt = 0;
		for(int j=a;j<=b;++j){
			int now = j, go = j, nxt = j, digit = 1;
			while(now/10 > 0){
				now /= 10;
				digit *= 10;
			}
			while(true){
				int first = nxt/digit;
				nxt = nxt*10 + first;
				nxt = nxt%(digit*10);
				if(go == nxt) break;
				if(go < nxt){
					if(go >= a && nxt <= b){
						++cnt;
					}
				}
			}
		}
		printf("Case #%d: %d\n", i, cnt);
	}
	return 0;
}
