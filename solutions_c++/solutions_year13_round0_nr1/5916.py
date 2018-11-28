#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <cstring>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VII;
typedef vector<VS> VSS;

#define PB push_back

void check(const VS& board, char& win, bool& isdone) {
	for(int i=0; i<4; i++) {
		char head=(board[i][0]=='T')? board[i][1]:board[i][0];
		if (head=='.') {
			isdone=false;
			continue;
		}
		int count=0;
		for(int j=0; j<4; j++) {
			if(board[i][j]==head || board[i][j]=='T') count++;
			else if (board[i][j]=='.') isdone=false;
		}
		if(count==4) {
			win=head;
			return;
		}
	}
	
	for(int j=0; j<4; j++) {
		char head=(board[0][j]=='T')? board[1][j]:board[0][j];
		if (head=='.') {
			isdone=false;
			continue;
		}
		int count=0;
		for(int i=0; i<4; i++) {
			if(board[i][j]==head || board[i][j]=='T') count++;
			else if (board[i][j]=='.') isdone=false;
		}
		if(count==4) {
			win=head;
			return;
		}
	}
	
	char head=(board[0][0]=='T')? board[1][1]:board[0][0];
	if (head!='.') { 
	int count=0;
	for(int i=0; i<4; i++) {
		if (board[i][i]==head || board[i][i]=='T') count++;
		if (count==4) {
			win=head;
			return;
		}
	}
	} else isdone=false;
	
	head=(board[0][3]=='T')? board[1][2]:board[0][3];
	if(head!='.') {
	int count=0;
	for(int i=0; i<4; i++) {
		if(board[i][3-i]==head || board[i][3-i]=='T') count++;
		if (count==4) {
			win=head;
			return;
		}
	}
	} else isdone=false;
}

int main() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int n;
	string line;
	getline(fin, line);
	stringstream ss;
	ss << line;
	ss >> n;
	for(int i=1; i<=n; i++) {
		VS board;
		for(int j=1; j<=4; j++) {
			string line;
			getline(fin, line);
			board.PB(line);
		}
		getline(fin, line);
		char win='.';
		bool isdone=true;
		check(board, win, isdone);
		if (win!='.') {
			fout << "Case #" << i << ": " << win << " won" <<endl;
		} else if (isdone) {
			fout << "Case #" << i << ": " << "Draw" << endl;			
		} else fout << "Case #"<< i << ": "<<"Game has not completed"<< endl;
	} 
	fin.close();
	fout.close();
	return 0;
}

