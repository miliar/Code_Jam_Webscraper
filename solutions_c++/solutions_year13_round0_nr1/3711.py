// Tic-Tac-Toe-Tomek.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
using namespace std;

string judge(vector<string> &);
bool sb_win(string &, string &, bool &);
int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("d:\\A-large.in");
	ofstream out("d:\\A-large.out");
	int number_of_test_cases = 0;
	vector<vector<string>> boards;

	if(!in) {
		return 0;
	}
	//收集input文件中的数据
	in >> number_of_test_cases;
	for(int i=0;i<number_of_test_cases;i++) {
		vector<string> board;
		for(int j=0;j<4;j++) {
			string line;
			in >> line;
			board.push_back(line);
		}
		boards.push_back(board);
	}

	int serial_number = 1;
	for(vector<vector<string>>::iterator iter=boards.begin(); iter!=boards.end(); ++iter) {
		vector<string> board = *iter;
		/* 判断这一局的胜负 */
		out << "Case #" << serial_number++ << ": " << judge(board) << endl;
	}


	return 0;
}

string judge(vector<string> &board) {
	bool not_full = false;
	//横向比较
	for(vector<string>::iterator iter=board.begin(); iter!=board.end(); ++iter) {
		string line = *iter;
		string winner;
		if(sb_win(line, winner, not_full)) {
			return winner + " won";
		}
	}

	//纵向比较
	for(int i=0; i<4; ++i) {  //i代表列
		string column;
		for(vector<string>::iterator iter=board.begin(); iter!=board.end(); ++iter) {
			string line = *iter;
			column += line[i];
		}
		string winner;
		if(sb_win(column, winner, not_full)) {
			return winner + " won";
		}
	}

	string winner;
	//主对角线
	string main_diagonal;
	for(int i=0; i<4; ++i) {  //i代表列
		main_diagonal += board[i][i];
	}
	if(sb_win(main_diagonal, winner, not_full)) {
		return winner + " won";
	}

	//副对角线
	string vice_diagonal;
	for(int i=0; i<4; ++i) {
		vice_diagonal += board[i][3-i];
	}
	if(sb_win(vice_diagonal, winner, not_full)) {
		return winner + " won";
	}
	
	if(not_full == false) {
		//之前的循环未遇到'.',重新完整的扫描一遍，以确定是平局还是游戏未结束
		for(int i=0; i<4; ++i) {
			for(int j=0; j<4; ++j) {
				if(board[i][j] == '.') {
					return "Game has not completed";
				}
			}
		}
		return "Draw";
	} else {
		//之前的循环有遇到'.',说明游戏未结束
		return "Game has not completed";
	}
}

//有胜出者返回true，无法判断返回false
bool sb_win(string &line, string &winner, bool &not_full) {
	string potential_winner;//只会取'O'和'X'两种值
	for(string::size_type ix=0; ix!=line.size(); ++ix) {
		bool need_continue = true;
		switch(line[ix]) {
			case 'T':
				break;
			case 'O': 
			case 'X':
				if(potential_winner.empty()) {
					potential_winner = line[ix];
				} else {
					if(potential_winner[0] != line[ix]) {
						need_continue = false;
					}
				}
				break;
			case '.':
				if(not_full == false) {
					not_full = true;
				}
				need_continue = false;
				break;
		}
		//如果有出现胜负的可能性，则循环会继续，否则跳出循环
		if(!need_continue)
			break;
		if(ix == line.size() - 1) {
			//最后一次迭代，走到这一步说明有胜出者了
			winner = potential_winner;
			return true;
		}
	}
	return false;
}