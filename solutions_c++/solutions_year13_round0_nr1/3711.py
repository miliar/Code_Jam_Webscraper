// Tic-Tac-Toe-Tomek.cpp : �������̨Ӧ�ó������ڵ㡣
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
	//�ռ�input�ļ��е�����
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
		/* �ж���һ�ֵ�ʤ�� */
		out << "Case #" << serial_number++ << ": " << judge(board) << endl;
	}


	return 0;
}

string judge(vector<string> &board) {
	bool not_full = false;
	//����Ƚ�
	for(vector<string>::iterator iter=board.begin(); iter!=board.end(); ++iter) {
		string line = *iter;
		string winner;
		if(sb_win(line, winner, not_full)) {
			return winner + " won";
		}
	}

	//����Ƚ�
	for(int i=0; i<4; ++i) {  //i������
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
	//���Խ���
	string main_diagonal;
	for(int i=0; i<4; ++i) {  //i������
		main_diagonal += board[i][i];
	}
	if(sb_win(main_diagonal, winner, not_full)) {
		return winner + " won";
	}

	//���Խ���
	string vice_diagonal;
	for(int i=0; i<4; ++i) {
		vice_diagonal += board[i][3-i];
	}
	if(sb_win(vice_diagonal, winner, not_full)) {
		return winner + " won";
	}
	
	if(not_full == false) {
		//֮ǰ��ѭ��δ����'.',����������ɨ��һ�飬��ȷ����ƽ�ֻ�����Ϸδ����
		for(int i=0; i<4; ++i) {
			for(int j=0; j<4; ++j) {
				if(board[i][j] == '.') {
					return "Game has not completed";
				}
			}
		}
		return "Draw";
	} else {
		//֮ǰ��ѭ��������'.',˵����Ϸδ����
		return "Game has not completed";
	}
}

//��ʤ���߷���true���޷��жϷ���false
bool sb_win(string &line, string &winner, bool &not_full) {
	string potential_winner;//ֻ��ȡ'O'��'X'����ֵ
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
		//����г���ʤ���Ŀ����ԣ���ѭ�����������������ѭ��
		if(!need_continue)
			break;
		if(ix == line.size() - 1) {
			//���һ�ε������ߵ���һ��˵����ʤ������
			winner = potential_winner;
			return true;
		}
	}
	return false;
}