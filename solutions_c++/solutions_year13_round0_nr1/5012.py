#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <bitset>
#include <queue>
using namespace std;

//conversion
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

//typedef
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long ll;

//container util
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)

//constant
const double EPS = 1e-10;
const int MAXI = 1234567890;

//debug
#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;



void printList(vector<int>& v) {
  for (size_t i = 0; i < v.size(); i++) {
	cout << v[i] << " ";
  }
  cout << endl;
}

void printMatrix(vector< vector<int> >& v) {
  for (size_t i = 0; i < v.size(); i++) {
	printList(v[i]);
  }
  cout << endl;
}

bool checkD(char c, vector<string>& board) {
  bool flag = true;
  for (int i = 0; i < 4; i++) {
    if (board[i][i] == c
	|| board[i][i] == '.') flag = false;
  }
  if (flag) return true;

  flag = true;
  for (int i = 0; i < 4; i++) {
    if (board[i][3 - i] == c
	|| board[i][3 - i] == '.') flag = false;
  }
  if (flag) return true;
  return false;
}

bool checkS(char c, vector<string>& board) {
  for (int i = 0; i < 4; i++) {
    bool flag = true;
    for (int j = 0; j < 4; j++) {
      if (board[i][j] == c
	  || board[i][j] == '.') flag = false;
    }
    if (flag) return true;
  }

  for (int i = 0; i < 4; i++) {
    bool flag = true;
    for (int j = 0; j < 4; j++) {
      if (board[j][i] == c
	  || board[j][i] == '.') flag = false;
    }
    if (flag) return true;
  }
  return false;

}


string solve(vector<string>& board) {
  if (checkS('O', board) || checkD('O', board)) {
    return "X won";
  } else if (checkS('X', board) || checkD('X', board)) {
    return "O won";
  }

  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
      if (board[i][j] == '.') {
	return "Game has not completed";
      }
    }
  }

  return "Draw";
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    vector<string> board;
    for (int j = 0; j < 4; j++) {
      string s;
      cin >> s;
      board.push_back(s);
    }
    string ans = solve(board);
    cout << "Case #" << i + 1 << ": " << ans << endl;
  }
  return 0;
}
