#include <stdio.h>
#include <stdlib.h>

void answer (int j,int n,int k){

	int cosiente=k;
	int residuo;

	for(int i=0;i<n;++i){

		if(cosiente%2<1){

			printf("Case #%d: OFF\n",j);
			return;

		}
		else{
			cosiente/=2;
			
		}

	}


printf("Case #%d: ON\n",j);

}

int main(){
 freopen("A-large.in", "r", stdin);
 freopen("A-large.out", "w", stdout);

int c;
scanf("%d",&c);

for(int i=1;i<=c;++i){

int n,k;
	scanf("%d %d",&n,&k);

	answer(i,n,k);

}




return 0;

}