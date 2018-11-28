#include<cstdio>
#include<cstring>
char c[6][6];
#define x_win 0
#define o_win 1
#define draw 2
int check()
{
	int x[2][6],y[2][6],s[2][2];
	bool flag=0;
	memset(x,0,sizeof(x));
	memset(y,0,sizeof(y));
	memset(s,0,sizeof(s));
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		{
			if(c[i][j]=='X')
			{
				x[0][i]++;
				y[0][j]++;
				if(i==j)s[0][0]++;
				if(i+j==3)s[0][1]++;
			}
			else if(c[i][j]=='O')
			{
				x[1][i]++;
				y[1][j]++;
				if(i==j)s[1][0]++;
				if(i+j==3)s[1][1]++;
			}
			else if(c[i][j]=='T')
			{
				x[0][i]++;
				x[1][i]++;
				y[0][j]++;
				y[1][j]++;
				if(i==j)
				{
					s[0][0]++;
					s[1][0]++;
				}
				if(i+j==3)
				{
					s[0][1]++;
					s[1][1]++;
				}
			}
			else flag=1;
		}
	for(int i=0;i<4;i++)
	{
		if(x[0][i]==4)return x_win;
		if(x[1][i]==4)return o_win;
		if(y[0][i]==4)return x_win;
		if(y[1][i]==4)return o_win;
	}
	if(s[0][0]==4)return x_win;
	if(s[1][0]==4)return o_win;
	if(s[0][1]==4)return x_win;
	if(s[1][1]==4)return o_win;
	if(flag)return 666;
	else return draw;
}
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		for(int i=0;i<4;i++)scanf("%s",c[i]);
		int t=check();
		printf("Case #%d: ",tt);
		if(t==x_win)printf("X won");
		else if(t==o_win)printf("O won");
		else if(t==draw)printf("Draw");
		else printf("Game has not completed");
		printf("\n");
	}
}
