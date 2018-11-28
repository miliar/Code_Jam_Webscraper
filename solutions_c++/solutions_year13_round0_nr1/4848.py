#include<cstdio>
#include<cstring>
char s[5][5];
bool check(char c)
{
	int i,j;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			if(s[i][j]==c||s[i][j]=='T')continue;
			break;
		}
		if(j==4)return true;
		for(j=0;j<4;j++)
		{
			if(s[j][i]==c||s[j][i]=='T')continue;
			break;
		}
		if(j==4)return true;
	}
	for(i=0;i<4;i++)
	{
		if(s[i][i]==c||s[i][i]=='T')continue;
		break;
	}
	if(i==4)return true;
	for(i=0;i<4;i++)
	{
		if(s[i][3-i]==c||s[i][3-i]=='T')continue;
		break;
	}
	if(i==4)return true;
	return false;
}
int main()
{
	int T,i,j,ca=1;
	freopen("A-large.in","r",stdin);
	freopen("A-large.txt","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		for(i=0;i<4;i++)scanf("%s",s[i]);
		printf("Case #%d: ",ca++);
		int flag=-1;
		for(i=0;i<4;i++)
		{
			if(check('O'))flag=0;
			if(check('X'))flag=1;
		}
		if(flag==-1)
		{
			for(i=0;i<4;i++)
			{
				for(j=0;j<4;j++)
				{
					if(s[i][j]=='.')break;
				}
				if(j<4)break;
			}
			if(i<4)puts("Game has not completed");
			else puts("Draw");
		}
		else if(flag==0)puts("O won");
		else puts("X won");
	}
	return 0;
}