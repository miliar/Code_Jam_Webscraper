#include <iostream>
#include <vector>
#include <algorithm>
#include <cctype>
#include <ctime>
#include <set>
#include <map>
using namespace std;
int check (vector < vector <char> > arr,int p, int q, char c) {
	int cou = 0;
	for (int i = 0; i < 4; i++) {
		if (arr[i][q] == c || arr[i][q] == 'T') {
			cou++;
			if (cou == 4)
				return cou;
		}
		else
			break;
	}
	cou = 0;
	for (int i = 0; i < 4; i++) {
		if (arr[p][i] == c || arr[p][i] == 'T') {
			cou++;
			if (cou == 4)
				return cou;
		}
		else
			break;
	}
	cou = 0;
	if (p == q) {
		if ((arr[0][0] == c || arr[0][0] == 'T') && (arr[1][1] == c || arr[1][1] == 'T') && (arr[2][2] == c || arr[2][2] == 'T') && (arr[3][3] == c || arr[3][3] == 'T')) {
			cou = 4;
			return cou;
		}
	}
	if ((p == 1 && q==2) || (p==2 && q==1) || (p==3 && q==0) || (p==0 && q==3)) {
		if ((arr[3][0] == c || arr[3][0] == 'T') && (arr[2][1] == c || arr[2][1] == 'T') && (arr[1][2] == c || arr[1][2] == 'T') && (arr[0][3] == c || arr[0][3] == 'T')) {
			cou = 4;
			return cou;
		}
	}
	return 0;
}

int main () {
	int t;
	cin >> t;
	for (int y = 1; y <= t; y++) {
		int empty = 0;
		int ans_x = 0;
		int ans_o = 0;
		char ch;
		vector < vector <char> > arr (4,vector <char> (4,'c'));
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> ch;
				arr[i][j] = ch;
			}
		}
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (arr[i][j] == '.') {
					empty = 1;
				}
			//if (emp == 1)
				//break;
			if (arr[i][j] == 'X') 
				ans_x = check (arr,i,j,arr[i][j]);
			if (arr[i][j] == 'O')
				ans_o = check (arr,i,j,arr[i][j]);
			}
			if (ans_x == 4 || ans_o == 4)
				break;
			//if (emp == 1)
				//break;
		}
		if (ans_x == 4)
			cout <<"Case #"<<y<<": "<< "X won" << endl;
		if (ans_o == 4)
			cout <<"Case #"<<y<<": "<< "O won" << endl;
		if (ans_x != 4 && ans_o != 4) {
			if (empty == 1) {
				cout <<"Case #"<<y<<": "<<"Game has not completed" << endl;
			}
		}
		if (ans_x != 4 && ans_o != 4) {
			if (empty == 0) {
				cout <<"Case #"<<y<<": "<< "Draw" << endl;
			}
		}

	}
	return 0;
}

