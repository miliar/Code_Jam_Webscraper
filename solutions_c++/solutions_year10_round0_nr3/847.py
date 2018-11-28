#include<stdio.h>
#include<algorithm>

using namespace std;

#define MAXN (1024)

long long int fw[MAXN],sum[MAXN],gr[MAXN];

int main(){
	int teste,nteste,i,j,r,n;
	long long int resp,soma,k;
	scanf("%d",&nteste);
	for(teste=1;teste<=nteste;teste++){
		scanf("%d %lld %d",&r,&k,&n);
		for(i=0;i<n;i++) scanf("%lld",gr+i);
		
		for(i=0;i<n;i++){
			j=i;
			soma=0;
			while(soma + gr[j] <=k){
				soma += gr[j];
				j++;
				if(j==n)j=0;
				if(j==i) break;
			}
			
			fw[i] = j;
			sum[i] = soma;
		}
		
		resp = 0;
		
		i=0;
		while(r--){
			resp += sum[i];
			i = fw[i];
		}
		printf("Case #%d: %lld\n",teste,resp);
	}
}
