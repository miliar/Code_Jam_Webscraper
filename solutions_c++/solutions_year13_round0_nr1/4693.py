#include<iostream>
#include<string>
using namespace std;

int check_won(string str){
	if (str == "XXXX" || str == "XXXT" || str == "XXTX" || str == "XTXX" || str == "TXXX")
		return 1;
	else if (str == "OOOO" || str == "OOOT" || str == "OOTO" || str == "OTOO" || str == "TOOO")
		return 2;
	else return 3;
}

int main(){
	int t, j, k, T, not_completed = 0, progress = 1, fg = 0;
	char ch;
	char board[4][4];
	cin >> t;
	string str, s;
	for (T = 1; T <= t; T++){
		not_completed = 0, progress = 1;
		for (j = 0; j < 4; j++){
			for (k = 0; k < 4; k++){
				cin >> ch;
				board[j][k] = ch;
				if (ch == '.')
					not_completed = 1;
			}
		}
		for (j = 0; j < 4; j++){
			str = "";
			for (k = 0; k < 4; k++){
				str = str + board[j][k];
			}
			fg = check_won(str);
			if (fg == 1){
				cout << "Case #" << T << ": X won" << "\n";
				progress = 0;
				break;
			}
			else if (fg == 2){
				cout << "Case #" << T << ": O won" << "\n";
				progress = 0;
				break;
			}else
				progress = 1;
		}
		if (progress == 1){
			for (j = 0; j < 4; j++){
				str = "";
				for (k = 0; k < 4; k++){
					str = str + board[k][j];
				}
				fg = check_won(str);
				if (fg == 1){
					cout << "Case #" << T << ": X won" << "\n";
					progress = 0;
					break;
				}
				else if (fg == 2){
					cout << "Case #" << T << ": O won" << "\n";
					progress = 0;
					break;
				}else
					progress = 1;
			}
		}
		if (progress == 1){
			str = "";
			for (j = 0; j < 4; j++)
				str = str + board[j][j];
			fg = check_won(str);
			if (fg == 1){
				cout << "Case #" << T << ": X won" << "\n";
				progress = 0;
			}
			else if (fg == 2){
				cout << "Case #" << T << ": O won" << "\n";
				progress = 0;
			}else
				progress = 1;
		}
		if (progress == 1){
			str = "";
			for (j = 0; j < 4; j++)
				str = str + board[j][3-j];
			fg = check_won(str);
			if (fg == 1){
				cout << "Case #" << T << ": X won" << "\n";
				progress = 0;
			}
			else if (fg == 2){
				cout << "Case #" << T << ": O won" << "\n";
				progress = 0;
			}else
				progress = 1;
		}
		if (progress == 1){
			if (not_completed == 0){
				cout << "Case #" << T << ": Draw" << "\n";
			}else{
				cout << "Case #" << T << ": Game has not completed" << "\n";
			}
		}
	}
	return 0;
}
