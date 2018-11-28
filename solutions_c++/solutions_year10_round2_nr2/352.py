#include <iostream>
#include <vector>
using namespace std;

bool can( int p, int v, int obj, int time )
{
    if ( 1.0*(obj-p) / v <= time ) return true;
    return false;
}

int main()
{
    int t; cin >> t;
    for (int caso = 0; caso < t; ++caso)
    {
        int n, k, b, t;
        cin >> n >> k >> b >> t;
        vector<int> pos(n);
        for (int i = 0; i < n; ++i)
            cin >> pos[i];
        vector<int> vel(n);
        for (int i = 0; i < n; ++i)
            cin >> vel[i];
        
        vector<bool> ok(n);
        for ( int i = 0; i < n; ++i )
            ok[i] = can( pos[i], vel[i], b, t );
        
        int cont = 0;
        for ( int i = 0; i < n; ++i )
            if ( ok[i] ) ++cont;
        
        if ( cont < k )
        {
            cout << "Case #" << caso+1 << ": IMPOSSIBLE" << endl;
            continue;
        }
        
        int trocas = 0;
        for ( int i = n-1; i > n-1-k; --i )
        {
            if ( ok[i] ) continue;
            
            for ( int j = i-1; j >= 0; --j )
                if ( ok[j] )
                {
                    trocas += (i-j);
                    ok[i] = true;
                    ok[j] = false;
                    break;
                }
        }
        cout << "Case #" << caso+1 << ": " << trocas << endl;
        
    }
}
