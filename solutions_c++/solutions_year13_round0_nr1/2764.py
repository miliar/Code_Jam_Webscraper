#include <cstdio>

using namespace std;

int ttt;
char a[11][11];

	inline bool win(char ch)
	{
		for (int i = 1; i<=4; i++)
			if (a[i][1] == a[i][2] && a[i][2] == a[i][3] && a[i][3] == a[i][4] && a[i][4] == ch) return true;
	        for (int j = 1; j<=4; j++)
	        	if (a[1][j] == a[2][j] && a[2][j] == a[3][j] && a[3][j] == a[4][j] && a[4][j] == ch) return true;
	        if (a[1][1] == a[2][2] && a[2][2] == a[3][3] && a[3][3] == a[4][4] && a[4][4] == ch) return true;
	        if (a[1][4] == a[2][3] && a[2][3] == a[3][2] && a[3][2] == a[4][1] && a[4][1] == ch) return true;
	        return false;
	}

int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.txt", "w", stdout);
	scanf("%d\n", &ttt);
	for (int it = 1; it<=ttt; it++)
	{
		printf("Case #%d: ", it);
		bool full = true;
		int t1, t2;
		t1 = t2 = 0;
		for (int i = 1; i<=4; i++)
		{
			for (int j = 1; j<=4; j++)
			{
				a[i][j] = getchar();
				if (a[i][j] == 'T') t1 = i, t2 = j;
				if (a[i][j] == '.') full = false;
			}
			getchar();
	        }
	        getchar();
	        a[t1][t2] = 'O';
	        if (win('O'))
	        {
	        	printf("O won\n");
	        	continue;
	        }
	        a[t1][t2] = 'X';
	        if (win('X')) 
	        {
	        	printf("X won\n");
	        	continue;
	        }
	        if (full) printf("Draw\n"); else printf("Game has not completed\n"); 
	}
	return 0;
}