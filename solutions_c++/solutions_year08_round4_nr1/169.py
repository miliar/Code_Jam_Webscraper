#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

ifstream in("in.txt");
ofstream out("out.txt");
void SolveCase();
void SolveEasy();

int main() {
  int N;
  in >> N;
  for (int tc = 1; tc <= N; tc++) {
    out << "Case #" << tc << ": ";
    //SolveEasy();
    SolveCase();
  }
  return 0;
}

int m;
vector<int> v, c, val;
vector<int> memo;

int GetBest(int pos) {
  if (pos >= (m-1)/2)
    return 2*m;
  if (memo[pos] != -1)
    return memo[pos];

  int best = 2*m;
  int goal = 1 - val[pos];
  for (int i = 0; i < 2; i++)
    for (int j = 0; j < 2; j++)
      for (int k = 0; k < 2; k++) {
        if (c[pos] == 0 && i == 1) continue;
        int op = (i == 0? v[pos] : 1 - v[pos]);
        int lhs = (j == 0? val[2*pos+1] : 1 - val[2*pos+1]);
        int rhs = (k == 0? val[2*pos+2] : 1 - val[2*pos+2]);
        int result;
        if (op == 1)
          result = min(lhs, rhs);
        else
          result = max(lhs, rhs);
        if (result != goal) continue;
        int cost = 0;
        if (i) cost++;
        if (j) cost += GetBest(2*pos+1);
        if (k) cost += GetBest(2*pos+2);
        best = min(best, cost);
      }

  memo[pos] = best;
  return best;
}

// 1 = and
void SolveCase() {
  int goal;
  in >> m >> goal;
  v = vector<int>(m, 0);
  c = vector<int>(m, 0);
  val = vector<int>(m, 0);
  memo = vector<int>(m, -1);
  for (int i = 0; i < (m-1)/2; i++)
    in >> v[i] >> c[i];
  for (int i = (m-1)/2; i < m; i++)
    in >> v[i];
  for (int i = m-1; i >= 0; i--) {
    if (i >= (m-1)/2)
      val[i] = v[i];
    else if (v[i])
      val[i] = min(val[2*i+1], val[2*i+2]);
    else
      val[i] = max(val[2*i+1], val[2*i+2]);
  }
  if (val[0] == goal) {
    out << 0 << endl;
  } else {
    int x = GetBest(0);
    if (x >= 2*m)
      out << "IMPOSSIBLE" << endl;
    else
      out << x << endl;
  }
}

void SolveEasy() {
  int goal, best;
  in >> m >> goal;
  //out<< m << endl;
  v = vector<int>(m, 0);
  c = vector<int>(m, 0);
  for (int i = 0; i < (m-1)/2; i++)
    in >> v[i] >> c[i];
  for (int i = (m-1)/2; i < m; i++)
    in >> v[i];
  best = 2*m;

  for (int bm = 0; bm < (1<<15); bm++) {
    int cost = 0;
    val = vector<int>(m, 0);
    for (int i = m-1; i >= 0; i--) {
      int op = v[i];
      if (i < (m-1)/2) {
        if (bm & (1<<i)) {
          op = 1-op;
          cost++;
          if (!c[i]) cost = 2*m;
        }
      }
      if (i >= (m-1)/2)
        val[i] = v[i];
      else if (op)
        val[i] = min(val[2*i+1], val[2*i+2]);
      else
        val[i] = max(val[2*i+1], val[2*i+2]);
    }
    if (val[0] == goal) best = min(best, cost);
  }

  if (best >= 2*m)
    out << "IMPOSSIBLE" << endl;
  else
    out << best << endl;
}