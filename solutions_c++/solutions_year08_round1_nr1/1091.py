#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cassert>

#define TMP(x) tmp_ ## x
#define FOR(I,B,E) for (__typeof(E) I = (B), TMP(I) = (E); I < TMP(I); ++I)
#define FOREACH(I,C) for (__typeof((C).begin()) I = (C).begin(); I != (C).end(); ++I)
#define LOOP(I,E) FOR(I,0,E)
#define REP(E) FOR(TMP(i),0,E)
#define KEY(P) (P)->first
#define VAL(P) (P)->second

using namespace std;

namespace messi {

void run() {
  string line;
  int T;
  cin >> T;
  FOR(t, 1, T + 1) {
    int n;
    cin >> n;
    vector<int> v1s;
    vector<int> v2s;
    FOR(i,0,n) {
      signed int x;
      cin >> x;
      v1s.push_back(x);
    }
    FOR(i,0,n) {
      signed int y;
      cin >> y;
      v2s.push_back(y);
    }
    sort(v1s.begin(),v1s.end(),less<int>());
    sort(v2s.begin(),v2s.end(),greater<int>());
    signed int min = 0;
    FOR(i,0,n) {
      min += v1s[i] * v2s[i];
    }
    cout << "Case #" << t << ": " << min << endl;
  }
}

}//namespace

int main() {
  messi::run();
  return 0;
}
