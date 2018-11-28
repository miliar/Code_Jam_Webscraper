#include<stdio.h>
#include<math.h>
void task(){
	int n,k,x;
	scanf("%i%i",&n,&k);
	x=(int)pow(2,n)-1;
	if(k%(x+1)==x) printf("ON");
	else printf("OFF");
}
int main(){
	int x;
	int i;
	scanf("%i",&x);
	for(i=0;i<x;i++){
		printf("Case #%i: ",i+1);
		task();
		printf("\n");
	}
	return 0;
}
