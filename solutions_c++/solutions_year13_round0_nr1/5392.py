# include <iostream>
# include <cstdio>
using namespace std;
char map[5][5];
bool win(int x, int y)
{
	int i, count1, e1, count2, e2, count3, e3;
	count1=e1=count2=e2=count3=e3=0;
	for (i = 1; i<=4; i++)
	{
		if (map[x][i]==map[x][y])
			count1++;
		if (map[i][y]==map[x][y])
			count2++;
		if (map[x][i]=='T')
			e1++;
		if (map[i][y]=='T')
			e2++;
	}
	if (x==1&&y==1)
	{
		for (i = 1; i<=4; i++)
		{
			if (map[i][i]==map[x][y])
				count3++;
			if (map[i][i]=='T')
				e3++;
		}
	}
	if (x==1&&y==4)
	{
		for (i = 4; i>=1; i--)
		{
			if (map[i][5-i]==map[x][y])
				count3++;
			if (map[i][5-i]=='T')
				e3++;
		}
	}
	if ((count1+e1)==4||(count2+e2)==4||(count3+e3)==4)
		return true;
	else
		return false;
}
int main()
{
	int n, i, j, flag, flag2, N;
//	freopen("A-small-attempt2.in", "r", stdin);
//	freopen("x.out", "w", stdout);
	cin>>n;
	N=1;
	while (n--)
	{
		flag = 0, flag2 = 0;
		for (i = 1; i<5; i++)
		{
			for (j = 1; j<5; j++)
				cin>>map[i][j];
		}
		for (i = 1; i<5; i++)
		{
			for (j = 1; j<5; j++)
			{
				if (map[i][j]=='.')
				{
					flag2=1;
					continue;
				}
				if (win(i, j))
				{
					flag=1;
					break;
				}
		//		cout<<map[i][j];
			}
		//	cout<<endl;
			if (flag)break;
		}
		if (flag)
			printf("Case #%d: %c won\n", N++, map[i][j]);
		else if (flag2)
			printf("Case #%d: Game has not completed\n", N++);
		else
			printf("Case #%d: Draw\n", N++);
	}
	return 0;
}
