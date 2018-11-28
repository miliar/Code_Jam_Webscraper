#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <deque>

using namespace std;

typedef long long int int64;
typedef vector<int> VI;
#define REP(i,a,b) for (int i=int(a); i<int(b); ++i)
void unittest();

int N;
int D;

/*
bool traverse(int cur, int prev) {
  que.erase(cur);
  int dist = viles[cur];
  int forward = min(dist, cur-prev);

  // printf("Traverse %d, forward=%d\n", cur, forward);

  int bound = cur + forward;
  if (bound>=D) return true;

  while(!que.empty()) {
    ISET::iterator sit = que.begin();
    int next = *sit;
    if (next>bound) return false;

    bool ok = traverse(next, cur);
    if (ok) return true;
  }
  return false;
}
*/

typedef map<int, int> IIMAP;
typedef set<int> ISET;
typedef pair<int, int> PII;
typedef deque<PII> Q;

IIMAP viles;
ISET untraversed;
Q q;

bool go() {
  while(!q.empty()) {
    PII pii = q.front();
    q.pop_front();

    int cur = pii.first;
    ISET::iterator sit = untraversed.find(cur);
    if (sit==untraversed.end())
      continue;
    untraversed.erase(sit);

    int last = pii.second;
    int dist = viles[cur];

    int forward = min(dist, cur-last);
    int bound = cur + forward;

    if (bound>=D) {
      return true;
    }

    for (sit=untraversed.begin(); sit!=untraversed.end(); ++sit) {
      int next = *sit;
      if (next>bound) {
        break;
      }
      PII item = PII(next, cur);
      q.push_back(item);
    }
  }
  return false;
}

void solve(int caseNum) {
  viles.clear();
  untraversed.clear();
  q.clear();

  int firstDist;

  cin>>N;
  REP(i, 0, N) {
    int dist, len;
    cin>>dist>>len;

    if (i==0) firstDist = dist;

    viles[dist] = len;
    untraversed.insert(dist);
  }
  cin>>D;

  PII start(firstDist, 0);
  q.push_back(start);

  bool ok = go();

  printf("Case #%d: %s\n", caseNum, ok?"YES":"NO");
}

int main() {
  unittest();

  int caseCount;
  cin>>caseCount;
  REP(i, 1, caseCount+1)
    solve(i);

  return 0;
}

void unittest() {
}

