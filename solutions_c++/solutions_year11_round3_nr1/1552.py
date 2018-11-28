#include <cstdio>
#include <cstdlib>
#include <algorithm>


using namespace std;

char field[52][52];

int main()
{
	int r, c, T;
	freopen("out.txt", "w", stdout);
	freopen("11.in", "r", stdin);
	scanf("%d", &T);
	for(int t = 0; t < T; t++)
	{
		bool normal = true;
		scanf("%d%d", &r, &c);
		for(int i = 0; i < r; i++)
		{
			scanf("%s", &field[i]);
		}
		for(int i = 0; i < r - 1; i++)
			for(int j = 0; j < c - 1; j++)
				if(field[i][j] == '#' && field[i][j+1] == '#' && field[i+1][j] == '#' && field[i+1][j+1] == '#')
				{
					field[i][j] = '/';
					field[i][j+1] = '\\';
					field[i+1][j] = '\\';
					field[i+1][j+1] = '/';
				}
		for(int i = 0; i < r; i++)
			for(int j = 0; j < c; j++)
				if(field[i][j] == '#')
					normal = false;
		if(!normal)
			printf("Case #%d:\nImpossible\n", t+1);
		else
		{
			printf("Case #%d:\n", t+1);
			for(int i = 0; i < r; i++)
				printf("%s\n", field[i]);

		}
	}
	return 0;
}
