#include <stdio.h>
#include <stdlib.h>

int main(){

	int t;
	int a,b,i,j;
	int teste=1;
	
	teste = 1;
	
	scanf("%d",&t);
	
	while(t--){
		scanf("%d %d",&a,&b);
		int toques[4][1<<a];
		for(i=0;i<1<<a;i++){
			if(i==0){
			  toques[0][i] = b-a+1;
			}else{
				toques[0][i] = 2*b-a+2;
			}
			if(i>=0 && i<=1){
				toques[1][i] = b-a+3;
			}else{
				toques[1][i] = 2*b-a+4;
			}
			if(i>=0 && i<=3){
				toques[2][i] = b-a+5;
			}else{
				toques[2][i] = 2*b-a+6;
			}
			toques[3][i] = b+2;
		}
		
		double p[a];
		
		for(i=0;i<a;i++)
			scanf("%lf",&p[i]);
		
		double q[1<<a];
		
		for(i=0;i<1<<a;i++){
			q[i] = 1.0; 
			for(j=0;j<a;j++){
				if((i&(1<<j))){
					q[i] = q[i]*(1-p[a-j-1]);
				}else{
					q[i] = q[i]*p[a-j-1];
				}
			}
		}
		
		double e[4];
		double min;
		
		
		for(i=0;i<4;i++){
			e[i] = 0.0;
			
			
			
			for(j=0;j<1<<a;j++){
				
				e[i]+= toques[i][j]*q[j];
			}
			
			if(i==0) min = e[i];
			else if(e[i] < min) min = e[i];	
			
		
		}
		
		
		printf("Case #%d: %.6lf\n", teste++,min);
		 	
		
	
		
		
		
		
	
	
	}
	
	


}
