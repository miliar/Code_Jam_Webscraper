#include <stdio.h>
#include <algorithm>

#define MAX 100

int person[MAX];
FILE *stin,*stout;

bool compare(int a, int b);

int main(void)
{
	int i,j,T,N,S,scount,P,count,temp;

	stin=fopen("B-large.in","r");
	stout=fopen("output.txt","w");

	fscanf(stin,"%d",&T);
	for(i=0;i<T;i++){
		count=scount=0;
		fscanf(stin,"%d%d%d",&N,&S,&P);
		for(j=0;j<N;j++){
			fscanf(stin,"%d",&person[j]);
		}
		std::sort(person,person+N,compare);

		for(j=0;j<N;j++){
			if(person[j] > ((P-1)*3) ) count++;
			else{
				temp=person[j]-P;
				if(S>scount){
					if(temp < 0){
						if(temp == P) count++;
					}
					else if((temp == P-2+P-2) || (temp == P-2+P-1) || (temp == P-2+P)) count++;
					scount++;
				}
				else{
					if(temp < 0){
						if(temp == P) count++;
					}
					if((temp == P-1+P-1) || (temp == P-1+P) || (temp == P+P)) count++;
				}
			}
		}
		fprintf(stout,"Case #%d: %d\n",i+1,count);
	}

	fclose(stin);
	fclose(stout);

	return 0;
}

bool compare(int a, int b)
{
     return a > b;
}