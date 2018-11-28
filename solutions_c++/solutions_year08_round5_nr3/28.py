#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

typedef __int64 ll;

ifstream in("in.txt");
ofstream out("out.txt");
void Init();
void SolveCase();

int main() {
  int N;
  in >> N;
  Init();
  for (int tc = 1; tc <= N; tc++) {
    cout << "Case #" << tc << endl;
    out << "Case #" << tc << ": ";
    SolveCase();
  }
  return 0;
}

void Init() {}
bool IsSet(int bm, int i) {return (bm & (1<<i)) > 0;}
int Works(int w, int bm1, int bm2, const vector<bool> &can_sit) {
  for (int i = 0; i < w; i++)
    if (IsSet(bm2, i)) {
      if (!can_sit[i]) return false;
      if (i > 0 && (IsSet(bm1, i-1) || IsSet(bm2, i-1))) return false;
      if (i+1 < w && (IsSet(bm1, i+1) || IsSet(bm2, i+1))) return false;
    }
  return true;
}

void SolveCase() {
  int best = 0;
  vector<int> best1(1100, 0), best2(1100, 0);
  int h, w;
  in >> h >> w;
  vector<vector<bool> > can_sit(h, vector<bool>(w));
  for (int i = 0; i < h; i++) {
    string s;
    in >> s;
    for (int j = 0; j < w; j++)
      can_sit[i][j] = (s[j] == '.');
  }

  for (int i = 0; i < h; i++) {
    for (int bm2 = 0; bm2 < (1<<w); bm2++) {
      int this_best = 0, base = 0;
      for (int j = 0; j < w; j++)
        if (IsSet(bm2, j))
          base++;
      for (int bm1 = 0; bm1 < (1<<w); bm1++)
        if (Works(w, bm1, bm2, can_sit[i])) {
          this_best = max(this_best, best1[bm1] + base);
        }
      best2[bm2] = this_best;
      if (this_best > best)
        best = this_best;
    }
    best1 = best2;
  }
  out << best << endl;
}