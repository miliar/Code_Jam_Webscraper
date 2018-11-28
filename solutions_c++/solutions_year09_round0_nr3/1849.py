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

const string txt = "welcome to code jam";
const int dt = 19, t[] = {4,3,4,2,4,3,4,5,1,4,5,3,4,2,4,5,3,4,5};
const int MOD = 10000, Max = 600; 

int zz, k, dq, wyn;
char q[Max], f[Max];

int Func(int x, int y, int a, int b) {
  int s, w=0;

  if(a>b) w=1; else
  if(a==b) {
    FOR(i,x,y) if(q[i]==txt[a]) w++;

  } else {
    s=0; FOR(i,a,b) if(s==0 || t[s]>t[i]) s=i;

    FOR(i,x,y) 
      if(q[i]==txt[s]) w = (w + (Func(x,i-1,a,s-1) * Func(i+1,y,s+1,b))) % MOD;
  }

  return w%MOD;
}

int main() {

scanf("%d", &zz);
FOR(z,1,zz) {
  scanf(" %[^\n]", f);
  
  dq=k=0;
  while(f[k]) {
    if(txt.find(f[k]) != string::npos) q[dq++]=f[k];
    f[k++]=0;
  }

  wyn=Func(0, dq-1, 0, dt-1);

  printf("Case #%d: %04d\n", z, wyn);
}


return 0;
}
