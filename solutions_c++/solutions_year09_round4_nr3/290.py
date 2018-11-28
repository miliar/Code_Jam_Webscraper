
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


vector< vector<int> > g;
int nLeft, nRight;
vector<bool> visited;
vector<int> matching;
bool augment(int left) {
  if(left < 0)
    return true;
  if(visited[left])
    return false;
  visited[left] = true;
  REP(i, g[left].size()) {
    int right = g[left][i];
    if(augment(matching[right])){
      matching[right] = left;
      return true;
    }
  }
  return false;
}
int match(void) {
  matching.assign(nRight, -1);
  int matches = 0;
  REP(left, nLeft) {
    visited.assign(nLeft, false);
    if(augment(left))
      matches++;
  }
  return matches;
}


bool isUpper(vector<int>& v1, vector<int>& v2) {
  int n = v1.size();
  REP(i, n){
    if(v1[i] <= v2[i])
      return false;
  }
  return true;
}


int main(void) {
  int nCases;
  cin >> nCases;

  REP(iCase, nCases) {
    int n, k;
    cin >> n >> k;
    nLeft = n;
    nRight = n;
    g.resize(n+n);
    REP(i, n+n)
      g[i].clear();
    
    vector<vector<int> > table;
    REP(i, n){
      vector<int> vec;
      REP(j, k){
	int v;
	cin >> v;
	vec.push_back(v);
      }
      table.push_back(vec);
    }
    
    REP(i, n){
      REP(j, n){
	if(isUpper(table[i], table[j])){
	  g[i].push_back(j);
	}
      }
    }
    int res = n - match();
    
    cout << "Case #" << (iCase+1) << ": " << res << endl;
  }
  
  return 0;
}
