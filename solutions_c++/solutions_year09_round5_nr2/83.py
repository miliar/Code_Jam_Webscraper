
#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <list>
#include <cmath>
#include <complex>
#include <numeric>
#include <cassert>
using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); ++i)
#define FOR(i,s) for(__typeof((s).begin()) i = (s).begin(); i != (s).end(); ++i)
#define ALLOF(s) ((s).begin()), ((s).end())

typedef long long integer;

const int MOD = 10009;
string poly;
int nDict;
vector<vector<int> > expr;


void calc_term(int& p) {
  vector<int> res;
  while(p < poly.size() && isalpha(poly[p])){
    res.push_back(poly[p++]-'a');
  }
  expr.push_back(res);
}

void calc_exp(int& p) {
  calc_term(p);
  while(p < poly.size()){
    assert(poly[p] == '+');
    p++;
    calc_term(p);
  }
}

int calc(const vector<int>& vec) {
  int res = 0;
  REP(i, expr.size()){
    const vector<int>& term = expr[i];
    int tmp = 1;
    REP(j, term.size()){
      tmp = (tmp * vec[term[j]]) % MOD;
    }
    res = (res + tmp) % MOD;
  }
  return res;
}

map<vector<int>, int> memo;

int go(int len, const vector<vector<int> >& hists, vector<int>& vec) {
  if(len == 0){
    return calc(vec);
//     if(memo.count(vec))
//       return memo[vec];
//     int res = calc(vec);
//     return memo[vec] = res;
  }else{
    int res = 0;
    REP(i, hists.size()){
//       vector<int> next = hists[i];
//       REP(j, 26)
// 	next[j] += vec[j];
//       res = (res + go(len-1, hists, next)) % MOD;
      REP(j, 26)
	vec[j] += hists[i][j];
      res = (res + go(len-1, hists, vec)) % MOD;
      REP(j, 26)
	vec[j] -= hists[i][j];
    }
    return res;
  }
}

void solve(void) {
  memo.clear();
  cin >> poly;
  expr.clear();
  int p = 0;
  calc_exp(p);
  int K;
  cin >> K;
  cin >> nDict;
  vector<vector<int> > hists(nDict, vector<int>(26, 0));
  REP(i, nDict){
    string s;
    cin >> s;
    REP(j, s.size())
      hists[i][s[j]-'a']++;
  }
  
  REP(len, K){
    vector<int> vec(26, 0);
    int res = go(len+1, hists, vec);
    cout << res << " ";
  }
  cout << endl;
}


int main(void) {
  int nCases;
  {
    string s;
    getline(cin, s);
    istringstream sin(s);
    sin >> nCases;
  }

  REP(iCase, nCases) {
    cout << "Case #" << (iCase+1) << ": ";
    solve();
  }
  
  return 0;
}
