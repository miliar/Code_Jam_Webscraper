#include<stdio.h>
#include<string.h>
#include<string>
#include<stdlib.h>
#include<math.h>
#include<algorithm>

using namespace std;
char buf[64];


int main(){
	long long int resp,aux,pot[64];
	int i,j,T,count;
	char c;
	
	scanf("%d ",&T);
	int tot = T;
	while(T--){
		gets(buf);
//		printf("%s ",buf);
		int tam = strlen(buf);
		count = 0;
		for(i=0;i<tam;i++){
			if(buf[i] < 0) continue;
			count--;
			
			c = buf[i];
			for(j=i;j<tam;j++){
				if(buf[j] == c){
					buf[j] = count;
				}
			}
		}
		long long int b = -count;
//		printf("%lld\n",b);
		if(b == 1)
			b++;
		
		pot[0] = 1;
		for(i=1;i<62;i++)
			pot[i] = pot[i-1]*b;
		
		resp = 0;
		
		for(i=0;i<tam;i++){
			if(buf[i] == -1){
				resp += pot[tam-i-1];
			}else if(buf[i] == -2){
				continue;
			}else{
				aux = -buf[i] - 1;
				resp += aux*pot[tam-i-1];
			}
		}
		
		
		printf("Case #%d: %lld\n",tot-T,resp);
	}

	return 0;
}
