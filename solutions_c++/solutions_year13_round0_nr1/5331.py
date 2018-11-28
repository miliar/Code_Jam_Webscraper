#include <iostream>
#include <cstdio>

using namespace std;

#define forsn(i,s,n) for(int i = (s);i < (int)(n);i++)
#define forn(i,n) forsn(i,0,n)

char board[4][4];

int main() {
	freopen("tttlarge.in","r",stdin);
	freopen("tttlarge.out","w",stdout);
	int T;
	cin >> T;
	forn(caso, T) {
		scanf("\n");
		forn(i,4) {
			forn(j, 4) {
				scanf("%c",&board[i][j]);
			}
			scanf("\n");
		}
		cout << "Case #" << caso + 1 << ": ";
		bool completed = true;
		forn(i,4) forn(j,4) if (board[i][j] == '.') completed = false;
		bool xwon = false;
		bool ywon = false;
		forn(row, 4) {
			bool xwonrow = true;
			bool ywonrow = true;
			forn(col, 4) {
				xwonrow = xwonrow && !(board[row][col] == 'O' || board[row][col] == '.');
				ywonrow = ywonrow && !(board[row][col] == 'X' || board[row][col] == '.');
			}
			xwon = xwon || xwonrow;
			ywon = ywon || ywonrow;
		}
		forn(col, 4) {
			bool xwonrow = true;
			bool ywonrow = true;
			forn(row, 4) {
				xwonrow = xwonrow && !(board[row][col] == 'O' || board[row][col] == '.');
				ywonrow = ywonrow && !(board[row][col] == 'X' || board[row][col] == '.');
			}
			xwon = xwon || xwonrow;
			ywon = ywon || ywonrow;
		}
		bool xwondiag1 = true;
		bool xwondiag2 = true;
		bool ywondiag1 = true;
		bool ywondiag2 = true;
		forn(diag, 4) {
			xwondiag1 = xwondiag1 && !(board[diag][diag] == 'O' || board[diag][diag] == '.');
			xwondiag2 = xwondiag2 && !(board[diag][3 - diag] == 'O' || board[diag][3 - diag] == '.');
			ywondiag1 = ywondiag1 && !(board[diag][diag] == 'X' || board[diag][diag] == '.');
			ywondiag2 = ywondiag2 && !(board[diag][3 - diag] == 'X' || board[diag][3 - diag] == '.');
		}
		xwon = xwon || xwondiag1;
		xwon = xwon || xwondiag2;
		ywon = ywon || ywondiag1;
		ywon = ywon || ywondiag2;
		if (xwon && !ywon) cout << "X won" << endl;
		if (!xwon && ywon) cout << "O won" << endl;
		if (!(xwon ^ ywon) && !completed) cout << "Game has not completed" << endl;
		if (!xwon && !ywon && completed) cout << "Draw" << endl;
	}
}
