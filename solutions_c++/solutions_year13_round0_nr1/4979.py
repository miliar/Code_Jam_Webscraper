#include "std.h"
#include <string.h>

int mat[4][4];
char buf[1024];

int main() {
    int T;
    cin >> T; cin.getline(buf, sizeof buf);
    FOR(tt, T) {
	//	DBG(1, V(tt));
	ZERO(mat);
	int full = 1;
	FOR(i, 4)
	{
	    string s;
	    cin >> s;
	    FOR(j, 4) {
		char c = s[j];
		switch(c) {
		case '.': full = c = 0; break;
		case 'X': c = 1; break;
		case 'O': c = 2; break;
		case 'T': c = 3; break;
		}
		mat[i][j] = c;
	    }
	}

	cout << "Case #"<<(tt+1)<<": ";

	int m = 3;
	FOR(i, 4) m &= mat[i][i];
	if (m & 1) goto x;
	if (m & 2) goto o;
	m = 3;
	FOR(i, 4) m &= mat[i][3-i];
	if (m & 1) goto x;
	if (m & 2) goto o;
	FOR(i, 4) {
	    m = 3;
	    FOR(j, 4) m &= mat[i][j];
	    if (m & 1) goto x;
	    if (m & 2) goto o;
	    m = 3;
	    FOR(j, 4) m &= mat[j][i];
	    if (m & 1) goto x;
	    if (m & 2) goto o;
	}
	cout << (full ? "Draw" : "Game has not completed"); goto end;
    x:  cout << "X won"; goto end;
    o:  cout << "O won"; goto end;

    end:
	cout << endl;
    }
    return 0;
}
