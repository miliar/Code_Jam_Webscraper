#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int t;
    cin >> t;
    
    int n, k;
    for (int caso = 1; caso <= t; ++caso)
    {
        cin >> n >> k;
        
        double d = pow( 2.0, (double)n );
        unsigned u = (unsigned)d;
        
        cout << "Case #" << caso << ": ";
        if ( (k+1)%u == 0 )
            cout << "ON" << endl;
        else
            cout << "OFF" << endl;
    }
    
}
