#include<iostream>
using namespace std;
#include<algorithm>
#include<queue>
#include<stack>
#include<functional>
#include<string>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<math.h>
#include<vector>
#include<deque>
#include<list>
#include<set>
#include<map>
int R, C;
char board[60][60];
int main() {


	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int T;
	cin >> T;
	++T;
	int kase = 0;
	while( --T ) {
		cin >> R >> C;
		for(int i = 0 ; i < R; ++i)
			for(int j = 0 ; j < C; ++j)
				cin >> board[i][j];
		for(int i = 0 ; i < R - 1; ++i)
			for(int j = 0 ; j < C - 1; ++j) {
				if( board[i][j] == board[i+1][j] && board[i][j] == board[i][j+1] && board[i][j] == board[i+1][j+1] && board[i][j] == '#' ) {
					board[i][j] = '/';
					board[i][j+1] = '\\';
					board[i+1][j] = '\\';
					board[i+1][j+1] = '/'; 
				}
			}
			bool imp = 0;
			for(int i = 0 ; i < R; ++i) {
				for(int j = 0 ; j < C; ++j)
					if( board[i][j] == '#' ) {
						imp = true;
					}
					if( imp )
						break;
			}
			if( imp ) {
				cout << "Case #" << ++kase << ":\nImpossible" << endl;
			} else {
				cout << "Case #" << ++kase << ":" << endl;
				for(int i = 0 ; i < R; ++i) {
					for(int j = 0 ; j < C; ++j)
						cout << board[i][j];
					cout << endl;
				}
				

			}
	}
	return 0;

}