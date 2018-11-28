#include <iostream>
#include <vector>

using namespace std;

#define forn(i,n) for(int i=0;i<(n);i++)
#define forab(i,a,b) for(int i=(a);i<(b);i++)

#define ll long long

inline ll area(ll x1,ll y1, ll x2, ll y2, ll x3, ll y3)
{
  return abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2);
}

int main()
{
    int C;
    cin >> C;
    forn(casos,C)
    {
        int N,M,A;
        cin >> N >> M >> A;
        N++;
        M++;
        cout << "Case #" << casos+1<<": ";
        forn(x1,N)
        forab(x2,x1,N)
        forn(y1,M)
        forn(y2,M)
        {
         int x3 = 0,y3 = 0;
         if (A == area(x1,y1,x2,y2,x3,y3))
         {
          cout << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << y3;
          goto final;
         }
        }
        cout << "IMPOSSIBLE";
final:
        cout << endl;
    }
    return 0;
}
