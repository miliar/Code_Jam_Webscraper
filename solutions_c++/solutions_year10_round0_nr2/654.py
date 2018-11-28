#include <iostream>

using namespace std;

#define forn(i,n) for (int (i)=0; (i) < (n); (i)++)
typedef long long tint;
tint n, tt, m;
tint x[1024], y[1024];

tint mcd(tint a, tint b){ return (a==0)?b:mcd(b %a, a);}
tint miabs(tint a){ return (a>=0)?a:-a;}

int main(){
    freopen("B-small.in", "r", stdin);
    freopen("B-small.out", "w", stdout);
    cin >> tt;
    forn(t,tt)
    {
        cin >> n;
        forn(i,n) cin >> x[i];
        forn(i,n-1) y[i+1] = miabs(x[i+1] - x[0]);
        m = y[1];
        forn(i,n-2) m = mcd(m, y[i+2]);
        tint z = m - ((x[0]%m)+m)%m;
        if (z==m) z=0;
        cout << "Case #" << t+1 << ": " << z << endl;
    }
    return 0;
}
