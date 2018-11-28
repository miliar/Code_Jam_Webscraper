#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <cmath>

using namespace std;

typedef long long int int64;
typedef vector<int> VI;
#define REP(i,a,b) for (int i=int(a); i<int(b); ++i)
void unittest();

int R, C, D;
int64 a[500][500];
int64 sr[501][501];
int64 sc[501][501];
int64 fac[500];

int best;

void dmp(int64 ss[501][501]) {
  REP(i, 0, R+1) {
    REP(j, 0, C+1) {
      printf("%2lld", ss[i][j]);
    } printf("\n");
  }
}

bool attempt(int x, int y, int sz) {
  // printf("Trying %d %d %d\n", x, y, sz);
#if 0
  REP(i, x, x+sz) {
    REP(j, y, y+sz) {
      if ( (i==x||i==x+sz-1) && (j==y||j==y+sz-1) ) continue;
      printf("%d %d\n", i, j);
    }
  }
#endif
  if (sz%2==1) {
    int64 mid = (sz-1)/2;
    REP(i, 0, sz) {
      fac[i] = i-mid;
      // cout<<fac[i]<<endl;
    }
  } else { //even
    int64 ff = (sz-1)*-1;
    REP(i, 0, sz) {
      fac[i] = ff;
      // cout<<fac[i]<<endl;
      ff += 2;
    }
    // cout<<"--\n";
  }

  int64 bal = 0;
  REP(i, x, x+sz) {
    int64 v;
    if (i==x||i==x+sz-1)
      v = sr[i+1][y+sz-1] - sr[i+1][y+1];
    else
      v = sr[i+1][y+sz] - sr[i+1][y];
    // cout<<i<<" "<<v<<endl;
    // cout<<"*"<<y+sz-1<<" "<<y+1<<endl;
    bal += v*fac[i-x];
  }
  if (bal!=0) return false;

  bal = 0;
  REP(j, y, y+sz) {
    int64 v;
    // cout<<y+sz-1<<" "<<y+1<<endl;
    if (j==y||j==y+sz-1)
      v = sc[x+sz-1][j+1] - sc[x+1][j+1];
    else
      v = sc[x+sz][j+1] - sc[x][j+1];
    // cout<<v<<endl;
    bal += v*fac[j-y];
  }
  if (bal!=0) return false;
  // printf("GOAL! %d %d %d\n", x, y, sz);
  return true;
}

void solve(int caseNum) {
  cin>>R>>C>>D;
  best = 0;

  REP(i, 0, R) {
    char buf[600];
    cin>>buf;
    REP(j, 0, C) {
      a[i][j] = buf[j]-'0';
      sr[i][j] = sc[i][j] = 0;
    }
  }

  REP(i, 1, R+1) {
    REP(j, 1, C+1) {
      sr[i][j] = sr[i][j-1];
      sr[i][j] += a[i-1][j-1];
    }
  }
  REP(j, 1, C+1) {
    REP(i, 1, R+1) {
      sc[i][j] = sc[i-1][j];
      sc[i][j] += a[i-1][j-1];
    }
  }
  // dmp(sr);
  // dmp(sc);
  REP(sz, 3, min(R, C)+1) {
    REP(i, 0, R-sz+1) {
      REP(j, 0, C-sz+1) {
        if(attempt(i, j, sz)) {
          best = max(best, sz);
        }
      }
    }
  }

  if (best>0)
    printf("Case #%i: %d\n", caseNum, best);
  else
    printf("Case #%i: IMPOSSIBLE\n", caseNum);
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

