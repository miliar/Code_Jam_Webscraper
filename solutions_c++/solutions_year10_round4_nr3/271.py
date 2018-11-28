#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <set>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <fstream>
#include <numeric>
#include <limits.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> ii;

#define ITE(v) typeof(v.begin())
#define FOR(i,n) for(int i = 0; i < n; i++)
#define FORIT(it,v) for(ITE(v) it = v.begin(); it != v.end(); it++)
#define ALL(v) v.begin(), v.end()
#define SZ(v) int(v.size())
#define pb push_back
#define SQR(a) ((a)*(a))
#define OK(y,x) (y >= 0 && y < n && x >= 0 && x < m)

#define INF 0x3f3f3f3f
#define EPS (1e-8)

inline int cmp(double a, double b = 0.0) {
  if (fabs(a-b) <= EPS) return 0;
  if (a < b) return -1;
  return 1;
}


set<ii> s[2];


int main() {
  int ntests;
  scanf("%d",&ntests);
  FOR(kk,ntests) {
    s[0].clear();
    s[1].clear();
    printf("Case #%d: ",kk+1);
    int n;
    cin >> n;
    int x1, y1, x2, y2;
    FOR(k,n) {
      cin >> x1 >> y1 >> x2 >> y2;
      if (x2 < x1) swap(x1,x2);
      if (y2 < y1) swap(y1,y2);
      for (int i = x1; i <= x2; i++) {
        for (int j = y1; j <= y2; j++) {
          s[0].insert(ii(i,j));
        }
      }
    }
    int atual = 0;
    int ot = 1;
    int cnt = 0;
    while (!s[atual].empty()) {
      cnt++;
      s[ot].clear();
      FORIT(it,s[atual]) {
        int y = it->first;
        int x = it->second;
        if (s[atual].count(ii(y-1,x+1))) {
          s[ot].insert(ii(y,x+1));
        }
        if (s[atual].count(ii(y+1,x))) {
          s[ot].insert(ii(y+1,x));
        }
        if (s[atual].count(ii(y,x+1))) {
          s[ot].insert(ii(y,x+1));
        }
      }
      swap(atual,ot);
    }
    cout << cnt << endl;
  }  
  return 0;
}
