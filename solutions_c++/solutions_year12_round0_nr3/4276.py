#include<stdio.h>
#include<math.h>
#include<conio.h>

int T,A,B;
	FILE *fo=fopen("output.txt","w");

int getlen(int x){
int len =0;
while(x>=10){
	x/=10;
	len++;
}
len++;
return len;
}

int process(int x){
	int len = getlen(x);
	int temp=x;
	int ppp=1;
	int count = 0;

	
	for(int i=1;i<len;i++) ppp*=10;
	
	
	for(int i=1;i<len;i++){
		temp=(temp/10)+(temp%10)*ppp;
		if(x<temp){
			if(temp<=B){
				count++;
				//fprintf(fo,"(%d , %d)\n",x,temp);
			}
		}
	}	
	
	return count;
}


int main(){
	FILE *fp=fopen("input.txt","r");

	fscanf(fp,"%d",&T);
	for(int casen = 1 ; casen <= T; casen++){
		fscanf(fp,"%d %d",&A,&B);
		int solun=0;
 
		for(int i=A;i<=B;i++)
				solun+=process(i);
		
		fprintf(fo,"Case #%d: %d\n",casen,solun);
	}
}
