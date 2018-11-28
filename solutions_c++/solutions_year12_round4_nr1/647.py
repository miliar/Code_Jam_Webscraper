#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <map>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define REPR(i,n) for(int i=(n-1);i>=0;--i)
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define FORR(i,z,n) for (int (i)=(n-1);(i)>=(z);--(i))
#define FOREACH(it,c) \
  for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define MP make_pair
#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define UNIQUE(x) remove(unique((x).begin(),(x).end()),(x).end())
#define CLEAR(x,v) memset((x),(v),sizeof((x)))
#define FORS(i,x) for(int i=0;i<(int)(x).size();i++)

int n;
int d[10000];
int l[10000];
int h[10000];
int D;

bool reach(int i, int w) {
  w=min(w,l[i]);
  if (w<=h[i]) return false;
  h[i]=w;
  int dd=d[i]+w;
  if (dd>=D) return true;
  for (int j=i+1;j<n && d[j]<=dd; ++j) {
    if (reach(j,d[j]-d[i])) return true;
  }
  return false;
}

int main() {
  int T;
  cin >> T;
  FORE(tcase,1,T) {
    cin >> n;
    FOR(i,0,n) cin >> d[i] >> l[i];
    memset(h,0,sizeof(h));
    cin >> D;
    cout << "Case #" << tcase << ": " << (reach(0,d[0])?"YES":"NO") << endl;
  }
}



