# include <stdio.h>
# include <iostream>
# include <string>
using namespace std;
char map[4][4];
int dir[8][2] = {1,0,0,1,-1,0,0,-1,1,1,-1,-1,1,-1,-1,1};
int flag,c,sig,flag2;
string s;
char status;
void dfs(int i,int j,int d)
{
	if (c == 3)
	{
		if (sig == 1)
			flag2 = 2;
		else
			flag2 = 3;
		return;
	}
	int next_i,next_j;
	if (status == 'X')
		sig = 1;
	else
	    sig = 2;	
	next_i = i+dir[d][0];next_j = j+dir[d][1];
	if (next_i>=0&&next_j>=0&&next_j<4&&next_i<4)
	{
		if (map[next_i][next_j] == status || map[next_i][next_j] == 'T')
		{
			c++;
			return dfs(next_i,next_j,d);
		}
	}
	return;	
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t,p,i,j,d;
	scanf("%d%*c",&t);
	for (p=1;p<=t;++p)
	{
		flag = flag2 = 0;
		for (i=0;i<4;++i)
		{
			for (j=0;j<4;++j)
				scanf("%c",&map[i][j]);
			getchar();
		}
		getline(cin,s);
		for (i=0;i<4;++i)
			for (j=0;j<4;++j)
			{
				if (map[i][j] == '.')
					flag = 1;
				else if (map[i][j] != 'T')
				{
					status = map[i][j];
					for (d=0;d<8;++d)
					{
						c = sig = 0;
						dfs(i,j,d);
					}		
				}
			}	
		if (flag2==2)
			printf("Case #%d: X won\n",p);
		else if (flag2==3)
			printf("Case #%d: O won\n",p);
		else if (flag)
			printf("Case #%d: Game has not completed\n",p);
		else
			printf("Case #%d: Draw\n",p);
	}	
	return 0;
}