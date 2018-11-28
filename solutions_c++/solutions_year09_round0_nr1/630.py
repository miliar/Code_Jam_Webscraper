#include <iostream>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;
int L, N, T;

vector<string> w;

int pot[5555];
int test = 0;

void go() {
  int i, j;
  for (i = 0; i < N; ++i) pot[i] = 1;

  //read letters
  for (j = 0; j < L; ++j) {
    char c;
    int was[30]; memset(was, 0, sizeof(was));
    cin >> c;
    if (c == '(') {
      cin >> c;
      while (c != ')') {
        was[c-'a'] = 1; cin >> c;
      }
    } else {
      was[c-'a'] = 1;
    }
    for (i = 0; i < N; ++i) if (!was[w[i][j]-'a']) pot[i] = 0;
  }
  int cat = 0;
  for (i = 0; i < N; ++i) if (pot[i]) cat++;
  printf("Case #%d: %d\n", ++test, cat);
}
int main() {
  freopen("large.in", "r", stdin); 
  freopen("large.out", "w", stdout);

  cin >> L >> N >> T;

  for (int i = 0; i < N; ++i) {
    string line;
    cin >> line;
    w.push_back(line);
  } 
  while (T--) go(); 
  return 0;
}
