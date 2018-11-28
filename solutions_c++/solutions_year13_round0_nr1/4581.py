#include <cstdio>

const int EMPTY = -50;
const char* OUTPUT_STRING = "Case #%d: %s\n";

const char* X_WON = "X won";
const char* O_WON = "O won";
const char* DRAW = "Draw";
const char* UNDECIDED = "Game has not completed";

using namespace std;

int convert(char c) {
	switch(c) {
		case 'X':
			return 1;
		case 'O': 
			return -1;
		case '.':
			return EMPTY;
		case 'T':
			return 0;
	}
}


void testcase(int T) {
	int board[4][4];	
	int top[5];
	int right[5];

	char line[5];
	for(int x = 0; x < 4;x++)
		for(int y = 0; y < 4; y++) 
			board[x][y] = EMPTY;

	for(int x = 0; x < 5; x++) top[x] = right[x] = 0;

	int dotcount = 0;

	for(int x = 0; x < 4; x++) {
		scanf("%s", line);
		for(int y = 0; y < 4; y++) {
			int val =  convert(line[y]);
			if (val == EMPTY) dotcount++;
			board[x][y] = val;
			top[y] += val;
			right[x] += val;
		}
	}
	bool x_won = false;
	bool o_won = false;
	
	for (int x = 0; x < 4; x++) {
		top[4] += board[3-x][x];
		right[4] += board[x][x];
	}

	

	for(int x = 0; x < 5; x++) {
		if (top[x] == 3 || top[x] == 4) x_won = true;
		if (top[x] == -3 || top[x] == -4) o_won = true;

		if (right[x] == 3 || right[x] == 4) x_won = true;
		if (right[x] == -3 || right[x] == -4) o_won = true;

//		printf("TOP[%d] = %d\n", x, top[x]);
//		printf("RIGHT[%d] = %d\n", x, right[x]);
	}

	if (x_won && o_won) {
		printf(OUTPUT_STRING, T, DRAW);
		return;
	}

	if (!x_won && !o_won) {
		if (dotcount > 0)
			printf(OUTPUT_STRING, T, UNDECIDED);
		else
			printf(OUTPUT_STRING, T, DRAW);
			
		return;
	}

	if (x_won) {
		printf(OUTPUT_STRING, T, X_WON);
		return;
	}

	if(o_won) {
		printf(OUTPUT_STRING, T, O_WON);
		return;
	}

}


int main() {
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; i++){
		testcase(i);
	}
	return 0;
}

