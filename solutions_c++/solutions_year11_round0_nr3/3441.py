#include <stdio.h>


int main(){
	long long val;
	long long soma;
	long long x;
	long long menor;
	int n,m;
	int j;
	scanf("%d",&n);
	
	for(int i =1;i<=n;i++){
		scanf("%d",&m);
		x = soma = 0LL;
		menor = 1LL<<60;
		for(int j = 0;j<m;j++){
			scanf("%lld",&val);
			x=x^val;
			soma+=val;
			if(menor > val)
				menor = val;
		}
		printf("Case #%d: ",i);
		if(x == 0LL){
			printf("%lld\n",soma-menor);
		}else{
			printf("NO\n");
		}
	}
	return 0;
}
