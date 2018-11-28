#include <cstdio>
#include <cstdlib>

using namespace std;

char board[10][10];

bool ok(char player, char ch)
{
	return ch == 'T' or ch == player;
}

bool check(char player)
{
	for (int i = 0; i < 4; i++) if (ok(player, board[i][0]) and ok(player, board[i][1]) and ok(player, board[i][2]) and ok(player, board[i][3])) return true;
	for (int j = 0; j < 4; j++) if (ok(player, board[0][j]) and ok(player, board[1][j]) and ok(player, board[2][j]) and ok(player, board[3][j])) return true;
	if (ok(player, board[0][0]) and ok(player, board[1][1]) and ok(player, board[2][2]) and ok(player, board[3][3])) return true;
	if (ok(player, board[0][3]) and ok(player, board[1][2]) and ok(player, board[2][1]) and ok(player, board[3][0])) return true;
	
	return false;
}

int main()
{
//	freopen("A-large.in", "r", stdin);
//	freopen("out1_large.txt", "w", stdout);
	
	int T;
	scanf("%d", &T);
	
	for (int t = 1; t <= T; t++)
	{
		int blank = 0;
		
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++) {
				scanf(" %c", &board[i][j]);
				blank += (board[i][j] == '.');
			}
		
		printf("Case #%d: ", t);
		if (check('X')) printf("X won");
		else if (check('O')) printf("O won");
		else if (blank > 0) printf("Game has not completed");
		else printf("Draw");
		printf("\n");
	}
	
//	fclose(stdin);
//	fclose(stdout);
	
	return 0;
}
