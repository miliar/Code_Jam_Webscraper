#include <cstdio>

enum end_state_t {G_NC, G_DR, G_XW, G_OW};

const char *OUTPUTS[] = {
	"Game has not completed",
	"Draw",
	"X won",
	"O won"
};

const int mr[][4] = {
	{0, 0, 0, 0}, // rows
	{1, 1, 1, 1},
	{2, 2, 2, 2},
	{3, 3, 3, 3},
	{0, 1, 2, 3}, // columns
	{0, 1, 2, 3},
	{0, 1, 2, 3},
	{0, 1, 2, 3},
	{0, 1, 2, 3}, // diagonals
	{0, 1, 2, 3}
};
const int mc[][4] = {
	{0, 1, 2, 3}, // rows
	{0, 1, 2, 3},
	{0, 1, 2, 3},
	{0, 1, 2, 3},
	{0, 0, 0, 0}, // columns
	{1, 1, 1, 1},
	{2, 2, 2, 2},
	{3, 3, 3, 3},
	{0, 1, 2, 3}, // diagonals
	{3, 2, 1, 0}
};

end_state_t solve(const char board[4][5])
{
	end_state_t result = G_NC;

	int nx, no, nt;
	for(int i = 0; i < 10; ++i) {
		nx = no = nt = 0;
		for(int j = 0; j < 4; ++j) {
			switch(board[mr[i][j]][mc[i][j]]) {
				case 'X':
					++nx;
					break;
				case 'O':
					++no;
					break;
				case 'T':
					++nt;
			}
		}

		if((nx + nt) == 4) result = G_XW;
		if((no + nt) == 4) result = G_OW;
	}

	int total_filled = 0;
	for(int i = 0; i < 4; ++i) {
		for(int j = 0; j < 4; ++j) {
			if(board[i][j] != '.') total_filled++;
		}
	}

	if(total_filled == 16 && result == G_NC) result = G_DR;

	return result;
}

int main(int argc, char **argv)
{
	int T;
	char board[4][5];

	scanf("%d\n", &T);
	for(int i = 1; i <= T; ++i) {
		for(int j = 0; j < 4; ++j) {
			scanf("%s\n", &board[j][0]);
		}
		scanf("\n");

		end_state_t out = solve(board);
		printf("Case #%d: %s\n", i, OUTPUTS[out]);
	}

	return 0;
}
