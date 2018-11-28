#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 10

FILE *stin,*stout;

void right_shift(char a[],int len);

int main(void)
{
	int i,j,k,T,A,B,count,temp,previous_j=0,previous_temp=0;
	char m[MAX],cB[MAX];

	stin=fopen("C-small-attempt0.in","r");
	stout=fopen("output.txt","w");

	fscanf(stin,"%d",&T);
	for(i=0;i<T;i++){
		count=0;
		fscanf(stin,"%d%d",&A,&B);
		
		for(j=A;j<=B;j++){
			itoa(j,m,10);
			for(k=0;k<strlen(m)-1;k++){
				right_shift(m,strlen(m));
				if(m[0] != 0){
					temp=atoi(m);
					if((temp <= B) && (temp > j) && ( (previous_j != j) || (previous_temp != temp) )){
						count++;
						previous_j=j;
						previous_temp=temp;
					}
				}
			}
		}
		fprintf(stout,"Case #%d: %d\n",i+1,count);
	}

	fclose(stin);
	fclose(stout);

	return 0;
}

void right_shift(char a[],int len)
{
	int i;
	char temp=a[len-1];

	for(i=len-1;i>0;i--){
		a[i]=a[i-1];
	}
	a[0]=temp;
}