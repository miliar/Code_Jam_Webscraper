#include<cstdio>
#include<iostream>
using namespace std;
char map[6][6];

char f()
{
	int i,j,flag;
	char c;
	for(i=1;i<=4;i++)
	{
		if(((c=map[i][1])!='.')&&c!='T')
		{
			flag=1;
			for(j=2;j<=4;j++)
			{
				if(map[i][j]!='T'&&map[i][j]!=c)
				{
					flag=0;
					break;
				}
			}
			if(flag==1)return c;
		}
	}
	for(i=1;i<=4;i++)
	{
		if(((c=map[i][4])!='.')&&c!='T')
		{
			flag=1;
			for(j=1;j<=3;j++)
			{
				if(map[i][j]!='T'&&map[i][j]!=c)
				{
					flag=0;
					break;
				}
			}
			if(flag==1)return c;
		}
	}
	for(i=1;i<=4;i++)
	{
		if(((c=map[1][i])!='.')&&c!='T')
		{
			flag=1;
			for(j=2;j<=4;j++)
			{
				if(map[j][i]!='T'&&map[j][i]!=c)
				{
					flag=0;
					break;
				}
			}
			if(flag==1)return c;
		}
	}
	for(i=1;i<=4;i++)
	{
		if(((c=map[4][i])!='.')&&c!='T')
		{
			flag=1;
			for(j=1;j<=3;j++)
			{
				if(map[j][i]!='T'&&map[j][i]!=c)
				{
					flag=0;
					break;
				}
			}
			if(flag==1)return c;
		}
	}
	if((c=map[1][1])!='.'&&c!='T')
	{
		flag=1;
		for(i=2;i<=4;i++)
		{
			if(map[i][i]!='T'&&map[i][i]!=c)
			{
				flag=0;
				break;
			}
		}
		if(flag==1)return c;
	}
	if((c=map[4][4])!='.'&&c!='T')
	{
		flag=1;
		for(i=1;i<=3;i++)
		{
			if(map[i][i]!='T'&&map[i][i]!=c)
			{
				flag=0;
				break;
			}
		}
		if(flag==1)return c;
	}
	if((c=map[1][4])!='.'&&c!='T')
	{
		flag=1;
		for(i=2;i<=4;i++)
		{
			if(map[i][5-i]!='T'&&map[i][5-i]!=c)
			{
				flag=0;
				break;
			}
		}
		if(flag==1)return c;
	}
	if((c=map[4][1])!='.'&&c!='T')
	{
		flag=1;
		for(i=1;i<=3;i++)
		{
			if(map[i][5-i]!='T'&&map[i][5-i]!=c)
			{
				flag=0;
				break;
			}
		}
		if(flag==1)return c;
	}
	return 0;
}

int main()
{
	freopen("A-large.in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,step,i,j;
	int type;
	char t;
	scanf("%d",&step);
	for(T=1;T<=step;T++)
	{
		printf("Case #%d: ",T);
		type=0;
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				cin>>map[i][j];
				if(map[i][j]=='.')type=1;
			}
		}
		t=f();
		if(t=='O')printf("O won\n");
		else if(t=='X')printf("X won\n");
		else if(type==1)printf("Game has not completed\n");
		else printf("Draw\n");
	}
	return 0;
}