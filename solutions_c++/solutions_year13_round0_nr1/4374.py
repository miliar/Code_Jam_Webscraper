#include<cstdio>
using namespace std;
char s[5][10];
bool isDown()
{
	int i,j;
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			if(s[i][j]=='.')
				return false;
	return true;
}
bool isLine(char c,int l)
{
	int i;
	for(i=0;i<4;i++)
		if(s[l][i]!=c && s[l][i]!='T')
			return false;
	return true;
}
bool isCol(char c,int l)
{
	int i;
	for(i=0;i<4;i++)
		if(s[i][l]!=c && s[i][l]!='T')
			return false;
	return true;
}
bool isDia1(char c)
{
	int i;
	for(i=0;i<4;i++)
		if(s[i][i]!=c && s[i][i]!='T')
			return false;
	return true;
}
bool isDia2(char c)
{
	int i;
	for(i=0;i<4;i++)
		if(s[i][3-i]!=c && s[i][3-i]!='T')
			return false;
	return true;
}
int cnt()
{
	int i;
	for(i=0;i<4;i++)
		if(isLine('X',i) || isCol('X',i))
			return 1;
	if(isDia1('X') || isDia2('X'))
		return 1;
	for(i=0;i<4;i++)
		if(isLine('O',i) || isCol('O',i))
			return 0;
	if(isDia1('O') || isDia2('O'))
		return 0;
	return -1;
}
int main()
{
	int t,cas=0,i;
	freopen("A-large.in","r",stdin);
	freopen("o.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		for(int i=0;i<4;i++)
			scanf("%s",s[i]);
		printf("Case #%d: ",++cas);
		int num=cnt();
		if(num==-1)
		{
			if(isDown())
				printf("Draw\n");
			else
				printf("Game has not completed\n");
		}
		if(num==1)
			printf("X won\n");
		if(num==0)
			printf("O won\n");
	}
	return 0;
}
