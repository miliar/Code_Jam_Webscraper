#include <stdio.h>
#include <stdlib.h>

int C;
int D;
int T;
int N;
int teste=1;
char comb[38][4];
char oposto[29][3];
char input[101];
char typemagic[101];
char magic[101];
char flag;
char combinado;
char tem;

int pin;

void imprima(int tam){
		int i;
		printf("[");
		flag = 1;
		for(i=0;i<=tam;i++){
			
			if(input[i]!='-'){
			 if(flag==0) printf(", ");	
			 printf("%c",input[i]);
			 flag = 0;
			}
			
			
		}
		printf("]\n");
		

}


int main(){
	int i,j,k;
	scanf("%d",&T);
	
	while(T--){
		scanf("%d",&C);	
		
		for(i=0;i<C;i++){
			scanf("%s", comb[i]);
		}
		
		scanf("%d",&D);
		
		for(i=0;i<D;i++){
			scanf("%s", oposto[i]);
		}
		
		scanf("%d",&N);
	  scanf("%s", input);
	
		pin = 1;
	
	
		while( pin < N ){
	    
	    for(i=0;i<C;i++){
				if( (input[pin]==comb[i][0] && input[pin-1]==comb[i][1]) || 
				    (input[pin]==comb[i][1] && input[pin-1]==comb[i][0]) ){
						
						//printf("combinando %d\n",pin);
						input[pin-1] = '-';
						input[pin] = comb[i][2];
						pin++;
						i = 0;
				}
			}
			
			
			
			for(i=0;i<D;i++){
				if(input[pin]==oposto[i][0]){
					tem = 0;
					for(j=0;j<pin;j++){
						if(input[j]==oposto[i][1])
							tem = 1;
					}
					
					if(tem){
					 //printf("limpando %d\n",pin);
					 for(j=0;j<=pin;j++) input[j]='-'; 	
					}
					
							
				}else if(input[pin]==oposto[i][1]){
			    
			    tem = 0;
					for(j=0;j<pin;j++){
						if(input[j]==oposto[i][0])
							tem = 1;
					}
					
					if(tem){
					
					// printf("limpando %d\n",pin);
					 for(j=0;j<=pin;j++) input[j]='-'; 	
					}
				   
			  }	
			}
			
			
			//imprima(pin);
			pin++;
		//	printf("pin %d N %d\n", pin, N);
			//system("PAUSE");
			
	    
					
		}
		
		printf("Case #%d: ",teste++);
		imprima(N-1);
		
	
	}
	

}
