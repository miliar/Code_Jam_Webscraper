#include <stdio.h>

const double a = 1.6180339887498948482045868343656;
const double b = 0.61803398874989484820458683436564;

int main(){
	int i,j;
	int T, testcase = 0;
	scanf("%d",&T);
	while(T-- > 0){
		int a1,b1,a2,b2;
		++testcase;
		long long ans = 0;
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		for(i=a1;i<=a2;i++){
			if(b2 < i*b){
				ans += b2-b1+1;
			}else if(b2 < i*a){
				if(b1 < i*b){
					ans += (int)(i*b)-b1+1;
				}
			}else{
				if(b1 > i*a){
					ans += b2-b1+1;
				}else if(b1 > i*b){
					ans += b2-(int)(i*a);
				}else{
					ans += b2-(int)(i*a) + (int)(i*b)-b1+1;
				}
			}
		}
		printf("Case #%d: %lld\n",testcase,ans);
	}
	return 0;
}
