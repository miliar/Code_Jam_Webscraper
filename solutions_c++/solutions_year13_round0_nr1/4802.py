#include<stdio.h>
#include<string.h>
int t;
char map[10][10];

int check()
{
	int o=0,x=0,dot=0;
	for(int i=0;i<4;i++)
	{
		o=x=0;
		for(int j=0;j<4;j++)
			if(map[i][j]=='O')o++;
			else if(map[i][j]=='X')x++;
			else if(map[i][j]=='T')o++,x++;
			else dot++;
		if(o==4)return 1;
		else if(x==4)return 2;
		o=x=0;
		for(int j=0;j<4;j++)
			if(map[j][i]=='O')o++;
			else if(map[j][i]=='X')x++;
			else if(map[j][i]=='T')o++,x++;
		if(o==4)return 1;
		else if(x==4)return 2;
	}
	o=x=0;
	for(int i=0;i<4;i++)
	{
		if(map[i][i]=='O')o++;
		else if(map[i][i]=='X')x++;
		else if(map[i][i]=='T')o++,x++;
	}
	if(o==4)return 1;
	else if(x==4)return 2;
	o=x=0;
	for(int i=0;i<4;i++)
	{
		if(map[i][3-i]=='O')o++;
		else if(map[i][3-i]=='X')x++;
		else if(map[i][3-i]=='T')o++,x++;
	}
	if(o==4)return 1;
	else if(x==4)return 2;
	else if(dot>0)return 3;
	else return 0;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for(int kk=1;kk<=t;kk++)
	{
		gets(map[0]);
		for(int i=0;i<4;i++)gets(map[i]);
		int ans=check();
		printf("Case #%d: ",kk); 
		if(ans==1)puts("O won");
		else if(ans==2)puts("X won");
		else if(ans==3)puts("Game has not completed");
		else if(ans==0)puts("Draw");
	}
	
	return 0;
}
