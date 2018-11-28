#include<stdio.h>

#define MAXN 100
#define MAX 0x7ffffff

FILE *fs = fopen("input.txt","rt");
FILE *fp = fopen("output.txt","wt");

int n;
int P,Q;
int bribe[MAXN+1];

int dy[MAXN+1][MAXN+1];

void dynamic()
{
	int i,j,gap,k;

	for(i=1;i<=Q;i++){
		for(j=i+1;j<=Q;j++){
			dy[i][j] = MAX;
		}
		dy[i][i+1] = 0;
	}

	for(i=1;i<=Q-2;i++){
		dy[i][i+2] = bribe[i+2]-bribe[i]-2;
	}
	for(gap=3;gap<Q;gap++){
		for(i=1;i<Q;i++){
			j = i+gap;
			if(j <= Q){
				for(k=i+1;k<j;k++){
					if(dy[i][j] > dy[i][k] + dy[k][j] + bribe[j]-bribe[i]-2){
						dy[i][j] = dy[i][k] + dy[k][j] + bribe[j] - bribe[i]-2;
					}
				
				}
			}
		}		
	}
}

int main()
{
	int i,j;

	fscanf(fs,"%d",&n);
	for(i=1;i<=n;i++){
		fscanf(fs,"%d %d",&P,&Q);
		bribe[1] = 0;
		for(j=2;j<=Q+1;j++) fscanf(fs,"%d",&bribe[j]);
		bribe[Q+2] = P+1;
		Q += 2;
		
		dynamic();
		fprintf(fp,"Case #%d: %d\n",i,dy[1][Q]);
	}
	return 0;
}