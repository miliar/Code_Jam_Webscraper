#include<stdio.h>
#include<memory.h>

int st[16];
char u[4]=" XO";

int whoWinsNow()
{
	int i,j,b_row,b_col;
	for(i=0;i<16;i+=4)
	{
		b_row=3;
		for(j=0;j<4;j++)
		{
			b_row&=st[i+j];
		}
		if(b_row>0)
			return b_row;
	}
	for(j=0;j<4;j++)
	{
		b_col=3;
		for(i=0;i<16;i+=4)
		{
			b_col&=st[i+j];
		}
		if(b_col>0)
			return b_col;
	}
	int b_dia1,b_dia2;
	b_dia1=b_dia2=3;
	for(i=0;i<16;i+=5)
		b_dia1&=st[i];
	for(i=3;i<13;i+=3)
	{
		b_dia2&=st[i];
	}
	if(b_dia1>0)return b_dia1;
	if(b_dia2>0)return b_dia2;
	return 0;
}


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test,T=0,i,j,ec;
	char map[4][5];

	scanf("%d",&test);

	for(;test>0;test--)
	{
		T++;
		memset(st,0,sizeof(st));
		ec=0;
		for(i=0;i<4;i++)
		{
			scanf("%s",map[i]);
			for(j=0;j<4;j++)
			{
				if(map[i][j]=='X')
				{
					st[i*4+j]=1;
				}
				else if(map[i][j]=='O')
				{
					st[i*4+j]=2;
				}
				else if(map[i][j]=='T')
				{
					st[i*4+j]=3;
				}
				else
					ec++;
			}
		}
		printf("Case #%d: ",T);
		int first = whoWinsNow();
		if(first!=0)
		{
			printf("%c won\n",u[first]);
			continue;
		}
		if(ec==0)
			printf("Draw\n");
		else
			printf("Game has not completed\n");
	}
	return 0;
}