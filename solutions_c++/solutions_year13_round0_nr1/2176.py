#include <stdio.h>
#include <vector>
int check(char p[4][4])
{
	int flag1=0,flag2=0,flag3=0,flag4,flag5,i,j;
	for(i=0;i<4;i++)
	{
		flag1=0;
		flag2=0;
		flag4=0;
		flag5=0;
		for(j=0;j<4;j++)
		{
			if(p[i][j]=='O' || p[i][j]=='.')
				flag1=1;
			if(p[i][j]=='X' || p[i][j]=='.')
				flag2=1;
			if(p[j][i]=='O' || p[j][i]=='.')
				flag4=1;
			if(p[j][i]=='X' || p[j][i]=='.')
				flag5=1;

			if(p[i][j]=='.')
				flag3=1;
		}		
		if(flag1==0 || flag4==0)
			return 0;
		if(flag2==0 || flag5==0)
			return 1;
	}
	flag1=0;
	flag2=0;
	flag4=0;
	flag5=0;
	for(i=0;i<4;i++)
	{
		if(p[i][i]=='O' || p[i][i]=='.')
			flag1=1;
		if(p[i][i]=='X' || p[i][i]=='.')
			flag2=1;
		if(p[i][4-i-1]=='O' || p[i][4-i-1]=='.')
			flag4=1;
		if(p[i][4-i-1]=='X' || p[i][4-i-1]=='.')
			flag5=1;		
	}
	if(flag1==0 || flag4==0)
		return 0;
	if(flag2==0 || flag5==0)
		return 1;
	if(flag3==0)
		return 2;
	return 3;
}
int main()
{
	int i,j,k,t,test;
	char p[4][4];
	scanf("%d\n",&test);
	for(t=1;t<=test;t++)
	{
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%c",&p[i][j]);
			}
			scanf("\n");
		}
		scanf("\n");
		k=check(p);
		if(k==0)
			printf("Case #%d: X won\n",t);
		else if(k==1)
			printf("Case #%d: O won\n",t);
		else if(k==2)
			printf("Case #%d: Draw\n",t);
		else if(k==3)
			printf("Case #%d: Game has not completed\n",t);

	}
	return 0;
}