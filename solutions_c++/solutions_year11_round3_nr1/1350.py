#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <string> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <cstring> 
#include <ctime> 
 
using namespace std; 
 
int main () { 
  int t, T; 

  cin >> T; 
  for (t = 1; t <= T; t++) {
    int R, C;
    cin >> R >> C;
    int a[R][C];
    for (int r = 0; r < R; r++)
      for (int c = 0; c < C; c++) {
	char s; cin >> s;
	a[r][c] = s;
      }
    for (int r = 0; r < R - 1; r++)
      for (int c = 0; c < C - 1; c++)
	if (a[r][c] == '#' && a[r][c+1] == '#' && a[r+1][c] == '#' && a[r+1][c+1] == '#') {
	  a[r][c] = '/';
	  a[r][c+1] = '\\';
	  a[r+1][c] = '\\';
	  a[r+1][c+1] = '/';
	}
    bool flag = true;
    for (int r = 0; r < R; r++) {
      for (int c = 0; c < C; c++)
	if (a[r][c] == '#') {
	  flag = false; break;
	}
      if (flag == false) break;
    }
    cout << "Case #" << t << ": " << endl;
    if (flag) {
      for (int r = 0; r < R; r++) {
	for (int c = 0; c < C; c++)
	  cout << (char)a[r][c];
	cout << endl;
      }
    }
    else
      cout << "Impossible" << endl;
  }
  return 0; 
}
