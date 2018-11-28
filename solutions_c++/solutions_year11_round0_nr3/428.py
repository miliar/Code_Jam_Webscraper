#include <stdio.h>

int n;
int main(){
	int T;
	scanf("%d",&T);
	for(int testcase = 1; testcase <= T; testcase ++){
		scanf("%d",&n);
		int minv,sum = 0;
		int xsum = 0;
		for(int i = 0;i < n;i ++){
			int dat;
			scanf("%d",&dat);
			xsum ^= dat;
			if( i == 0){
				minv = dat;
			}else{
				if(minv > dat) minv = dat;
			}
			sum += dat;
		}
		if(xsum == 0){
			printf("Case #%d: %d\n",testcase,sum-minv);
		}else{
			printf("Case #%d: NO\n",testcase);
		}
	}
	return 0;
}

