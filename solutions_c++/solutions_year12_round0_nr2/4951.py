#include <stdio.h>

int t;
int n, s, p;
int res;
int curr;
int minn, mins;

int main(){
	scanf("%d", &t);
	for(int cases = 1; cases <= t; cases++){
		res = 0;
		scanf("%d%d%d", &n, &s, &p);
		minn = p * 3 - 2;
		if(minn < 0){
			minn = 0;
		}
		mins = p * 3 - 4;
		if(mins < 2){
			mins = 2;
		}
		for(int i = 1; i <= n; i++){
			scanf("%d", &curr);
			if(curr >= minn){
				res++;
			}else{
				if(curr >= mins && s > 0){
					s--;
					res++;
				}
			}
		}
		printf("Case #%d: %d\n", cases, res);
	}
	return 0;
}