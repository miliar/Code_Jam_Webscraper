#include <iostream>
using namespace std;

char map[50][50];
int n, k;

int dirx[4] = {0, 1, 1, 1};
int diry[4] = {-1, -1, 0, 1};

bool isOK(int x, int y)
{
	return (x >=0 && x < n && y >=0 && y < n);

}
char *solve()
{
	bool red, blue;
	int i, j, kk;
	int x, y;
	int num;
	char c;
	for(i = 0; i < n; i++)
	{
		kk = n - 1;
		for(j = n-1; j >=0; j--)
		{
			if(map[i][j] != '.')
			{
				map[i][kk] = map[i][j];
				if(j != kk)
					map[i][j] = '.';
				kk--;
			}
		}
	}

	red = false;
	blue = false;
	for(i = 0; i < n; i++)
	{
		for(j = n-1; j >=0; j--)
		{
			if(map[i][j] == '.')
				continue;
			c = map[i][j];
			for(kk = 0; kk < 4; kk++)
			{
				x = i + dirx[kk];
				y = j + diry[kk];
				num = 1;
				while(isOK(x,y) && map[x][y] == c)
				{
					num++;
					x += dirx[kk];
					y += diry[kk];
				}
				if(num >= k)
				{
					if(c == 'R')
						red = true;
					else
						blue = true;
				}
			}
		}
	}

	if(red)
	{
		if(blue)
			return "Both";
		return "Red";
	}
	if(blue)
		return "Blue";

	return "Neither";

}

int main()
{

	int i, j;
	int case_num;
	int t;
	cin>>t;
	for(case_num = 1; case_num <= t; case_num++)
	{
		cin>>n>>k;
		for(i = 0; i < n; i++)
		{
			cin>>map[i];
		}

		printf("Case #%d: %s\n", case_num, solve());

	}
	return 0;
}