#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <iostream>
#include <map>
#include <cmath>
#include <set>
#include <queue>
#include <cstring>
#include <fstream>
using namespace std;
typedef long long LL;

#define INF 2000000000
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++)
#define FS first
#define SD second
#define MP make_pair

vector<pair<int,int> > walls;
set<int> S[10000];
int n,m;
int IND;

void go(int idx) {
 // printf("A %d\n",idx);
  FOR(i,0,m) {
    int a = walls[i].FS;
    int b = walls[i].SD;
    //printf("%d %d\n",a,b);
    if (S[idx].count(a) && S[idx].count(b)) {
      S[IND].insert(a);
      S[IND+1].insert(a);
      S[IND].insert(b);
      S[IND+1].insert(b);
      int s = (a+1)%n;

      while (s!=b) {
        if (S[idx].count(s)) {
          S[IND].insert(s);
        }
        s = (s+1)%n;
      }
      s = (s+1)%n;
      while (s!=a) {
        if (S[idx].count(s)) {
          S[IND+1].insert(s);
        }
        s = (s+1)%n;
      }
      int p = IND;
      if (S[IND].size() > 2 && S[IND+1].size() > 2) {
        IND += 2;
        S[idx].clear();
        go(p);go(p+1);
        return;
      }
      else {
        S[IND].clear();
        S[IND+1].clear();
      }

    }
  }
}

int V[5000];
int U[5000];
vector<set<int> > v;
int col[10];
int C[10];
int ret;
bool is[10];
bool is2[10];
void go2(int idx) {
  if (idx == n) {
    int p = 0;
    FORE(i,1,5) is[i] = false;
    FOR(i,0,n) is[col[i]] = true;
    FORE(i,1,5) {
      if(is[i]) ++p;
    }
    if (p>ret) {
      bool ok = true;
      FOR(i,0,SZ(v)) {
        set<int>::iterator it = v[i].begin();
        FORE(j,1,5) is2[j] = false;
        while (it != v[i].end()) {
          is2[col[*it]] = true;
          ++it;
        }
        FORE(j,1,5) if(is[j] != is2[j]) ok = false;
        if(!ok) break;
      }
      if (ok) {
        ret = p;
        FOR(i,0,n) C[i] = col[i];
      }
    }
  }
  else {
    FORE(i,1,5) {
      col[idx] = i;
      go2(idx+1);
    }
  }
}

int main() {
  int t;scanf("%d",&t);
  FORE(test,1,t) {
    IND = 1;
    scanf("%d%d",&n,&m);
    FOR(i,0,m) scanf("%d",&V[i]);
    FOR(i,0,m) scanf("%d",&U[i]);
    walls.clear();
    FOR(i,0,m) {
      walls.push_back(MP(V[i]-1,U[i]-1));
    }
    FOR(i,0,10000) S[i].clear();
    FOR(i,0,n) S[0].insert(i);
    go(0);
    FOR(i,0,10000) {
      if(!S[i].empty()) {
        v.push_back(S[i]);

      }
    }
    ret = 0;
    if (v.size() == 1) {
      ret = n;
      FORE(i,1,n) C[i-1] = i;
    }
    else {
      go2(0);
    }
    printf("Case #%d: %d\n", test, ret);
    FOR(i,0,n) printf("%d ", C[i]);
    printf("\n");
    v.clear();
  }

}
