#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define syso system("pause")
#define mp make_pair

using namespace std;

bool valid(int i, int j) {
  return i > -1 && j > -1 && i < 4 && j < 4;
}

int vec[4][2] = {{1, 0}, {0, 1}, {1, 1}, {-1, 1}};

int main(){
  freopen("Al.out","wt", stdout);
  freopen("Al.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  FOR (test, tests){
    string game[4];
    FOR (i, 4)
      cin >> game[i];
    int cnt = 0;
    FOR (i, 4)
      FOR (j, 4)
        cnt += game[i][j] == '.';

    bool Xwin = false, Owin = false;
    FOR (i, 4)
      FOR (j, 4)
        FOR (k, 4) {
          bool Xgood = true;
          bool Ogood = true;
          int cntT = 0;
          FOR (l, 4) {
            int ni = i + l * vec[k][0];
            int nj = j + l * vec[k][1];
            if (!valid(ni, nj)) {
              Xgood = Ogood = false;
              break;
            }
            if (game[ni][nj] != 'X' && game[ni][nj] != 'T')
              Xgood = false;
            if (game[ni][nj] != 'O' && game[ni][nj] != 'T')
              Ogood = false;
            cntT += game[ni][nj] == 'T';
          }
          Xwin |= (Xgood && cntT <= 1);
          Owin |= (Ogood && cntT <= 1);
        }

    cout << "Case #" << (test + 1) << ": ";
    if (Xwin)
      cout << "X won";
    else if (Owin)
      cout << "O won";
    else if (cnt)
      cout << "Game has not completed";
    else
      cout << "Draw";
    cout << "\n";
  }
  return 0;
}
