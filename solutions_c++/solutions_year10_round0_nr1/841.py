#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

int main(){
	int nteste,teste,n,k,pot;
	scanf("%d",&nteste);
	for(teste =1;teste <=nteste;teste++){
		printf("Case #%d: ",teste);
		scanf("%d %d",&n,&k);
		pot = 1<<n;
		k -= pot - 1;
		if(k < 0  || k % pot != 0)
			printf("OFF\n");
		else
			printf("ON\n");				
	}
}
