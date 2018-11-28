#include <stdio.h>
#include <stdlib.h>

int max;
int T;
int N;
int V[1001];
  


int pile(int i,int s1,int x1, int s2,int x2){
	
	if(i>=N){
		if((x1^x2)==0){
			if(s1 > max && s2!=0 ){
				max = s1;  
			}
		}
	}else{
		pile(i+1,s1+V[i],x1^V[i],s2,x2);
		pile(i+1,s1,x1,s2+V[i],x2^V[i]);
	}
}



int main(){
  int i;
  int soma;
  int teste=1;
	
	scanf("%d",&T);
	while(T--){
		scanf("%d",&N);
		
		soma = 0;
		for(i=0;i<N;i++){
		  scanf("%d",&V[i]);
			soma ^=  V[i];
		}
			
    
		if(soma!= 0){
			printf("Case #%d: ",teste++);
		  printf("NO\n");
		}else{
			max = 0;
			pile(0,0,0,0,0);
			printf("Case #%d: ",teste++);
		  printf("%d\n",max);
		}
			
	}
  
  
	return 0;
}
