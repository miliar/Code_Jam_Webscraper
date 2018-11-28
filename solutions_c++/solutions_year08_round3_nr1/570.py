#include <map>
#include <vector>
#include <list>
#include <algorithm>
#include <string>
#include <iostream>

using namespace std;

#define FOR(x,N) for(large x=0; x<N; x++)

#define GET(x) cin >> x;
#define GETt(T,x) T x; cin >> x;

#define SORT(A) sort(A.begin(), A.end());
#define RSORT(A,T) sort(A.begin(), A.end(), greater<T>());

#define DEBUG_TRACE(x) cout << #x "=" << x << endl;
//#define DEBUG_TRACE(x)

typedef long long large;
typedef long double real;


int main()
{
  GETt(int, prob);

  FOR(iii,prob)
  {
    GETt(int, P);
    GETt(int, K);
    GETt(int, L);

    vector<long> freq(L);

    FOR(zzz,L) GET(freq[zzz]);

    large cnt=0;
    int mlt=1;
    int delta=1;
    large idx=0;
    vector<large> keycnt(K,0);

    RSORT(freq, long);
    vector<long>::iterator iter;
    FOR(zzz,L)
    {
      keycnt[idx]+= (freq[zzz]*mlt);
//cout << "keycnt[" << idx << "]=" << keycnt[idx] <<endl;
      idx+=delta;
      if(idx==K || idx==-1)
      {
        delta= (-delta);
        ++mlt;
        idx+=delta;
      }
    }

    FOR(zzz,K) cnt+=keycnt[zzz];

    cout << "Case #" << iii+1 << ": " << cnt << endl;
  }

  return 0;
}
