// another fine solution by misof
// #includes {{{
#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
using namespace std;
// }}}

/////////////////// PRE-WRITTEN CODE FOLLOWS, LOOK DOWN FOR THE SOLUTION ////////////////////////////////

// pre-written code {{{
#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define REP(i,n) for(int i=0;i<(int)(n);++i)
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

class MaximumMatching {
  vector< vector<int> > left_to_right, right_to_left;

  public:
  void add_edge(int left, int right);
  int maximum_matching_size();
  vector< pair<int,int> > maximum_matching();
  pair< vector<int>, vector<int> > minimum_vertex_cover();
};

void MaximumMatching::add_edge(int left, int right) {
  if ( int(left_to_right.size()) <= left ) left_to_right.resize(left+1);
  if ( int(right_to_left.size()) <= right ) right_to_left.resize(right+1);
  left_to_right[left].push_back(right);
  right_to_left[right].push_back(left);
}

vector< pair<int,int> > 
MaximumMatching::maximum_matching() {
  int L = left_to_right.size(), R = right_to_left.size();
  vector<int> match(L,-1);
  for (int r=0; r<R; r++) {
    bool found = false;
    vector<int> from(L,-1);
    queue<int> Q;
    FOREACH(it,right_to_left[r]) { Q.push(*it); from[*it]=*it; }
    while (!Q.empty() && !found) {
      int l = Q.front(); Q.pop();
      if (match[l]==-1) {
        found = true;
        while (from[l]!=l) { match[l] = match[from[l]]; l = from[l]; }
        match[l]=r;
      } else {
        FOREACH(it,right_to_left[ match[l] ]) if (from[*it]==-1) { Q.push(*it); from[*it]=l; }
      }
    }
  }
  vector< pair<int,int> > result;
  for (int i=0; i<L; i++) if (match[i] != -1) result.push_back(make_pair(i,match[i]));
  return result;
}

int MaximumMatching::maximum_matching_size() { return maximum_matching().size(); }

pair< vector<int>, vector<int> >
MaximumMatching::minimum_vertex_cover() {
  int L = left_to_right.size(), R = right_to_left.size();
  vector< pair<int,int> > matching = maximum_matching();

  vector<int> match(L,-1);
  vector<bool> matched(R,false);
  FOREACH(it,matching) { match[it->first]=it->second; matched[it->second]=true; }

  vector<bool> visited(L,false);
  queue<int> Q;
  for (int r=0; r<R; r++) if (!matched[r])
    FOREACH(it,right_to_left[r]) if (!visited[*it]) { visited[*it]=true; Q.push(*it); }
  while (!Q.empty()) {
    int l = Q.front(); Q.pop();
    FOREACH(it,right_to_left[ match[l] ]) if (!visited[*it]) { Q.push(*it); visited[*it]=true; }
  }

  vector<int> left_cover, right_cover;
  for (int l=0; l<L; l++) 
    if (visited[l]) left_cover.push_back(l);
    else if (match[l]!=-1) right_cover.push_back(match[l]);

  return make_pair( left_cover, right_cover );
}

int main() {
  int T;
  cin >> T;
  FOR(t,1,T) {
    int N, K;
    cin >> N >> K;
    vector< vector<int> > P(N, vector<int>(K));
    REP(n,N) REP(k,K) cin >> P[n][k];
    MaximumMatching M;
    REP(n,N) REP(n2,N) {
      bool ok = true;
      REP(i,K) if (P[n][i] >= P[n2][i]) ok = false;
      if (ok) M.add_edge(n,n2);
    }
    cout << "Case #" << t << ": " << (N-M.maximum_matching_size()) << endl;
  }
  return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
