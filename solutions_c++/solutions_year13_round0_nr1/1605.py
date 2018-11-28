#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <map>

#define fii(x,y) for(int i=x;i<y;i++)
#define fjj(x,y) for(int j=x;j<y;j++)
#define fkk(x,y) for(int k=x;k<y;k++)
#define fi(x) fii(0,x)
#define fj(x) fjj(0,x)
#define fk(x) fkk(0,x)
#define eps 0.0000000001
#define inf 1<<28

using namespace std;

int main() {
	int T, tc;

	cin >> T;

	for(tc=1;tc<=T;tc++) {
		bool complete = true;
		bool x_won, o_won;
		char board[10][4];
		char t;

		fi(4) {
			fj(4) {
				cin >> t;

				if(t == '.') {
					complete = false;
				}

				board[i][j] = t;
				board[j+4][i] = t;
			}
		}

		fi(4) {
			board[8][i] = board[i][i];
		}

		fi(4) {
			board[9][i] = board[i][3-i];
		}

		/*fi(10) {
			fj(4) {
				cout << board[i][j];
			}

			cout << endl;
		}*/

		fi(10) {
			x_won = true;
			o_won = true;

			fj(4) {
				if(board[i][j] == 'O' || board[i][j] == '.') {
					x_won = false;
				}

				if(board[i][j] == 'X' || board[i][j] == '.') {
					o_won = false;
				}

				if(!x_won && !o_won) {
					break;
				}
			}

			if(x_won || o_won) {
				break;
			}
		}

		if(x_won) {
			cout << "Case #" << tc << ": X won" << endl;
		} else if(o_won) {
			cout << "Case #" << tc << ": O won" << endl;
		} else if(complete) {
			cout << "Case #" << tc << ": Draw" << endl;
		} else {
			cout << "Case #" << tc << ": Game has not completed" << endl;
		}
	}
}
