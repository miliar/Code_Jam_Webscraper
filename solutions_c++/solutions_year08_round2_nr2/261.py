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
#define ALL(x) (x).begin(),(x).end()
#define MP make_pair
typedef long long ll_t;
typedef long double ld_t;
typedef vector<int> VI;
typedef vector<VI> VVI;

vector<ll_t> g_prime;
bool flg[10000] ;
void setup(int n)
{
  fill_n(flg , n+1 , true);
  g_prime.clear() ; 
  for(int i=2;i<=n;i++){
    if(!flg[i]) continue;
    g_prime.push_back(i); 
    for(int j=i+i;j<=n;j+=i){
      flg[j]=false;
    }
  }
}


set<int> factor(int n)
{
  set<int> ret;
  FOR(i,SZ(g_prime))
    {
      int x = g_prime[i];
      if(n < x) break;
      int cnt = 0;
      while(n % x == 0){
        n /= x;
        cnt++;
      }
      if(cnt>0){
        ret.insert(x);
      }
    }
  return ret;
}

int main()
{
  int t; 
  cin>>t;
  setup(1001);
  FOR(case_no,t)
    {
      ll_t A,B,P;
      cin>>A>>B>>P;
      ll_t ans = B-A+1;
      vector<set<int> > dat;
      FOR(i,ans){
        dat.push_back(factor(i+A));
      }
      bool yet = true;
      while(yet)
        {
          yet = false;
          FOR(i,SZ(dat)) FOR(j,i)
            {
              vector<int> ins;
              set_intersection(ALL(dat[i]) , ALL(dat[j]) , back_inserter(ins));
              bool ok = false;
              FOR(a,SZ(ins)){
                if(P <= ins[a]){
                  ok = true; 
                  break;
                }
              }
              if(ok){
                dat[j].insert(ALL(dat[i]));
                dat.erase(dat.begin() + i);
                yet = true;
                break;
              }
            }
        }
      ans = SZ(dat);
      printf("Case #%d: %lld\n" , case_no + 1 , ans);
    }
  return 0 ;
}
