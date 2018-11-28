#include <stdio.h>
#include <stdlib.h>


int om[20][20];
int n,m,d;

int check_center2(int x,int y,int k)
{
	int i,j;
	int x_mass=0,y_mass=0;
	for(i = x ; i <= x + k; i++)
	{
		for(j = y; j <= y + k ;j++)
		{
			if( (i==x || i ==  x+k) && (y==j || j == y + k) )
				continue;
			x_mass+= (2*(i-x+1) - (k+2)) * (om[i][j] + d);
			y_mass+= (2*(j-y+1) - (k+2)) * (om[i][j] + d);			
		}
	}
	if(x_mass ==0 && y_mass ==0)
		return 1;
	return 0;
}

int check_center(int x,int y,int k)
{
	int i,j;
	int x_mass=0,y_mass=0;
	for(i = x - k ; i <= x + k; i++)
	{
		for(j = y - k; j <= y + k ;j++)
		{
			if( abs(i - x) == k && abs(j - y) ==k)
				continue;
			x_mass+= (i - x) * (om[i][j] + d);
			y_mass+= (j - y) * (om[i][j] + d);
		}
	}
	if(x_mass ==0 && y_mass ==0)
		return 1;
	return 0;
}

int main()
{
	int cas,asd;
	int i,j,max,k;
	char cc;
//	freopen("2.in","r",stdin);
	freopen("B-small-attempt4.in","r",stdin);
	freopen("B-small-attempt4.out","w",stdout);
	scanf("%d",&cas);
	for(asd=0;asd<cas;asd++)
	{
		printf("Case #%d: ",asd+1);
		scanf(" %d %d %d",&n,&m,&d);
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++)
			{
				scanf(" %c",&cc);
				om[i][j] = cc - '0';
			}
		}

		max = 0;
		for(i=1;i<=n-2;i++)
		{
			for(j=i+2;j<=n;j++)
			{
				if( (j - i) % 2 == 0)
				{
				for(k = (j - i)/2 + 1; k <= m - (j - i)/2 ; k++)
				{

					if(check_center( (i+j)/2 , k, (j - i)/2) )
					{
						if(j - i + 1 > max)
							max = j - i + 1;
					}

				}
				}
				else
				{
				for(k=1;k <= m  - (j - i); k++)
				{
					if(check_center2(i, k , j - i) )
					{
						if(j - i + 1 > max)
						max = j - i + 1;
					}
				}
				}
			}
		}
		if(max==0)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",max);
	}
	return 0;
}
