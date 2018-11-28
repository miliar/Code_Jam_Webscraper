#include <iostream>
#include <string>
#include <vector>

using namespace std;

enum Outcome {XWIN, OWIN, DRAW, NOVER};

Outcome check(const string& str) {
	//cout << "checking " << str << endl;
  int num_x = 0, num_o = 0, num_t = 0;
  for (int i = 0; i < str.size(); ++i) {
    if ('X' == str[i]) { ++num_x; }
    if ('O' == str[i]) { ++num_o; }
    if ('T' == str[i]) { ++num_t; }
  }
  if (str.size() == num_x + num_t) {
    return XWIN;
  } else if (str.size() == num_o + num_t) {
    return OWIN;
  } else if (str.size() == num_x + num_o + num_t) {
  	return DRAW;
  } else {
  	return NOVER;
 	}
}

Outcome solve(const vector<string>& matrix) {
  string str;
  bool nover = false;
  
  for (int i = 0; i < 4; ++i) {
    Outcome res = check(matrix[i]);
    if (NOVER == res) {
      nover = true;
    }
    if (XWIN == res) {
    	return XWIN;
    }
    if (OWIN == res) {
    	return OWIN;
    }
  }
  for (int j = 0; j < 4; ++j) {
    str.clear();
    for (int i = 0; i < 4; ++i) { str.push_back(matrix[i][j]);}
    Outcome res = check(str);
    if (XWIN == res) {
    	return XWIN;
    }
    if (OWIN == res) {
    	return OWIN;
    }
  }
  str.clear();
  for (int i = 0; i < 4; ++i) {
  	str.push_back(matrix[i][i]);
  }
  Outcome res = check(str);
  if (XWIN == res) {
  	return XWIN;
  }
  if (OWIN == res) {
   	return OWIN;
  }
  str.clear();
  for (int i = 0; i < 4; ++i) {
  	str.push_back(matrix[i][3-i]);
  }
  res = check(str);
  if (XWIN == res) {
  	return XWIN;
  }
  if (OWIN == res) {
   	return OWIN;
  }
  if (nover) {
    return NOVER;
  } else {
  	return DRAW;
  }
}

int main(int argc, char *argv[]) {
  int n_cases;
  
  cin >> n_cases;
  
  for (int i = 0; i < n_cases; ++i) {
    vector<string> matrix;
    for (int r = 0; r < 4; ++r) {
    	string row;
    	cin >> row;
    	matrix.push_back(row);
    }
    Outcome res = solve(matrix);
    cout << "Case #" << i + 1 << ": ";
    switch (res) {
    	case XWIN: cout << "X won";
    		break;
    	case OWIN: cout << "O won";
    		break;
    	case DRAW: cout << "Draw";
    		break;
    	case NOVER: cout << "Game has not completed";
    		break;
    }
    cout << endl;
  }
}

