#include <iostream>
#include <algorithm>

using namespace std;

typedef long long int lli;

lli gcd(int a, int b)
{
  return b? gcd(b, a%b) : a;
}

lli lcm(lli a, lli b)
{
  return a / gcd( max(a, b), min(a, b) ) * b;
}

bool solve(lli n, lli pd, lli pg)
{
  if(pd != 100 && pg == 100)return false;
  if(pd != 0 && pg == 0)return false;

  lli div;

  lli Dw = pd;
  lli Dl = 100LL - pd;

  div = gcd( max(Dw, Dl), min(Dw, Dl) );

  Dw /= div;
  Dl /= div;

  lli today = Dw + Dl;
  if( n < today )return false;

  lli Gw = pg;
  lli Gl = 100LL - pg;
  
  div = gcd( max(Gw, Gl), min(Gw, Gl) );

  Gw /= div;
  Gl /= div;

  lli total = Gw + Gl; 

  return true;
}

int main(void)
{
  int tc, cnt = 0;
  cin >> tc;
  while( tc-- ){
    lli n, pd, pg;
    cin >> n >> pd >> pg;
    
    const string T = "Possible";
    const string F = "Broken";

    bool result = solve(n, pd, pg);    
    cout << "Case #" << ++cnt << ": " << (result ? T : F) << endl;
  }
  return 0;
}
