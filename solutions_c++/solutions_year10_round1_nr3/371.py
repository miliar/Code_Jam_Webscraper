#include <iostream>
#include <cstring>
using namespace std;
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define For(i,a,b) for (int i=(a); i<(b); i++)
#define Rep(i,n) For((i),0,(n))
#define Fore(it,x) for (typeof((x).begin()) it=(x).begin(); it!=(x).end(); it++)
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define Clear(x,with) memset((x), (with), sizeof((x)))
#define sz size()
typedef long long ll;

ll a1, a2, b1, b2;
ll ans;

void init()
{
     cin >> a1 >> a2 >> b1 >> b2;
     ans = 0;
}

bool check(ll x, ll y)
{
     if (x == y)
          return false;
     else if (y % x == 0)
          return true;
     else if (y-x > x)
          return !check(y%x, x) || !check(x, y%x+x);
     else
          return !check(y-x, x);
}

void calc()
{
     For (i, a1, a2+1)
     {
          For (j, b1, b2+1)
          {
               if (check(min(i, j), max(i, j)))
                    ans++;
          }
     }
}

int main(int argc, char *argv[])
{
     int t;
     cin >> t ;
     For (i, 1, t+1)
     {
          init();
          calc();
          cout << "Case #" << i << ": " << ans << endl;
          
     }
     return 0;
}
