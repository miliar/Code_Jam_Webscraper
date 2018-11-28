#include <iostream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <complex>
#include <string>
#include <stdint.h>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define rep(i,m,n) for(int i = m; i < (int)(n); i++)
#define FOR(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define ALLOF(c) (c).begin(), (c).end()

typedef double decimal;
typedef complex<decimal> P;

const decimal EPS = 1e-8;

const int MOD = 1000000007;

char C[26][26];
int O[26];

int main(){
  int T;
  cin >> T;
  REP(i, T){
    memset(C, 0, sizeof(C));
    memset(O, 0, sizeof(O));
    int N;
    cin >> N;
    REP(_, N){
      string s;
      cin >> s;
      int c0 = s[0] - 'A';
      int c1 = s[1] - 'A';
      C[c0][c1] = s[2];
      C[c1][c0] = s[2];
    }
    cin >> N;
    REP(_, N){
      string s;
      cin >> s;
      int c0 = s[0] - 'A';
      int c1 = s[1] - 'A';
      O[c0] |= 1 << c1;
      O[c1] |= 1 << c0;
    }
    cin >> N;
    vector<char> ans;
    int B = 0;
    int B0 = 0;
    int B1 = 0;
    REP(_, N){
      char c;
      cin >> c;
      int c0 = c - 'A';
      B1 = B0;
      B0 = B;
      if(ans.size() == 0){
        ans.push_back(c);
        B |= 1 << c0;
        continue;
      }
      int c1 = ans.back() - 'A';
      if(C[c0][c1] > 0){
        char x = C[c0][c1];
        ans[ans.size()-1] = x;
        int c2 = x - 'A';
        B = B1 | (1 << c2);
        continue;
      }
      if(B & O[c0]){
        ans.clear();
        B = 0;
        continue;
      }
      ans.push_back(c);
      B |= 1 << c0;
    }

    cout << "Case #" << i+1 << ": [";
    REP(j, ans.size()){
      if(j > 0) cout << ", ";
      cout << ans[j];
    }
    cout << "]" << endl;
  }

  return 0;
}

