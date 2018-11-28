#include<cstdio>

void check(int x)
{
	if(x==3  ||x==4  )throw true;
	if(x==300||x==400)throw false;
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		int s=0,b[4][4];
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				char c;
				scanf(" %c",&c);
				switch(c)
				{
					case 'X':
						b[i][j]=1;
						break;
					case '.':
						b[i][j]=10;
						break;
					case 'O':
						b[i][j]=100;
						break;
					default:
						b[i][j]=0;
				}
				s+=b[i][j];
			}
		}
		printf("Case #%d: ",t);
		try
		{
			for(int i=0;i<4;i++)
			{
				check(b[i][0]+b[i][1]+b[i][2]+b[i][3]);
				check(b[0][i]+b[1][i]+b[2][i]+b[3][i]);
			}
			check(b[0][0]+b[1][1]+b[2][2]+b[3][3]);
			check(b[0][3]+b[1][2]+b[2][1]+b[3][0]);
			puts(s==708||s==808?"Draw":"Game has not completed");
		}
		catch(bool x)
		{
			puts(x?"X won":"O won");
		}
	}
	return 0;
}
