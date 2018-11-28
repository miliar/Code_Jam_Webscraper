#include<iostream>
bool flag[200][200];
int t,r,c;
bool istrue;
char map[100][100];
char ans[100][100];
using namespace std;
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin >> t;
	for (int l = 1 ; l <= t; ++l)
	{
		cin >> r  >> c;
		istrue  = true;
		memset(flag , true, sizeof(flag));
		for (int i = 0; i < r ; ++i)
		{
			scanf("%s", map[i]);
			for (int j = 0; j < c; ++j)
			{
				ans[i][j] = '.';
			}
			ans[i][c] = '\0';
		}
		for (int i = 0; i < r; ++i)
		for (int j = 0; j <c; ++j)
		{
			if (!flag[i][j])
				continue;
			if (map[i][j] == '.')
				continue;
			if (map[i][j] == '#' && map[i][j+1] == '#' && map[i+1][j] == '#' && map[i+1][j+1] == '#')
				{
					ans[i][j] = '/';
					ans[i][j+1] = '\\';
					ans[i+1][j] = '\\';
					ans[i+1][j+1] = '/';
					flag[i][j] = false;
					flag[i][j+1] = false;
					flag[i+1][j] = false;
					flag[i+1][j+1] = false;
				}	
			else
			{
				istrue = false;
				break;
			}
		}
		printf("Case #%d:\n",l);
		if (!istrue)
		{
			cout << "Impossible" << endl;
		}
		else
		{
			for (int i = 0; i < r; ++i)
			{
				printf("%s\n", ans[i]);
			}
		}
	}
	return 0;
}
