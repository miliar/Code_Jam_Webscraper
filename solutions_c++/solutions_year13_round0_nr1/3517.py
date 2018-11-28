#include <cstdio>
#include <queue>
using namespace std;
#define M 5
int map[M][M];
int mark;
bool judge(int a)
{
	map[mark/4+1][mark%4+1]=a;
	int i,j;
	for(i=1;i<=4;i++)
	{
		if(map[i][1]==a&&map[i][1]==map[i][2]&&map[i][1]==map[i][3]&&map[i][1]==map[i][4])
			return true;
	}
	for(i=1;i<=4;i++)
	{
		if(map[1][i]==a&&map[1][i]==map[2][i]&&map[1][i]==map[3][i]&&map[1][i]==map[4][i])
			return true;
	}
	if(map[1][1]==a&&map[1][1]==map[2][2]&&map[1][1]==map[3][3]&&map[1][1]==map[4][4])
		return true;
	if(map[4][1]==a&&map[4][1]==map[3][2]&&map[4][1]==map[2][3]&&map[4][1]==map[1][4])
		return true;
	return false;
}
int main()
{
	int i,j,t,d=1,count;
	char s[5];
	scanf("%d",&t);
	while(t--)
	{
		mark=-1,count=0;
		for(i=0;i<4;i++)
		{
			scanf("%s",s);
			for(j=0;j<4;j++)
			{
				if(s[j]=='X')	map[i+1][j+1]=1;
				if(s[j]=='O')	map[i+1][j+1]=2;
				if(s[j]=='.')	map[i+1][j+1]=0,count++;
				if(s[j]=='T')	map[i+1][j+1]=3,mark=i*4+j;
			}
		}
		printf("Case #%d: ",d++);
		if(judge(1))
		{
			printf("X won\n");
			continue;
		}
		if(judge(2))
		{
			printf("O won\n");
			continue;
		}
		if(count==0)
		{
			printf("Draw\n");
		}
		else
			printf("Game has not completed\n");
	}
	return 0;
}
