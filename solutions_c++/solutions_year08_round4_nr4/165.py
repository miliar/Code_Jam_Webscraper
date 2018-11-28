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

int main() {
  int N;
  in >> N;
  for (int tc = 1; tc <= N; tc++) {
    out << "Case #" << tc << ": ";
    SolveCase();
  }
  return 0;
}

int NB(const string &s) {
  char last = 0;
  int res = 0;
  for (int i = 0; i < (int)s.size(); i++) {
    if (s[i] != last) {last = s[i]; res++;}
  }
  return res;
}

void SolveCase() {
  string s;
  int n;
  vector<int> perm;
  in >> n >> s;
  int best = 100000;
  int sl = s.size();
  for (int i = 0; i < n; i++)
    perm.push_back(i);
  do {
    string s2;
    for (int i=0; i < sl/n; i++)
      for (int j = 0; j < n; j++)
        s2 += s[i*n+perm[j]];
    best = min(best, NB(s2));
  } while (next_permutation(perm.begin(), perm.end()));
  out << best << endl;
}