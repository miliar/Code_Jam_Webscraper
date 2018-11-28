#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <iterator>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <queue>
#include <vector>
using namespace std;
 
typedef long long LL;
 
#define MP make_pair
#define ST first
#define ND second
#define ALL(k) k.begin(),k.end()
#define PB push_back
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOREACH(i,v) for(__typeof((v).begin())i=(v).begin();i!=v.end();++(i))
#define SZ(a) (int)((a).size())

int main()
{
  int tst,tstn;
  cin >> tstn;
  REP(tst,tstn)
  {
    cout << "Case #" << tst+1 << ": ";
    LL r,k,n;
    cin >> r >> k >> n;
    vector <int> T(n);
    REP(i,n) cin >> T[i];
    map <vector <int> , pair<LL,int> > M;
    LL cash = 0;
    LL rb = 0;
    bool done = false;
    while( M.find(T) == M.end())
    {
      M[T] = MP(cash,rb);
      if( rb == r) { cout << cash << endl; done = true; break; }
      vector <int> tmp (n);
      int j=0;
      int now = 0;
      for(j = 0;j<n;j++)
      {
        if(now + T[j] > k) break;
        now+=T[j];
      }
      cash+=(LL)now;
      int t=0;
      for(int i=j;i<n;i++) tmp[t++] = T[i];
      REP(i,j) tmp[t++] = T[i];
      T = tmp;
      rb++;
    }
    if(done) continue;    
    if( rb == r) { cout << cash << endl; done = true; continue; }

    r-=rb;
    pair <LL, int> P = M[T];
    int mod = rb- P.ND;
    LL add = cash - P.ST;
    cash+= add*(LL)(r/mod);
    REP(i,r%mod)
    {
      vector <int> tmp (n);
      int j=0;
      int now = 0;
      for(j = 0;j<n;j++)
      {
        if(now + T[j] > k) break;
        now+=T[j];
      }
      cash+=(LL)now;
      int t=0;
      for(int i=j;i<n;i++) tmp[t++] = T[i];
      REP(i,j) tmp[t++] = T[i];
      T = tmp;    
    
    }
    cout << cash << endl;
    
  }
  return 0;
}
