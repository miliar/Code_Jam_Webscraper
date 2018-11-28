#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <queue>
#include <stack>

using namespace std;

bool check(vector<string> &board, char ch)
{
	for (int i=0;i<board.size();i++) {
		bool flag = true;
		for (int j=0;j<board[i].size();j++) {
			if (board[i][j] != 'T' && board[i][j] != ch) {
				flag = false;
				break;
			}
		}
		if (flag) return true;
	}

	for (int i=0;i<board.size();i++) {
		bool flag = true;
		for (int j=0;j<board[i].size();j++) {
			if (board[j][i] != 'T' && board[j][i] != ch) {
				flag = false;
				break;
			}
		}
		if (flag) return true;
	}

	bool flag = true;
	for (int i=0;i<board.size();i++) {
		if (board[i][i] != 'T' && board[i][i] != ch) {
			flag = false;
			break;
		}
	}

	if (flag) return true;
	flag = true;
	for (int i=0;i<board.size();i++) {
		if (board[i][board.size()-i-1] != 'T' && board[i][board.size()-i-1] != ch) {
			flag = false;
			break;
		}
	}
	return flag;
}

int main()
{
	freopen("C:\\Projects\\gcj\\input.txt", "r", stdin);
	freopen("C:\\Projects\\gcj\\output.txt", "w", stdout);

	int z;
	cin >> z;
	for (int q=0;q<z;q++) {
		vector<string> board(4);
		for (int i=0;i<4;i++) {
			cin >> board[i];
		}

		bool xwon = false, owon = false, incomplete = false;
		for (int i=0;i<4;i++) {
			for (int j=0;j<4;j++) {
				if (board[i][j] == '.')
					incomplete = true;
			}
		}

		xwon = check(board, 'X');
		owon = check(board, 'O');

		cout << "Case #" << (q + 1) << ": ";

		if (xwon) cout << "X won" << endl;
		else if (owon) cout << "O won" << endl;
		else if (incomplete) cout << "Game has not completed" << endl;
		else cout << "Draw" << endl;
	}

	fclose(stdout);
	fclose(stdin);

	return 0;
}