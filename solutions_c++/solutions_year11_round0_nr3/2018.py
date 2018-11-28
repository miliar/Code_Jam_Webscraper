#include<stdio.h>
#include<stdlib.h>
int main(){
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++){
		int N ; 
		scanf("%d",&N);
		int sum = 0;
		int xsum = 0;
		int _min = 2147483647;
		for(int i=0;i<N;i++){
			int tmp;
			scanf("%d",&tmp);
			if(_min > tmp)_min = tmp;
			xsum ^= tmp;
			sum += tmp;
		}
		if(xsum != 0){
			printf("Case #%d: NO\n",t + 1);
		}else{
			printf("Case #%d: %d\n",t + 1,sum - _min);
		}
	}
	return 0;
}
