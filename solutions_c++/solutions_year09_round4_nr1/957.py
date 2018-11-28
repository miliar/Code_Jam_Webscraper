#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

#define REP(x, n) for(int x = 0; x < (n); ++x)
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define VAR(v, n) typeof(n) v = (n)
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define SIZE(x) ((int)(x).size())
#define PB push_back
#define PF push_front
#define MP make_pair
#define FI first
#define SE second

const int INF = 1000000001;
const double EPS = 10e-9;

const int Max = 50;
int zz,wyn,n,x,t[Max];
char h;

int main() {

scanf("%d", &zz);
FOR(z,1,zz) {
  scanf("%d", &n);
  FOR(i,1,n) {
    x=0;
    FOR(j,1,n) {
      scanf(" %c", &h);
      if(h=='1') x=j;
    }

    t[i]=x;
  }

  wyn=0;
  FOR(i,1,n-1) if(t[i]>i) {
    x=0;
    FOR(j,i+1,n) if(t[j]<=i) {x=j; break;}
    while(i<x) {
      swap(t[x-1], t[x]); wyn++;
      x--;
    }
  }
    

  printf("Case #%d: %d\n", z, wyn);
}

return 0;
}
