#include<iostream>

using namespace std;

#define rep(i, n) for (int i = 0; i < int(n); ++i)

int main() {
  int t;
  cin >> t;
  rep (iii, t) {
    string str[4];
    rep (i, 4) cin >> str[i];
    string res;
    try {
      rep (i, 4) {
	try {
	  rep (j, 4) {
	    if (str[i][j] == '.' || str[i][j] == 'O') {
	      throw 1;
	    }
	  }
	  throw "X won";
	} catch(int n) {
	}
      }
      rep (i, 4) {
	try {
	  rep (j, 4) {
	    if (str[j][i] == '.' || str[j][i] == 'O') {
	      throw 1;
	    }
	  }
	  throw "X won";
	} catch(int n) {
	}
      }
      try {
	rep (i, 4) {
	  if (str[i][i] == '.' || str[i][i] == 'O') {
	    throw 1;
	  }
	}
	throw "X won";
      } catch(int n) {
      }
      try {
	rep (i, 4) {
	  if (str[i][3 - i] == '.' || str[i][3 - i] == 'O') {
	    throw 1;
	  }
	}
	throw "X won";
      } catch(int n) {
      }
      rep (i, 4) {
	try {
	  rep (j, 4) {
	    if (str[i][j] == '.' || str[i][j] == 'X') {
	      throw 1;
	    }
	  }
	  throw "O won";
	} catch(int n) {
	}
      }
      rep (i, 4) {
	try {
	  rep (j, 4) {
	    if (str[j][i] == '.' || str[j][i] == 'X') {
	      throw 1;
	    }
	  }
	  throw "O won";
	} catch(int n) {
	}
      }
      try {
	rep (i, 4) {
	  if (str[i][i] == '.' || str[i][i] == 'X') {
	    throw 1;
	  }
	}
	throw "O won";
      } catch(int n) {
      }
      try {
	rep (i, 4) {
	  if (str[i][3 - i] == '.' || str[i][3 - i] == 'X') {
	    throw 1;
	  }
	}
	throw "O won";
      } catch(int n) {
      }
      rep (i, 4) rep (j, 4) if (str[i][j] == '.') throw "Game has not completed";
      throw "Draw";
    } catch (char const *s) {
      res = s;
    }
    cout << "Case #" << iii + 1 << ": " << res << endl;
  }
  return 0;
}
