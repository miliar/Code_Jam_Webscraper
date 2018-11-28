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

#define FOR(i,n)  for(int i=0;i<(int)(n);i++)
#define SZ(x) ((int)(x).size())
typedef long long ll_t;
typedef complex<ll_t> cmp_t ; 
ll_t outerProduct(cmp_t p, cmp_t q){ return imag(conj(p)*q); }

void solve()
{
  ll_t N,M,A;
  cin>>N>>M>>A;
  if(N*M<A) {
    puts("IMPOSSIBLE");
    return ;
  }
  {
    int x0 = 0 ;
    FOR(y0,M+1)
      {
        cmp_t p0(x0,y0);
        FOR(x1,N+1)
          {
            FOR(y1,M+1)
              {
                cmp_t p1(x1,y1);
                FOR(x2,N+1)
                  {
                    FOR(y2,M+1)
                      {
                        cmp_t p2(x2,y2);
                        ll_t area2 = outerProduct(p1-p0 , p2-p0);
                        if(area2<0) area2=-area2;
                        if(area2==A)
                          {
                            printf("%d %d %d %d %d %d\n",
                                   x0,y0,x1,y1,x2,y2);
                            return;
                          }
                      }
                  }
              }
          }
      }
  }
  puts("IMPOSSIBLE");
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
