#include<stdio.h>

#define MAXN 100

int n,T;
int d[MAXN+1][MAXN+1];

int c[MAXN+1];

int sol;

FILE *fs = fopen("input.txt","rt");
FILE *fp = fopen("output.txt","wt");

void mov(int from,int to)
{
	int i,t;

	for(i=from;i>to;i--){
		t = c[i];
		c[i]=c[i-1];
		c[i-1]=t;
	}
	sol += (from-to);
}

void input()
{
	int i,j,k,l,m,n,t;

	fscanf(fs,"%d",&T);

	for(k=1;k<=T;k++){
		fscanf(fs,"%d",&n);
		for(i=1;i<=n;i++){
			for(j=1;j<=n;j++){
				fscanf(fs,"%1d",&d[i][j]);
			}
			for(j=n;j>=1;j--) if(d[i][j]) break;
			c[i] = j;
		}

		sol = 0;
		for(i=1;i<=n;i++){
			if(c[i] > i){
				for(j=i+1;j<=n;j++){
					if(c[j] <= i) break;
				}
				if(j <= n) mov(j,i);
			}
		}

		fprintf(fp,"Case #%d: %d\n",k,sol);
	}
}

int main()
{

	input();
	return 0;

}
