#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    cout << "Case #" << t+1 << ": ";
    vector<string> table(4);
    for (int i = 0; i < 4; i++)
      cin >> table[i];

    int empty = 0;
    for (int i = 0; i < 4; i++) {
      int x, o;
      x = o = 0;
      for (int j = 0; j < 4; j++) {
	if (table[i][j] == 'X')
	  x++;
	else if (table[i][j] == 'O')
	  o++;
	else if (table[i][j] == 'T') {
	  x++; o++;
	} else {
	  empty++;
	}
      }
      if (x == 4) {
	cout << "X won" << endl;
	goto end;
      }
      else if (o == 4) {
	cout << "O won" << endl;
	goto end;
      }
    }

    for (int j = 0; j < 4; j++) {
      int x, o;
      x = o = 0;
      for (int i = 0; i < 4; i++) {
	if (table[i][j] == 'X')
	  x++;
	else if (table[i][j] == 'O')
	  o++;
	else if (table[i][j] == 'T') {
	  x++; o++;
	}
      }
      if (x == 4) {
	cout << "X won" << endl;
	goto end;
      }
      else if (o == 4) {
	cout << "O won" << endl;
	goto end;
      }
    }

    int x, o;
    x = o = 0;
    for (int i = 0; i < 4; i++) {
      if (table[i][i] == 'X')
	x++;
      else if (table[i][i] == 'O')
	o++;
      else if (table[i][i] == 'T') {
	x++; o++;
      }
    }
    if (x == 4) {
      cout << "X won" << endl;
      goto end;
    }
    else if (o == 4) {
      cout << "O won" << endl;
      goto end;
    }

    x = o = 0;
    for (int i = 0; i < 4; i++) {
      if (table[3-i][i] == 'X')
	x++;
      else if (table[3-i][i] == 'O')
	o++;
      else if (table[3-i][i] == 'T') {
	x++; o++;
      }
    }
    if (x == 4) {
      cout << "X won" << endl;
      goto end;
    }
    else if (o == 4) {
      cout << "O won" << endl;
      goto end;
    }

    if (empty == 0) {
      cout << "Draw" << endl;
    } else {
      cout << "Game has not completed" << endl;
    }

  end:
    ;
  }

  return 0;
}
