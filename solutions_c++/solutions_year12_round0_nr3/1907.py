#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
	int t,T;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		int A,B,n,count=0;
		scanf("%d %d",&A,&B);
		for(n=A;n<=B;n++){
			int a = n,b,p=10;
			int m[10],mcount=0;
			while(a>=10){
				a = n/p;
				b = n%p;
				p*=10;
				char num1[10]="",num2[10]="";
				itoa(a,num1,10);
				itoa(b,num2,10);
				strcat(num2,num1);
				int M = atoi(num2);
				int found=0,i;
				for(i=0;i<mcount;i++){
					if(m[i]==M){
						found=1;
						break;
					}
				}
				if(!found){
					if(M>n&&M<=B){
					    count++;
						m[mcount]=M;
						mcount++;
					}
				}					
			}
		}
		printf("Case #%d: %d\n",t,count);
	}	
	return 0;
}
