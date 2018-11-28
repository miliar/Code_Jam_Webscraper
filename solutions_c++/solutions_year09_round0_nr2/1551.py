using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

template <class T> string toStr(const T &x){ stringstream s; s << x; return s.str(); }
template <class T> int toInt(const T &x){ stringstream s; s << x; int r; s >> r; return r; }

#define For(i, a, b) for (int i=(a); i<(b); ++i)
#define foreach(x, v) for (typeof (v).begin() x = (v).begin(); x != (v).end(); ++x)
#define D(x) cout << #x " = " << (x) << endl

int di[] = {-1, +0, +0, +1};
int dj[] = {+0, -1, +1, +0};

const int MAXN = 105;
int rows, cols;
int mat[MAXN][MAXN];
int basin[MAXN][MAXN];
int current_basin;
map<int, char> face;

inline bool inside(int i, int j){
  return 0 <= i && i < rows && 0 <= j && j < cols;
}

bool sink(int i, int j){
  if (!inside(i, j)) return false;
  for (int k=0; k<4; ++k){
    int ni = i + di[k], nj = j + dj[k];
    if (inside(ni, nj) && mat[ni][nj] < mat[i][j]) return false;
  }
  return true;
}


int find_basin(int i, int j){
  if (basin[i][j] != -1) return basin[i][j];
  if (sink(i, j)){
    if (basin[i][j] == -1) basin[i][j] = current_basin++;
    return basin[i][j];
  }
  int best = INT_MAX;
  int bi = -1, bj = -1;
  for (int k=0; k<4; ++k){
    int ni = i + di[k], nj = j + dj[k];
    if (inside(ni, nj) && mat[ni][nj] < best){
      best = mat[ni][nj];
      bi = ni, bj = nj;
    }
  }
  assert(bi != -1 && bj != -1);
  return basin[i][j] = find_basin(bi, bj);
}

int main(){
  int T;
  cin >> T;
  for (int Caso=1; Caso<=T; ++Caso){
    cin >> rows >> cols;
    current_basin = 0;
    face.clear();
    for (int i=0; i<rows; ++i){
      for (int j=0; j<cols; ++j){
        cin >> mat[i][j];
        basin[i][j] = -1;
      }
    }
    for (int i=0; i<rows; ++i){
      for (int j=0; j<cols; ++j){
        find_basin(i, j);
      }
    }

    char current_face = 'a';

    printf("Case #%d:\n", Caso);
    for (int i=0; i<rows; ++i){
      for (int j=0; j<cols; ++j){
        if (face.count(basin[i][j]) == 0){
          face[basin[i][j]] = current_face++;
        }
        printf("%c", face[basin[i][j]]);
        if (j < cols - 1) printf(" ");
      }
      printf("\n");
    }

  }
  return 0;
}
