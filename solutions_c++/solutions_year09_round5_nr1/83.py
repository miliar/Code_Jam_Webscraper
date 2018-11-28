
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

struct Box {
  int ci;
  int cj;
  vector<pair<int, int> > v;
};

struct K {
  Box box;
  int cost;
};

bool operator>(const K& a, const K& b) {
  return a.cost > b.cost;
}

bool operator==(const Box& a, const Box& b) {
  if(a.ci != b.ci) return false;
  if(a.cj != b.cj) return false;
  REP(i, a.v.size()){
    if(a.v[i] != b.v[i])
      return false;
  }
  return true;
}

bool operator<(const Box& a, const Box& b) {
  if(a.ci != b.ci) return a.ci < b.ci;
  if(a.cj != b.cj) return a.cj < b.cj;
  return a.v < b.v;
}

inline void normalize(Box& b) {
  sort(ALLOF(b.v));
  b.ci = 100;
  b.cj = 100;
  REP(i, b.v.size()){
    b.ci = min(b.ci, b.v[i].first);
    b.cj = min(b.cj, b.v[i].second);
  }
  REP(i, b.v.size()){
    b.v[i].first -= b.ci;
    b.v[i].second -= b.cj;
  }
}

bool field[14][14];

bool isValid(const Box& b) {
  int n = b.v.size();
  int data[5] = {0, 1, 2, 3, 4};
  REP(i, n) REP(j, n){
    if(b.v[i].first == b.v[j].first && b.v[i].second + 1 == b.v[j].second ||
       b.v[i].first == b.v[j].first && b.v[i].second - 1 == b.v[j].second ||
       b.v[i].second == b.v[j].second && b.v[i].first + 1 == b.v[j].first ||
       b.v[i].second == b.v[j].second && b.v[i].first - 1 == b.v[j].first){
      int t = data[i];
      REP(k, n){
	if(data[k] == t)
	  data[k] = data[j];
      }
    }
  }

  REP(i, n-1)
    if(data[i] != data[i+1])
      return false;
  return true;
}
 
void print(const Box& b) {
  cerr << "(" << b.ci << ", " << b.cj << ") : " << endl;
  REP(i, b.v.size())
    cerr << " (" << b.v[i].first << ", " << b.v[i].second << ")";
  cerr << endl;
}

const int DIR[4][2] = {{1, 0},
		       {0, 1},
		       {-1, 0},
		       {0, -1}};
void solve(void) {
  REP(i, 14) REP(j, 14)
    field[i][j] = false;

  int nRows, nCols;
  cin >> nRows >> nCols;

  Box start, goal;
  REP(i, nRows){
    string s;
    cin >> s;
    REP(j, nCols){
      if(s[j] == '.'){
	field[i+1][j+1] = true;
      }else if(s[j] == '#'){
	
      }else if(s[j] == 'o'){
	field[i+1][j+1] = true;
	start.v.push_back(make_pair(i+1, j+1));
      }else if(s[j] == 'x'){
	field[i+1][j+1] = true;
	goal.v.push_back(make_pair(i+1, j+1));
      }else if(s[j] == 'w'){
	field[i+1][j+1] = true;
	start.v.push_back(make_pair(i+1, j+1));
	goal.v.push_back(make_pair(i+1, j+1));
      }else{
	assert(false);
      }
    }
  }
  
  normalize(start);
  normalize(goal);
  int res = -1;
  priority_queue<K, vector<K>, greater<K> > q;
  q.push((K){start, 0});
  set<Box> visited;
  while(!q.empty()){
    K cur = q.top();
    q.pop();
    const Box& box = cur.box;
//     print(box);
    if(visited.count(box) != 0)
      continue;
    visited.insert(box);
    if(box == goal){
      res = cur.cost;
      break;
    }
    
    REP(i, box.v.size()){
      int ci = box.v[i].first + box.ci;
      int cj = box.v[i].second + box.cj;
      REP(d, 4){
	int pi = ci - DIR[d][0];
	int pj = cj - DIR[d][1];
	int ni = ci + DIR[d][0];
	int nj = cj + DIR[d][1];
	if(field[ni][nj] && field[pi][pj]){
	  bool ok = true;
	  REP(j, box.v.size()){
	    if(box.ci + box.v[j].first == ni &&
	       box.cj + box.v[j].second == nj ||
	       box.ci + box.v[j].first == pi &&
	       box.cj + box.v[j].second == pj){
	      ok = false;
	      break;
	    }
	  }
	  
	  
	  if(ok){
	    Box next = box;
	    REP(k, next.v.size()){
	      next.v[k].first += next.ci;
	      next.v[k].second += next.cj;
	    }
	    next.v[i] = make_pair(ni, nj);
	    normalize(next);
// 	    print(next);
	    if((isValid(box) || isValid(next)) && !visited.count(next))
	      q.push((K){next, cur.cost+1});
	  }
	}
      }
    }
  }
  cout << res << endl;
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
