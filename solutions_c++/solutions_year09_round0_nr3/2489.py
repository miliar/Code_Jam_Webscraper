#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char word[501];
char pattern[30];
int cont;


void busca(int iw,int ip){

	int j;
	
	if(ip == strlen(pattern) ) cont++;
	else{
		for(j=iw; j< strlen(word); j++ )
		   if(word[j]==pattern[ip])
		      busca(j+1, ip+1);
	}  
	      
}

int main(){
	
	int n;
	int teste = 1;
	
	scanf("%d\n",&n);
	
	
	while(n--){
	  gets(word);
		
		
		
		strcpy(pattern,"welcome to code jam");
		
		cont = 0;
		busca(0,0);
		
		printf("Case #%d: %04d\n",teste++,cont%10000);
		
		
	}
}
