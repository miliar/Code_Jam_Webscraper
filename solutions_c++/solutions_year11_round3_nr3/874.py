
//Murugan Thunai !
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <fstream>  
using namespace std;

#define pb push_back
#define mp make_pair
#define v(x) vector< x >
#define sz size()
#define FOR(i, first, last) for (int i = (first); i != (last); ++i)
#define FORZ(i,n) FOR(i,0,n)
#define FORO(i,o) FORZ(i,((o).sz))
#define FOREACH(itr, x) for(__typeof(x.begin()) itr = x.begin(); itr != x.end(); itr++)
#define ALL(a) (a).begin(),(a).end()
#define SORT(a) sort(ALL(a))
#define ss stringstream
#define dbg(x) (cerr << #x << ": " << x<<'\n')
#define GI ({int t ; scanf("%d",&t);t;})
#define CLR(x, v) memset(x, v, sizeof(x));
typedef long long ll;
typedef unsigned long long ull;
typedef v(int) vi;
typedef v(vi) vvi;
typedef v(string) vs;
typedef v(vs) vvs;
typedef pair<int,int> ii;
typedef v(ii) vii;

#define MAX 1000000
int flag[MAX+1] = {0};
vector<int>prime;
void sieve()
{
  for(int i=2;i*i<=MAX;i++)
    if(!flag[i])
      for(int j=i*i;j<=MAX;j+=i)
        flag[j] = 1;
  prime.push_back(2);
  for(int i=3;i<=MAX;i+=2)
    if(!flag[i])
      prime.push_back(i);
}
int main()
{
  sieve();
  int T=GI;
  FOR(test,1,T+1)
  {
    int N = GI, L = GI, H = GI;
    ll p = 1;
    set<int> arr;
    FORZ(i, N)
    {
      int n = GI;
      for(int j=0;j<prime.size();j++)
        if(n%prime[j] == 0)
          arr.insert(prime[j]);
    }
    if(L == 1)
    {
      printf("Case #%d: 1\n", test);
      goto end;
    }
    FOREACH(itr, arr)
    {
      p *= (*itr);
      if(p > H)
      {
        printf("Case #%d: NO\n", test);
        goto end;
      }
    }
    dbg(p);
    if(p >= L && p <= H)
    {
      printf("Case #%d: %lld\n", test, p);
    }
    else
      printf("Case #%d: NO\n", test);
end:;
  }
	return 0;
}
//Powered by Siddharth
