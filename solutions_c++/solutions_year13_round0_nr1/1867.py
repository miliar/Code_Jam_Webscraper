#include <cstdio>
#include <cstring>

using namespace std;

int boo, n;
char a[4][4];

bool foo(int q, int w, int e, int r)
{
	int x = 0, y = 0, z = 0;
	if (q == 'X')
		x++;
	if (q == 'O')
		y++;
	if (q == 'T')
		z++;
	if (w == 'X')
		x++;
	if (w == 'O')
		y++;
	if (w == 'T')
		z++;	
	if (e == 'X')
		x++;
	if (e == 'O')
		y++;
	if (e == 'T')
		z++;
	if (r == 'X')
		x++;
	if (r == 'O')
		y++;
	if (r == 'T')
		z++;
	if (x + z == 4)
	{
		printf("X won\n");
		return 1;
	}
	if (y + z == 4)
	{
		printf("O won\n");
		return 1;
	}
	return 0;
}
int main()
{
	freopen("tic-tac-toe.in", "r", stdin);
	freopen("tic-tac-toe.out", "w", stdout);
	scanf("%d\n", &n);
	for (int i = 0; i < n; i++)
	{
		boo = 0;
		printf("Case #%d: ", i + 1);  
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
				scanf("%c", &a[j][k]);
			scanf("\n");
		} 
		scanf("\n");
		for (int j = 0; j < 4; j++)
			if (foo(a[j][0], a[j][1], a[j][2], a[j][3]))
			{
			    boo = 1;
				break;		
			}
		if (boo)
			continue;

		for (int j = 0; j < 4; j++)
			if (foo(a[0][j], a[1][j], a[2][j], a[3][j]))
			{
				boo = 1;
				break;
			}		
		if (boo)
			continue;
		if (foo(a[0][0], a[1][1], a[2][2], a[3][3]))
			continue;
		if (foo(a[0][3], a[1][2], a[2][1], a[3][0]))
			continue;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
			{
				if (a[j][k] == '.')
					boo = 1;
			}	
		if (!boo)
			printf("Draw\n");
		else	
			printf("Game has not completed\n");
	}
}