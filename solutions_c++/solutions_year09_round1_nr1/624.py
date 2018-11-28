#include<stdio.h>

FILE *fs = fopen("input.txt","rt");
FILE *fp = fopen("output.txt","wt");

#define MAXN 10

int n,T;
int input[MAXN+1];

int check[1000];


int calc(int x,int b)
{
	int sum=0;

	while(x){
		sum = sum + (int)(x%b)*(int)(x%b);
		x = x/ b;	
	}
	return sum;
}

int main()
{
	int i,j,k,p,l;
	char ch;

	fscanf(fs,"%d",&T);

	for(i=1;i<=T;i++){
		for(n=1;;n++){
			fscanf(fs,"%d",&input[n]);
			ch = 0;
			fscanf(fs,"%c",&ch);
			if(ch != ' ' || !ch) break;
		}		

		
		fprintf(fp,"Case #%d: ",i);
			
		for(j=2;;j++){
			for(k=1;k<=n;k++){
				p = j;
				
				for(l=1;l<=1000;l++) check[l] = 0;
				if(p < 1000) check[p] = 1;
				while(1){
					p = calc(p,input[k]);
					if(p == 1) break;
					if(check[p]) break;
					check[p] = 1;
				}
				if(p != 1) break;
			}		

			if(k == n+1){
				fprintf(fp,"%d\n",j);
				break;
			}
		}
	}
	
	return 0;
}