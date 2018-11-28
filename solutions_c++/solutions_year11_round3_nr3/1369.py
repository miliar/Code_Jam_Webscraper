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
#define MAX 10100

using namespace std;

long long n,l,h;
long long data[MAX];

long long gcd(long long a,long long b)
{
  return (b == 0)?a:gcd(b,a%b);
}

long long lcm(long long a, long long b)
{
  return  a * b/ gcd(a,b);
}

int main()
{
  freopen("C-small-attempt4.in","r",stdin);
  freopen("C.out","w",stdout);
  int t;
  scanf("%d",&t);
  FOR(ca,1,t)
  {
    cin >> n >> l >> h;
    long long val = -1;
    FOR(i,0,n-1)
    {
      cin >> data[i];
    }
    sort(data,data+n);
    FOR(i,l,h)
    {
      bool test = true;
      FOR(j,0,n-1)
      {
        if(data[j] % i != 0 && i % data[j] != 0)
        {
          test = false;
          break;
        }
      }
      if(test == true) 
      {
        val = i;
        break;
      }
    }
    printf("Case #%d: ",ca);
    //cout << val << endl;
    if(val == -1) cout << "NO" << endl;
    else cout << val << endl;
  }
  return 0;
}
