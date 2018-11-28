#include <cstdio>
#include <iostream>

using namespace std;

char s[10][10];

int main() {
  int T; scanf("%d\n", &T);
  for (int tt = 1; tt <= T; ++tt) {
  	for (int i = 0; i < 4; ++i) {
  		cin >> s[i];
  	}
  	bool X = false, O = false, D = true;
  	for (int i = 0; i < 4; ++i) {
  		int x = 0, o = 0, t = 0;
  		for (int j = 0; j < 4; ++j) {
  			if (s[i][j] == 'X') ++x;
  			else if (s[i][j] == 'O') ++o;
  			else if (s[i][j] == 'T') ++t;
  		}
  		if (x == 4 || x == 3 && t == 1) {
  			X = true;
  		}
  		if (o == 4 || o == 3 && t == 1) {
  			O = true;
  		}
  		if (x + o + t < 4) D = false;
  		x = 0, o = 0, t = 0;
  		for (int j = 0; j < 4; ++j) {
  			if (s[j][i] == 'X') ++x;
  			else if (s[j][i] == 'O') ++o;
  			else if (s[j][i] == 'T') ++t;
  		}
  		if (x == 4 || x == 3 && t == 1) {
  			X = true;
  		}
  		if (o == 4 || o == 3 && t == 1) {
  			O = true;
  		}
  		if (x + o + t < 4) D = false;
  	}
  	int x = 0, o = 0, t = 0;
	for (int j = 0; j < 4; ++j) {
		if (s[j][j] == 'X') ++x;
		else if (s[j][j] == 'O') ++o;
		else if (s[j][j] == 'T') ++t;
	}
	if (x == 4 || x == 3 && t == 1) {
		X = true;
	}
	if (o == 4 || o == 3 && t == 1) {
		O = true;
	}
	if (x + o + t < 4) D = false;

  	x = 0, o = 0, t = 0;
	for (int j = 0; j < 4; ++j) {
		if (s[3 - j][j] == 'X') ++x;
		else if (s[3 - j][j] == 'O') ++o;
		else if (s[3 - j][j] == 'T') ++t;
	}
	if (x == 4 || x == 3 && t == 1) {
		X = true;
	}
	if (o == 4 || o == 3 && t == 1) {
		O = true;
	}
	if (x + o + t < 4) D = false;

    printf("Case #%d: ", tt);
    if (X) cout << "X won" << endl;
    else if (O) cout << "O won" << endl;
    else if (D) cout << "Draw" << endl;
    else cout << "Game has not completed" << endl;
  }
  return 0;
}

