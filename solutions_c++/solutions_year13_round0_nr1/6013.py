#include<iostream>
using namespace std;

class ticTac {
private:
	char board[4][4];
	bool incomplete;
public:
	ticTac() {
		incomplete = false;
	}
	void input();
	void solve(int);
	bool checkRow(char);
	bool checkCol(char);
	bool checkDia(char);
};

bool ticTac::checkRow(char val) {
	bool flag = false;
	int j;
	for (int i = 0; i < 4; i++) {
		for (j = 0; j < 4; j++) {
			if (board[i][j] != val && board[i][j] != 'T') {
				flag = false;
				break;
			} else
				flag = true;
		}
		if (flag)
			return true;
	}
	return false;
}
bool ticTac::checkCol(char val) {
	bool flag = false;
	int j;
	for (int i = 0; i < 4; i++) {
		for (j = 0; j < 4; j++) {
			if (board[j][i] != val && board[j][i] != 'T') {
				flag = false;
				break;
			} else
				flag = true;
		}
		if (flag)
			return true;
	}
	return false;
}

bool ticTac::checkDia(char val) {
	int k = 0, i = 0, j = 0;
	bool flag = true;
	while (k < 4) {
		if (board[i][j] != val && board[i][j] != 'T') {
			flag = false;
			break;
		}
		i++;
		j++;
		k++;
	}
	if (flag)
		return true;
	flag = true;
	i = 0;
	j = 3;
	k = 0;
	while (k < 4) {
		if (board[i][j] != val && board[i][j] != 'T') {
			flag = false;
			break;
		}
		i++;
		j--;
		k++;
	}
	if (flag)
		return true;

	return false;
}

void ticTac::solve(int i) {

	if (checkRow('X'))
		cout << "Case #"<<i<<": X won"<<endl;
	else if (checkRow('O'))
		cout << "Case #"<<i<<": O won"<<endl;
	else if (checkCol('X'))
		cout << "Case #"<<i<<": X won"<<endl;
	else if (checkCol('O'))
		cout << "Case #"<<i<<": O won"<<endl;
	else if (checkDia('X'))
		cout << "Case #"<<i<<": X won"<<endl;
	else if (checkDia('O'))
		cout << "Case #"<<i<<": O won"<<endl;
	else if (incomplete)
		cout << "Case #"<<i<<": Game has not completed"<<endl;
	else
		cout << "Case #"<<i<<": Draw"<<endl;

	//checkCol();
}

void ticTac::input() {
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			cin >> board[i][j];
			if (board[i][j] == '.')
				incomplete = true;
		}
	}

}

int main() {
	int noOfInput;
	char input[16];

	cin >> noOfInput;
	int x = noOfInput;
	for (int i = 0; i < x; i++) {
		ticTac obj;
		obj.input();
		obj.solve(i + 1);
	}

	return 0;
}

