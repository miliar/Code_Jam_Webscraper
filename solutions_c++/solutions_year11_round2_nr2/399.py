#include <iostream>
#include <algorithm>

#define forn(i,n) for(int i = 0; i < n; ++i)
#define forab(i,a,b) for(int i = a; i <= b; ++i)

using namespace std;

int x[1200000], cnt, n, d;

bool f(double t){
    double z = x[0] - t + d;
    forn(i, cnt)
        if(i){
            if(x[i] + t < z)
                return 0;
            z = max(z, x[i] - t) + d;
        }
    return 1;
}

int main()
{
    int T;
    cin >> T;
    cout << fixed;
    cout.precision(8);
    forn(t, T){
        cin >> n >> d;
        cnt = 0;
        forn(i, n){
            int xi, pi;
            cin >> xi >> pi;
            forn(t, pi)
                x[cnt++] = xi;
        }
        double l = 0, r = 1e11;
        while( r - l > 1e-9 )
            if( f( (l + r) / 2) )
                r = (l + r) / 2;
            else
                l = (l + r) / 2;
        cout << "Case #" << t + 1 << ": " << l << endl;
    }
    return 0;
}
