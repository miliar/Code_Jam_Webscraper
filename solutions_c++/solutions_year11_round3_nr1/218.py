#include <iostream>
#include <set>
#include <iomanip>
#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <fstream>
using namespace std;

int main() {
  ifstream cin("A-large (3).in");
  ofstream cout("out.txt");
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++) {
    int R,C;
    cin >> R >> C;
    vector<string> m(R);
    for(int i = 0; i < R; i++) {
      cin >> m[i];
    }
    cout << "Case #" << t << ":";
    cout << " ";
    cout << endl;
    bool b = true;
    for(int i = 0; i < R; i++) {
      for(int j = 0; j < C; j++) {
        if(m[i][j] == '#') {
          if(j == C-1 || i == R-1) {
            cout << "Impossible" << endl;
            b = false;
            break;
          }
          if(m[i+1][j] != '#' || m[i][j+1] != '#' || m[i+1][j+1] != '#') {
            cout << "Impossible" << endl;
            b = false;
            break;
          }
          m[i][j] = '/';
          m[i+1][j] = '\\';
          m[i][j+1] = '\\';
          m[i+1][j+1] = '/';
        }
      }
      if(!b)
        break;
    }
    if(b) {
      for(int i = 0; i < R; i++) {
        cout << m[i] << endl;
      }
    }
    //cout << endl;
  }
}
