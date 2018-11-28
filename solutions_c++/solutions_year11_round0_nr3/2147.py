#include <cstdio>


int main(){
	int min, cases,nums,cur,xord,sum;
	scanf("%d",&cases);
	for(int c=1; c<=cases; ++c){
		scanf("%d",&nums);
		min=1000000000;
		cur=0;
		xord=0;
		sum=0;
		for(int i=0; i<nums; ++i){
			scanf("%d",&cur);
			if(cur<min) min=cur;
			xord^=cur;
			sum+=cur;
		}
		printf("Case #%d: ",c);
		if(xord==0){
			printf("%d\n",sum-min);
		}else{
			printf("NO\n");
		}
	}
	return 0;
}

