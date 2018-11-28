#include <stdio.h>
#include <stdlib.h>
#define min(a,b) a<b?a:b
#define max(a,b) a>b?a:b
#define abs(a)   a>0?a:-a

int O[101];
int co;
int B[101];
int cb;
int S[101];
int po,pb,io,ib;

int main(){
    
    int T,N,i,tempo,passo;
    int teste=1;
    char c;
    int x;
    
    scanf("%d",&T);
    
    while(T--){
			scanf("%d",&N);
			
			co = cb = 0;
			for(i=1;i<=N;i++){
				scanf(" %c %d",&c,&x);
				if(c=='O'){
					S[i] = 1;
					O[co++]=x;
				}else{
					S[i] = 2;
					B[cb++]=x;
				}
				
			}
			O[co] = 0;
			B[cb] = 0;
			
			po = pb = 1;
			io = ib = 0;
			tempo = 0;
			for(i=1;i<=N;i++){
				if(S[i]==1){
					//printf("movimento orange ir para %d\n",O[io]);
					
					
					if(O[io] > po) passo = O[io] - po;
					else passo = po - O[io];
					
					//printf("passo %d\n",passo);
					
					  
					tempo += passo;
					
					po = O[io];
					
					
					if( B[ib] >= pb ){
						if( pb + passo + 1 > B[ib]) pb = B[ib];
						else pb += passo + 1; 
					}else{
					  if( pb - passo - 1 < B[ib]) pb = B[ib];
					  else pb -= passo+1;
					}
					
					
					
					
					
					tempo++;
					//printf("Orange push button %d tempo %d\n",O[io],tempo);
					
					io++;
				}else{
					//printf("movimento blue ir para %d\n",B[ib]);
					
					if(B[ib] > pb) passo = B[ib] - pb;
					else passo = pb - B[ib];
					
					
					//printf("passo %d\n",passo);
					
					tempo += passo;
					
					pb = B[ib];
					
					if( O[io] >= po ){
						if( po + passo + 1 > O[io]) po = O[io];
						else po += passo + 1; 
					}else{
					  if( po - passo - 1 < O[io]) po = O[io];
					  else po -= passo+1;
					}
					
					
					
					tempo++;
					//printf("Blue push button %d tempo %d\n",B[ib],tempo);
					
					ib++;
				}
				//printf("comando %d orange %d blue %d tempo %d\n",i,po,pb,tempo);	
			}
			
			printf("Case #%d: ",teste++);
			printf("%d\n",tempo);
			
		
		}
    
		
		return 0;


}
