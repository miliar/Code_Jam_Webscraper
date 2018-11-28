#include<algorithm>
#include<cassert>
#include<cctype>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<deque>
#include<iostream>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<string>
#include<sstream>
#include<vector>
using namespace std;

typedef long long LL;
typedef long double LD;

#define dprintf(...) fprintf(stderr, __VA_ARGS__)

int cond = 1;
#define DB(X) {if(cond){cerr<<"Line:"<<__LINE__<<", "<<#X<<" = "<<X<<endl;}}
int main() {
	int t; cin >> t;
	string res[4] = {"X won\n", "O won\n", "Draw\n", "Game has not completed\n"};
	set<string> xw; xw.insert("XXXX"); xw.insert("XXXT"); xw.insert("XXTX"); xw.insert("XTXX"); xw.insert("TXXX");
	set<string> ow; ow.insert("OOOO"); ow.insert("OOOT"); ow.insert("OOTO"); ow.insert("OTOO"); ow.insert("TOOO");

	for(int i = 1; i <= t; ++i){
		string board[4], dummy;
		getline(cin, dummy);
		int r = 2;
		for(int j = 0; j < 4; ++j) {
			getline(cin, board[j]);
			if (r == 2) {
				for(int k = 0; k < 4; ++k)
					if (board[j][k] == '.') r = 3;
			}
		}
		vector<string> pos;
		for(int j = 0; j < 4; ++j) {
			pos.push_back(board[j]);
			stringstream ss; ss << board[0][j] << board[1][j] << board[2][j] << board[3][j];
			pos.push_back(ss.str());
		}
		string d1 = "", d2 = "";
		for(int j = 0; j < 4; ++j) {
			d1 += board[j][j];
			d2 += board[j][3 - j];
		}
		//cout << ": "<< board[0] <<  " " << d1 << " " << d2 << endl;
		pos.push_back(d1); pos.push_back(d2);
		for(int j = 0; j < pos.size(); ++j) {
			if (xw.find(pos[j]) != xw.end()) r = 0;
			if (ow.find(pos[j]) != ow.end()) r = 1;
			if (r < 2) break;
		}
		cout << "Case #" << i << ": " << res[r];
	}
	return 0;
}
