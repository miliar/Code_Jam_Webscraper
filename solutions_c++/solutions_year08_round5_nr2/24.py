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
void SolveCase();

int main() {
  int N;
  in >> N;
  for (int tc = 1; tc <= N; tc++) {
    out << "Case #" << tc << ": ";
    SolveCase();
  }
  return 0;
}

const int kl = 16;
int Encode(int x, int y, int p1x, int p1y, int p2x, int p2y) {
  int v1 = y*kl+x;
  int v2 = p1y*kl+p1x;
  int v3 = p2y*kl+p2x;
  return v1*kl*kl*kl*kl + v2*kl*kl + v3;
}

void Decode(int code, int *x, int *y, int *p1x, int *p1y, int *p2x, int *p2y) {
  *p2x = (code % kl); code /= kl;
  *p2y = (code % kl); code /= kl;
  *p1x = (code % kl); code /= kl;
  *p1y = (code % kl); code /= kl;
  *x = (code % kl); code /= kl;
  *y = (code % kl);
}

void SolveCase() {
  cout << "START" << endl;
  int gx, gy, sx, sy;
  int r, c;
  in >> r >> c;
  vector<vector<bool> > is_wall(r, vector<bool>(c, false));
  for (int i = 0; i < r; i++) {
    string s;
    in >> s;
    for (int j = 0; j < c; j++) {
      if (s[j] == 'O') {
        sx = j;
        sy = i;
      } else if (s[j] == 'X') {
        gx = j;
        gy = i;
      } else if (s[j] == '#') {
        is_wall[i][j] = true;
      }
    }
  }

  int dx[4] = {-1, 0, 1, 0};
  int dy[4] = {0, -1, 0, 1};
  int xtarget[15][15][4];
  int ytarget[15][15][4];
  for (int y = 0; y < (int)is_wall.size(); y++)
  for (int x = 0; x < (int)is_wall[y].size(); x++)
  for (int d = 0; d < 4; d++) {
    for (int l = 1; ; l++) {
      int x2 = x + dx[d] * l;
      int y2 = y + dy[d] * l;
      if (x2 < 0 || y2 < 0 || x2 >= (int)is_wall[y].size() || y2 >= (int)is_wall.size() || is_wall[y2][x2]) {
        xtarget[y][x][d] = x + dx[d] * (l-1);
        ytarget[y][x][d] = y + dy[d] * (l-1);
        break;
      }
    }
  }

  vector<int> best(kl*kl*kl*kl*kl*kl, -1);
  int spos = Encode(sx, sy, kl-1, kl-1, kl-1, kl-1);
  best[spos] = 0;
  queue<int> q0, q1;
  q0.push(spos);
  while (!q0.empty() || !q1.empty()) {
    int next_i;
    if (q0.empty()) {
      next_i = q1.front();
      q1.pop();
    } else {
      next_i = q0.front();
      q0.pop();
    }

    int x, y, p1x, p1y, p2x, p2y, dist = best[next_i];
    Decode(next_i, &x, &y, &p1x, &p1y, &p2x, &p2y);
    if (x == gx && y == gy) {
      out << dist << endl;
      return;
    }
    vector<int> targets1, targets0;
    if (x+1 < (int)is_wall[y].size() && !is_wall[y][x+1]) targets1.push_back(Encode(x+1, y, p1x, p1y, p2x, p2y));
    if (x > 0 && !is_wall[y][x-1]) targets1.push_back(Encode(x-1, y, p1x, p1y, p2x, p2y));
    if (y+1 < (int)is_wall.size() && !is_wall[y+1][x]) targets1.push_back(Encode(x, y+1, p1x, p1y, p2x, p2y));
    if (y > 0 && !is_wall[y-1][x]) targets1.push_back(Encode(x, y-1, p1x, p1y, p2x, p2y));
    if (x == p1x && y == p1y && p2x != kl-1) targets1.push_back(Encode(p2x, p2y, p1x, p1y, p2x, p2y));
    if (x == p2x && y == p2y && p1x != kl-1) targets1.push_back(Encode(p1x, p1y, p1x, p1y, p2x, p2y));

    for (int d = 0; d < 4; d++) {
      targets0.push_back(Encode(x, y, xtarget[y][x][d], ytarget[y][x][d], p2x, p2y));
      targets0.push_back(Encode(x, y, p1x, p1y, xtarget[y][x][d], ytarget[y][x][d]));
    }

    for (int i = 0; i < (int)targets0.size(); i++) {
      if (targets0[i] < 0 || targets0[i] >= kl*kl*kl*kl*kl*kl)
        cout << "ERROR" << endl;
      if (best[targets0[i]] == -1 || best[targets0[i]] > dist) {
        best[targets0[i]] = dist;
        q0.push(targets0[i]);
      }
    }
    for (int i = 0; i < (int)targets1.size(); i++) {
      if (targets1[i] < 0 || targets1[i] >= kl*kl*kl*kl*kl*kl)
        cout << "ERROR" << endl;
      if (best[targets1[i]] == -1 || best[targets1[i]] > dist+1) {
        best[targets1[i]] = dist+1;
        q1.push(targets1[i]);
      }
    }
  }
  out << "THE CAKE IS A LIE" << endl;
}
