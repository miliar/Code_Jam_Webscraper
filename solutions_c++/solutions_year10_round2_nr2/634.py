#include <iostream>
#include <string>
#include <map>

using namespace std;

typedef long long tint;

#define forn(i,n) for(int (i)=0; (i) < (n); (i)++)

#define EPS 0.0000000001

tint tt,n,k,b,tim,cant,coste;
tint x[64], v[64];
long double ti[64];

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    cin >> tt;
    forn(t,tt)
    {
        cin >> n >> k >> b >> tim;
        forn(i,n)
        {
            cin >> x[i];
        }
        forn(i,n)
        {
            cin >> v[i];
        }
        forn(i,n)
        {
            ti[i] = (double)(b-x[i])/(double)v[i];
        }
        cant = 0;
        coste = 0;
        forn(i,n)
        {
            if (ti[n-i-1]-EPS < tim)
            {
                cant++;
                if (cant == k) break;
            }
            else
            {
                coste += k-cant;
            }
        }
        cout << "Case #" << t+1 << ": ";
        if (cant < k)
        {
                cout << "IMPOSSIBLE" << endl;
        }
        else
        {
            cout << coste <<  endl;
        }
    }
}
