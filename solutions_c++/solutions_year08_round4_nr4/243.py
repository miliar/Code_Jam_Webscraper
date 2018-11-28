#include<iostream>
#include<sstream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<vector>
#include<cmath>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<numeric>
#include<functional>
#include<complex>

using namespace std;

#define FOR(i,n)  for(ll_t i=0;i<(ll_t)(n);i++)
#define SZ(x) ((int)(x).size())
typedef long long ll_t;
typedef complex<ll_t> cmp_t ; 
ll_t outerProduct(cmp_t p, cmp_t q){ return imag(conj(p)*q); }

void solve()
{
  ll_t K ; string S;
  cin>>K>>S;
  vector<int> perm(K , 0);
  FOR(i,K) perm[i] = i ;
  ll_t ans = 1LL<<30;
  do
    {
      string S2;
      FOR(i,SZ(S))
        {
          int tp = i / K * K + perm[i%K];
          char c = S[tp];
          S2 += c;
        }
      S2.erase(unique(S2.begin() , S2.end()) , S2.end());
      ans <?= S2.size();
    }
  while(next_permutation(perm.begin() , perm.end()));
  cout << ans << endl;
}

int main()
{
  int t; 
  cin>>t;
  FOR(case_no,t)
    {
      printf("Case #%d: " , case_no + 1 );
      solve();
    }
  return 0 ;
}
