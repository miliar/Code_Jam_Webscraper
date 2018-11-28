#include <iostream>

using namespace std;

bool se(char k[50][50], int r, int c, int y, int x) {
  if(y >= r || x >= c) return false;
  if(k[y][x] != '#' && k[y][x] != '/') return false;
  k[y][x] = '/';
  return true;
}

bool ne(char k[50][50], int r, int c, int y, int x) {
  if(y >= r || x >= c) return false;
  if(k[y][x] != '#' && k[y][x] != '\\') return false;
  k[y][x] = '\\';
  return se(k, r, c, y+1, x);
}

bool sw(char k[50][50], int r, int c, int y, int x) {
  if(y >= r || x >= c) return false;
  if(k[y][x] != '#' && k[y][x] != '\\') return false;
  k[y][x] = '\\';
  return true;
}

bool solve(char k[50][50], int r, int c) {
  bool ok = true;
  for(int i = 0; i < r; ++i) {
    for(int j = 0; j < c; ++j) {
      if(k[i][j] == '#') {
        k[i][j] = '/';
        ok = ok && ne(k, r, c, i, j+1) && sw(k, r, c, i+1, j);
      }
    }
  }
  return ok;
}

void f(int C) {
  char kuva[50][50];
  int r, c;
  cin >> r >> c;
  for(int i = 0; i < r; ++i) {
    for(int j = 0; j < c; ++j) {
      cin >> kuva[i][j];
    }
  }

  bool ok = solve(kuva, r, c);
  
  cout << "Case #"<< C << ":\n";
  if(!ok) cout << "Impossible\n";
  else {
    for(int i = 0; i < r; ++i) {
      for(int j = 0; j < c; ++j) {
        cout << kuva[i][j];
      }
      cout << "\n";
    }
  }
  
}

int main() {
  int T;
  cin >> T;
  for(int i = 1; i <= T; ++i) {
    f(i);
  }
}
