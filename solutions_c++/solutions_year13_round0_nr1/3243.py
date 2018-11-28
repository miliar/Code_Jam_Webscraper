#include <iostream>
using namespace std;
int t;
string m[4];
int process(){
	bool flag = false;
	for (int i=0; i<4; ++i){
		int c1 = 0, c2 = 0, c3 = 0, c4 = 0;
		for (int j=0; j<4; ++j){
			if (m[i][j] == 'X') c1++;
			if (m[i][j] == 'O') c2++;
			if (m[i][j] == 'T') c1++, c2++;
			if (m[j][i] == 'X') c3++;
			if (m[j][i] == 'O') c4++;
			if (m[j][i] == 'T') c3++, c4++;
			if (m[i][j] == '.') flag = true;
		}
		if (c1 == 4 || c3 == 4) return 1;
		if (c2 == 4 || c4 == 4) return 2;
	}
	int c1 = 0, c2 = 0, c3 = 0, c4 = 0;
	for (int i=0; i<4; ++i){
		if (m[i][i] == 'X') c1++;
		if (m[i][i] == 'O') c2++;
		if (m[i][i] == 'T') c1++, c2++;
		if (m[i][3-i] == 'X') c3++;
		if (m[i][3-i] == 'O') c4++;
		if (m[i][3-i] == 'T') c3++, c4++;
	}
	if (c1 == 4 || c3 == 4) return 1;
	if (c2 == 4 || c4 == 4) return 2;
	if (flag) return 0;
	return 3;
}

int main(){
	cin >> t;
	for (int cas=1; cas<=t; ++cas){
		for (int i=0; i<4; ++i) cin >> m[i];
		int res = process();
		cout << "Case #" << cas << ": ";
		if (res == 0) cout << "Game has not completed" << endl;
		else if (res == 1) cout << "X won" << endl;
		else if (res == 2) cout << "O won" << endl;
		else if (res == 3) cout << "Draw" << endl;
	}
}
