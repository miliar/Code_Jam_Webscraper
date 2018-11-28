#include<stdio.h>
#include<conio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>

int main(int argc, char **argv)
{

	int H,W, N, cases ;
	int map[102][102]; 
	int k[102][102];
	int pi[10002], pj[10002];

	char res[102][102];
	char label;
    
	int i, j, m, n, t, lowest;

    freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);

	scanf("%d",&cases);
	for(N=1; N<=cases; N++)
	{
		scanf("%d%d",&H,&W);
		for(i=1;i<=H;i++)
			for(j=1;j<=W;j++)
				scanf("%d",&map[i][j]);

		//--------- init --------------//
		label='a';

		for(i=1;i<=H;i++)
			for(j=1;j<=W;j++)
				res[i][j]='X';
		

		for(j=0;j<=W+1;j++)
		{
			map[0][j]  =11000;
			map[H+1][j]=11000;
		}

		for(i=0;i<=H+1;i++)
		{
			map[i][0]   = 11000;
			map[i][W+1] = 11000;
		}

		//-----------------------------//

		for(i=1;i<=H;i++)
		{
			for(j=1;j<=W;j++)
			{
											{	k[i][j]=0;  lowest=map[i][j];   }
				if(lowest	>map[i-1][j])	{	k[i][j]=4;  lowest=map[i-1][j]; } //UP er one is smaller
				if(lowest	>map[i][j-1])	{	k[i][j]=3;  lowest=map[i][j-1]; } //LT
				if(lowest	>map[i][j+1])	{	k[i][j]=2;  lowest=map[i][j+1]; } //RT
				if(lowest	>map[i+1][j])	{	k[i][j]=1;  lowest=map[i+1][j]; } //DN
			}
		}

		for(i=1;i<=H;i++)
		{
			for(j=1;j<=W;j++)
			{
				if(res[i][j]!='X')	continue;

				m=i; n=j; t=0;
				while((k[m][n]!=0) && ((res[m][n]=='X')))
				{
					pi[t]=m; pj[t]=n; t++;
					if	   (k[m][n]==4) {	m--;	}
					else if(k[m][n]==3) {	n--;	}
					else if(k[m][n]==2) {	n++;	}
					else if(k[m][n]==1) {	m++;	}
				}

				if(res[m][n]=='X')// If its a Sink
				{ 
					res[m][n] = label;
					label++;
				}
				
				for(t-- ; t>=0; t--)
					res[pi[t]][pj[t]]=res[m][n];
			}
		}

		printf("Case #%d:\n",N);

		for(i=1;i<=H;i++)
		{
			for(j=1;j<=W;j++)
			{
				printf("%c",res[i][j]);
				if(j!=W)printf(" ");
			}
			printf("\n");
		}
	}// N

	return 0;
}

