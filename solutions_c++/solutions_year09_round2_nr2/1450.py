#include <stdio.h>
#include <string.h>
#include <algorithm>
#define tam 8
using namespace std;



char linha[1024];
int number[tam];
int sol[tam];
int original[tam];
int x;
int t;
int nao_tem;

void imprime( int * v, int n){
	int i;
	
	for(i=0;;i++) if(v[i]!=0) break;
	
	for(;i<n;i++){
		printf("%d",v[i]);
	
	}
	  
	printf("\n");
}


bool mycomp (int a , int  b)
{ return a > b; }


int main(){

	int m;
	int teste=1;
	scanf("%d",&m);
	

	while(m--){
			int i,j;
			
			number[0]=0;
			
			scanf("%s",linha);
			
			t = strlen(linha)+1;
			
			for(i=1;i<=t;i++)
			  number[i] = linha[i-1]-'0';
			
			for(i=0;i<=t;i++){
			   original[i] = number[i];
		     sol[i] = number[i];
		  }
			
			
			
			
			nao_tem = 1;
			do {
				//printf("permutacao\n");
        //imprime(number,t);
        if( lexicographical_compare(number,number+t,original,original+t,mycomp) > 0){
        	//printf("maior que o original\n");
        	
        	if(nao_tem){
					   //printf("nao_tem\n");
						 for(i=0;i<=t;i++)
        	     sol[i] = number[i];
        	   nao_tem = 0;
					}else{
        	
						if( lexicographical_compare(number,number+t,sol,sol+t,mycomp) < 0 ){
	        	   //printf("menor que a solução atual");
							 for(i=0;i<=t;i++)
	        	     sol[i] = number[i];
						}
					}
				}else{
					//printf("maior que a original\n");
				}
        
      } while ( next_permutation (number,number+strlen(linha)+1) );

			
			printf("Case #%d: ",teste++);
			imprime(sol,t);
		
			
			
			
			
			
			
	}
	
	
}
