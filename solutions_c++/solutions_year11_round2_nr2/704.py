#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int main() {
  int T; fin >> T;

  for (int t = 0; t < T; ++t) {
    int C, D; fin >> C >> D;
    vector<int> P(C); vector<int> V(C);
    vector<double> pos;
    for (int i = 0; i < C; ++i) {
      fin >> P[i] >> V[i];
      for (int j = 0; j < V[i]; ++j)
        pos.push_back(P[i]);
    }
    double ans = 0;
    double xprev = pos[0];
    for (int i = 1; i < pos.size(); ++i) {
      double xnew = max(xprev + D, pos[i]);
      double t = 0.5*(xnew - pos[i]);
      if (t > ans) ans = t;
      xprev = xnew;
    }
    fout << "Case #" << t + 1 << ": " << ans << endl;
  }

  return 0;
}