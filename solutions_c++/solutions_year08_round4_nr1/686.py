#include<stdio.h>
#include<string.h>

const int maxn = 10000;
int n, v;
int n1, n2;
int node[maxn][2];
int f[maxn][2];

int main() {
	int cs, step;
	scanf("%d",&cs);	
	for(step=1;step<=cs;step++)
	{
		memset(node, 0, sizeof(node));		
		int i,j,k;
		for(i=0;i<maxn;i++)for(j=0;j<2;j++)f[i][j]=1000000;


		scanf("%d%d",&n, &v);
		n1 = (n-1)/2;
		n2 = (n+1)/2;
		for(i=0;i<n1;i++){
			scanf("%d%d",&node[i][0], &node[i][1]);
		}
		for(j=0;j<n2;j++){
			scanf("%d",&node[i][0]);
			f[i][node[i][0]] = 0;
			i++;			
		}
		for(i=n1-1;i>=0;i--)
		{
			int i1 = 2*i+1;
			int i2 = 2*i+2, f1;
			int l,r;
			for(l=0;l<2;l++)for(r=0;r<2;r++)
			{
				f1 = f[i1][l] + f[i2][r];					
				if(node[i][0]==1)
				{
					if(f1<f[i][l&r]) f[i][l & r] = f1;	
				} else {
					if(f1<f[i][l|r]) f[i][l | r] = f1;
				}				
			}
			if(node[i][1]==0) continue;
			
			for(l=0;l<2;l++)for(r=0;r<2;r++)
			{
				f1 = f[i1][l] + f[i2][r] + 1;					
				if(node[i][0]==0)
				{
					if(f1<f[i][l&r]) f[i][l & r] = f1;	
				} else {
					if(f1<f[i][l|r]) f[i][l | r] = f1;
				}				
			}
		}
		if(f[0][v]==1000000) printf("Case #%d: IMPOSSIBLE\n", step);
		else printf("Case #%d: %d\n", step, f[0][v]);
	}
	return 0;
}