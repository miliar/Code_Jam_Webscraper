
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
using namespace std;

vector<int> sum(vector<int> lhs, vector<int> rhs) {
	int dims = (int) lhs.size();
	vector<int> res(dims, 0);
	for (int i = 0; i < dims; ++i) {
		res[i] = lhs[i] + rhs[i];
	}
	return res;
}

vector<int> classify(char a, char b, char c, char d) {
	static int count[256];
	memset(count, 0, sizeof(count));
	vector<int> res(3, 0);
	char chars[] = {a, b, c, d};
	for (int i = 0; i < 4; ++i) {
		count[(int)chars[i]]++;
	}
	if (count['X'] == 4 || count['X'] == 3 && count['T'] == 1)
		++res[0];
	if (count['O'] == 4 || count['O'] == 3 && count['T'] == 1)
		++res[1];
	if (count['.'] > 0)
		++res[2];
	return res;
}


int main() {
	int tst;
	scanf("%d", &tst);
	for (int cas = 0; cas < tst; ++cas) {
		char board[8][8];
		int rows = 4;
		int cols = 4;
		for (int row = 0; row < rows; ++row)
			scanf("%s", board[row]);
		vector<int> total(3, 0);
		for (int row = 0; row < rows; ++row) {
			total = sum(total, classify(board[row][0], board[row][1], 
				board[row][2], board[row][3]));
		}
		for (int col = 0; col < cols; ++col) {
			total = sum(total, classify(board[0][col], board[1][col], 
				board[2][col], board[3][col]));
		}
		total = sum(total, classify(board[0][0], board[1][1], 
			board[2][2], board[3][3]));
		total = sum(total, classify(board[0][3], board[1][2], 
			board[2][1], board[3][0]));
		string outcome = "";
		if (total[0] > 0)
			outcome = "X won";
		else if (total[1] > 0)
			outcome = "O won";
		else if (total[2] > 0)
			outcome = "Game has not completed";
		else 
			outcome = "Draw";
		printf("Case #%d: %s\n", cas + 1, outcome.c_str());
	}
	return 0;
}