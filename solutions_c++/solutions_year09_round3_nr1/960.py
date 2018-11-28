#include <stdio.h>
#include <string.h>

char s[63];
int vet[1000];


int main()
{
	int cases = 1 ,t,  i, base, aux;
	unsigned long long int soma;
	
	scanf("%d",&t);
	
	while(t--){
		scanf("%s",s);
		
		memset(vet,0,sizeof(vet));
		base = 0;
		for(i=0;s[i]!='\0';i++){
			if(vet[s[i]] == 0) vet[s[i]] = 1, base++;
		}
		
		if(base==1) base = 2;
		for(i='0';i<='9';i++) vet[i] = -1;
		for(i='a';i<='z';i++) vet[i] = -1;
		
		vet[s[0]] = 1;
		for(i=1;s[i]!='\0';i++){
			if(vet[s[i]]==-1) { vet[s[i]] = 0; break;}
		}
		aux = 2;
		for(;s[i]!='\0';i++){
			if(vet[s[i]]==-1) vet[s[i]] = aux++;
		}
		
		soma = 0;
		aux = 1;
		for(i=i-1;i>=0;i--){
			soma += vet[s[i]]*aux;
			aux *= base;
		}
		
		printf("Case #%d: %llu\n",cases++,soma);
		
	}
	
	
	return 0;
}
