#include<stdio.h>
/*
google code jam 2010
qualification
A
*/
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	long z,zi=1;
	scanf("%ld",&z);
	while(z--){
		long n,k,bi=1;
		scanf("%ld%ld",&n,&k);
		bi=(bi<<n)-1;
		printf("Case #%ld: ",zi++);
		if((k&bi)==bi){
			printf("ON\n");
		}else{
			printf("OFF\n");
		}
	}
	return 0;
}
