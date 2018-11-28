#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <string.h>
#include <algorithm>
#include <set>
#include <cstdio>

using namespace std;

map<pair<int, int>, bool> m;
vector<pair<int, int> > v;
int N, D;

bool go(int vi, int d) {
  if(m.count(make_pair(vi, d))) {
    return m[make_pair(vi, d)];
  }
  if(v[vi].first + d >= D) {
    return true;
  }
  for(int i = vi+1; i < N; ++i) {
    if(v[i].first <= v[vi].first + d) {
      if(go(i, min(v[i].second, v[i].first-v[vi].first))) return m[make_pair(vi, d)] = true;
    }
  }
  return m[make_pair(vi, d)] = false;
}

string solve() {
  cin >> N;
  v.clear();
  m.clear();
  for(int i = 0; i < N; ++i) {
    int a, b; cin >> a >> b;
    v.push_back(make_pair(a, b));
  }
  cin >> D;
  if(go(0, v[0].first)) return "YES";
  return "NO";
  int cVine = 0, cLen = v[0].first;
  while(true) {
    int maxNext = 0;
    int next = -1;
    for(int i = cVine+1; i < N; ++i) {
      if(v[i].first <= v[cVine].first + cLen) {
        if(v[i].first + min(v[i].second, v[i].first-v[cVine].first) > maxNext) {
          maxNext = v[i].first + min(v[i].second, v[i].first-v[cVine].first);
          next = i;
        }
      }
    }
    if(next == -1) return "NO";
    if(maxNext >= D) return "YES";
    cLen = min(v[next].second, v[next].first-v[cVine].first);
    cVine = next;
  }
  
  
  return "YES";
}

int main() {
  int TC; cin >> TC;
  for (int t = 1; t <= TC; t++) {
    
    printf("Case #%d: ", t);
    cout << solve() << endl;
  }


  return 0;
}
