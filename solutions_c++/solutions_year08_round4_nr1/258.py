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

struct node
{
  bool isleaf;
  bool isAnd ; // for internal
  bool changable ; 
  bool val   ; // for leaf
};
ll_t INF = 1LL<<30;
ll_t memo[20010];
node dat[20010];

ll_t dfs(int pos)
{
  ll_t &ret = memo[pos];
  if(ret != -1) return ret;
  ll_t val = INF;
  node x = dat[pos];
  if(x.isleaf)
    {
      if(x.val) return 0 ;
      return INF;
    }
  else
    {
      int c1 = 2*pos;
      int c2 = 2*pos+1;
      if(x.changable)
        {
          ll_t v1 = dfs(c1);
          ll_t v2 = dfs(c2);
          {
            ll_t andcost = v1 + v2;
            if(x.isAnd==false) 
              andcost++;
            val <?= andcost;
          }
          {
            ll_t orcost = min(v1 , v2);
            if(x.isAnd==true) 
              orcost++;
            val <?= orcost;
          }
        }
      else
        {
          if(x.isAnd)
            {
              ll_t v1 = dfs(c1);
              ll_t v2 = dfs(c2);
              val <?= v1+v2;
            }
          else
            {
              ll_t v1 = dfs(c1);
              ll_t v2 = dfs(c2);
              val <?= min(v1,v2);
            }
        }
    }
  return ret=val;
}

void solve()
{
  int M , V;
  cin>>M>>V;
  memset(memo , -1 , sizeof(memo));
  int pos = 1 ;
  bool turn = V==0;
  FOR(_,(M-1)/2)
    {
      int G , C;
      cin>>G>>C;
      
      dat[pos].isleaf = false;
      dat[pos].isAnd = G ^ turn;
      dat[pos].changable = C ;
      pos++;
    }
  FOR(_,(M+1)/2)
    {
      int L ; 
      cin>>L;
      
      dat[pos].isleaf = true;
      dat[pos].val = L ^ turn;
      pos++;
    }
  ll_t ans = dfs(1);
  if(ans > INF/2) puts("IMPOSSIBLE");
  else
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
