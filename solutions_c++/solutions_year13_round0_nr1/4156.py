#include <stdio.h>
int t;
int m[5][5];
int s[2][5];
int d[2];
int main()
{
	scanf("%d",&t);
	for(int caso=1;caso<=t;caso++)
	{
		d[0]=0;
		d[1]=0;
		for(int i=1;i<=4;i++)
		{
			s[0][i]=0;
			s[1][i]=0;
		}
		int opa=0;
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
				char c;
				scanf(" %c",&c);
				if(c=='X') m[i][j]=1;
				else if(c=='O') m[i][j]=-1;
				else if(c=='T') m[i][j]=0;
				else 
				{
					opa=1;
					m[i][j]=100;
				}
				s[0][i]+=m[i][j];
				s[1][j]+=m[i][j];
			}
		}
		d[0]=m[1][1]+m[2][2]+m[3][3]+m[4][4];
		d[1]=m[1][4]+m[2][3]+m[3][2]+m[4][1];	
		int resp=0;
		for(int i=0;i<=1;i++)
		{
			if(d[i]==3 || d[i]==4) resp=1;
			if(d[i]==-3 || d[i]==-4) resp=-1;
		}
		for(int i=1;i<=4;i++)
		{
			for(int j=0;j<=1;j++)
			{
				if(s[j][i]==3 || s[j][i]==4) resp=1;
				if(s[j][i]==-3 || s[j][i]==-4) resp=-1;
			}
		}
		
		printf("Case #%d: ",caso);
		if(resp==0)
		{
			if(opa==1) printf("Game has not completed\n");
			else printf("Draw\n");
		}
		else if(resp==1) printf("X won\n");
		else printf("O won\n");
	}
	return 0;
}
