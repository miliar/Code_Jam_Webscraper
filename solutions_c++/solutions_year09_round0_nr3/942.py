#include <iostream>
#include <queue>
#include <algorithm>
#include <deque>
#include <vector>
#include <cmath>
#include <map>
#include <string>
#include <set>
#include <numeric>
#include <cassert>
#include <iomanip>
#include <ios>

using namespace std;
  
const string w = "welcome to code jam";
const int mod = 10000;
const int MAXL = 500;
const int W = 25;

string s;
int dyna[MAXL][W];

int how_many(int i, int j) {
  if (j == w.size()) return 1;
  if (i == s.size()) return 0;
  assert(i < MAXL);
  int &count = dyna[i][j];
  if (count >= 0) return count;
  count = how_many(i+1,j);
  if (s[i] == w[j])
    count += how_many(i+1,j+1);
  count %= mod;
  return count;
}

int main() {
  int N; cin>>N; cin.ignore();
  for (int tt = 1 ; tt <= N ; tt++) {
    getline(cin, s);
    fill(*dyna, *dyna + MAXL * W, -1);
    cout << "Case #"<<tt<<": ";
    cout << setw(4) << setfill('0') << how_many(0,0) << endl;
  }
}
