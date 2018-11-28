#include <iostream>
#include <string>
#include <vector>

using namespace std;
char A[5][5];

int main()
{
    int T;
    cin >> T;
    for (int i=1; i<=T; i++) {
	for (int j=0; j<4; j++) {
	    cin >> A[j];
	}
	char p[2] = {'X','O'};
	bool win[2] = {false,};
	bool notComplete = false;
	for (int x=0; x<2; x++) {
	    int c = 0, d = 0;
	    for (int j=0;j<4;j++) {
		int a = 0, b = 0;
		for (int k=0; k<4; k++) {
		    if (A[j][k] == p[x] || A[j][k] == 'T') a++;
		    if (A[k][j] == p[x] || A[k][j] == 'T') b++;
		    if (A[j][k] == '.') notComplete = true;
		}
		if (A[j][j] == p[x] || A[j][j] == 'T') c++;
		if (A[j][3-j] == p[x] || A[j][3-j] == 'T') d++;
		if (a == 4 || b == 4) win[x] = true;
	    }
	    if (c == 4 || d == 4) win[x] = true;
	}
	cout << "Case #" << i << ": ";
	if (win[0] && !win[1]) cout << "X won" << endl;
	else if (!win[0] && win[1]) cout << "O won" << endl;
	else if (win[0] && win[1]) cout << "Draw" << endl;
	else if (!win[0] && !win[1] && notComplete) cout << "Game has not completed" << endl;
	else if (!win[0] && !win[1] && !notComplete) cout << "Draw" << endl;
    }
    return 0;
}
