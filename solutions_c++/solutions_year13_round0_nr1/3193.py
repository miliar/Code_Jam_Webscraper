#include <algorithm>
#include <iostream>
#include <fstream>
#include <set>

using namespace std;

char judge(set<char> cs) {
	if(cs.size() == 1 && *(cs.begin()) != '.') {
		return *(cs.begin());
	}
	else if(cs.size() == 2) {
		set<char>::iterator it = cs.find('T');
		if(it == cs.end()) {
			return 0;			
		}
		it = cs.find('O');
		if(it == cs.end()) {
			it = cs.find('.'); 
			if(it == cs.end()) {
				return 'X';
			}
		}
		else{
			return 'O';
		}
	}
	return 0;
}

int main() {
	int n; 
	ifstream inf("A-large.in");
	ofstream outf("A-large.out");

	inf>>n;

	for(int i=0; i < n ; i++) {
		char board[4][4];
		char winer = 0;
		bool hasEmpt = false;

		set<char> rcs[4];
		set<char> ccs[4];
		set<char> diag[2];

		for(int m=0; m<4; m++) {
			for(int n=0; n<4; n++) {
				inf>>board[m][n];
				rcs[m].insert(board[m][n]);
				ccs[n].insert(board[m][n]);
				if(board[m][n] == '.') {
					hasEmpt = true;
				}
			}
		}
		for(int j=0; j<4; j++) {
			diag[0].insert(board[j][j]);
			diag[1].insert(board[j][3-j]);
		}
		winer = judge(diag[0]);
		if(winer) {
			outf<<"Case #"<<i+1<<": "<<winer<<" won"<<endl;
			continue;
		}
		winer = judge(diag[1]);
		if(winer) {
			outf<<"Case #"<<i+1<<": "<<winer<<" won"<<endl;
			continue;
		}

		for(int j=0; j<4; j++) {
			winer = judge(rcs[j]);
			if(winer) break;
			winer = judge(ccs[j]);
			if(winer) break;
		}
		if(winer) {
			outf<<"Case #"<<i+1<<": "<<winer<<" won"<<endl;
			continue;
		}

		if(hasEmpt) {
			outf<<"Case #"<<i+1<<": Game has not completed"<<endl;
		}
		else {
			outf<<"Case #"<<i+1<<": Draw"<<endl;
		}
	}
	return 0;
}
