
#include<stdio.h>

int main(void){
	_int64 test;
	_int64 n;
	_int64 k;
	_int64 ti;
	_int64 num;

	scanf(" %I64d",&test);
	// printf("%ld\n",test);
	for(ti=0;ti<test;ti++){
		scanf(" %I64d",&n);
		scanf(" %I64d",&k);
		
		num=1;
		num<<=n;

		if(k%num==num-1){
			printf("Case #%I64d: ON\n",ti+1);
		}
		else{
			printf("Case #%I64d: OFF\n",ti+1);
		}
	}
	return 0;
}
