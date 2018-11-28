#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#define FOR(a,b,c) for(int (a) = (b), _n = (c); (a) <= _n ; (a)++)
#define FORD(a,b,c) for(int (a) = (b), _n = (c) ; (a) >= _n ; (a)--)
#define FOR_N(a,b,c,n) for(int (a) = (b), _m = (n), _n = (c) ; (a) <= _n ; (a)+= _m )
#define FORD_N(a,b,c,n) for(int (a) = (b), _m = (n), _n = (c) ; (a) >= _n ; (a)-= _m)
#define EACH(v,it) for(__typeof(v.begin()) it = v.begin(); it != v.end() ; it++)
#define INF 200000000
#define MAX 1

using namespace std;

int main()
{
  freopen("Clarge.out","w",stdout);
  freopen("C-large.in","r",stdin);
  int t;
  scanf("%d",&t);
  FOR(ca,1,t)
  {
    long long n,total = 0;
    long long mins = INF,total2 = 0;
    cin >> n;
    while(n--)
    {
      long long a;
      cin >> a;
      total += a;
      total2 ^= a;
      mins = min (a,mins);
    }
    printf("Case #%d: ",ca);
    if(total2 != 0) puts("NO");
    else cout << total - mins << endl;
  }
  return 0;
}
