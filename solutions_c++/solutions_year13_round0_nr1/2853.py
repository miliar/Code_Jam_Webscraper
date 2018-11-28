#include <iostream>
#include <vector>

using namespace std;

inline char checkVertical(vector<string>& board)
{
	char res = 0;
	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			const char cur = board[i][j];

			if (cur == '.') {
				res = 0;
				break;
			}
			if (cur == 'T') {
				continue;
			}
			if (cur != res && res == 0) {
				res = cur;
			}
			if (cur != res) {
				res = 0;
				break;
			}
		}
		if (res != 0)
			return res;
	}

	return 0;
}

inline char checkHorizontal(vector<string>& board)
{
	char res = 0;
	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			const char cur = board[j][i];

			if (cur == '.') {
				res = 0;
				break;
			}
			if (cur == 'T') {
				continue;
			}
			if (cur != res && res == 0) {
				res = cur;
			}
			if (cur != res) {
				res = 0;
				break;
			}
		}
		if (res != 0)
			return res;
	}

	return 0;
}

inline char checkDiagonal(vector<string>& board)
{
	char res = 0;
	for (int i = 0; i < 4; ++i) {
		const char cur = board[i][i];
		
		if (cur == '.') {
			res = 0;
			break;
		}
		if (cur == 'T') {
			continue;
		}
		if (cur != res && res == 0) {
			res = cur;
		}
		if (cur != res) {
			res = 0;
			break;
		}
	}
	if (res != 0)
		return res;

	for (int i = 0; i < 4; ++i) {
		const char cur = board[i][3 - i];
		
		if (cur == '.') {
			res = 0;
			break;
		}
		if (cur == 'T') {
			continue;
		}
		if (cur != res && res == 0) {
			res = cur;
		}
		if (cur != res) {
			res = 0;
			break;
		}
	}

	return res;
}

inline char checkDraw(vector<string>& board)
{
	for (int i = 0; i < 4; ++i) {
	for (int j = 0; j < 4; ++j) {
		if (board[i][j] == '.')
			return 0;
	}
	}
	return 'D';
}

inline char solve(vector<string>& board)
{
	char res = 0;
	if (res = checkVertical(board))
		return res;
	if (res = checkHorizontal(board))
		return res;
	if (res = checkDiagonal(board))
		return res;
	if (res = checkDraw(board))
		return res;

	return 0;
}

int main()
{
	int T = 0;
	cin>>T; 
	for (int i = 0; i < T; ++i) {
		vector<string> v;
		for (int j = 0; j < 4; ++j) {
			string s;
			cin>>s;
			v.push_back(s);
		}

		const char res = solve(v);

		cout<<"Case #"<<(i + 1)<<": ";

		switch (res) {
		case 0:  cout<<"Game has not completed"; break;
		case 'D':cout<<"Draw"; break;
		case 'O':
		case 'X': cout<<res<<" won"; break;
		}
		cout<<endl;
	}
	return 0;
}
