#include <iostream>
using namespace std;
int main()
{
    freopen( "a.in" , "r" , stdin );
    freopen( "a.out", "w" , stdout ); 
    long long n,m,case_n;
    cin >> case_n;
    for ( int k  = 1 ; k <= case_n ; ++ k )
    {
        bool able = true;
        cin >> n >> m;
        ++ m;
        for ( int i = 0 ; i < n ; ++ i )
        {
            if ( m % 2 == 1 )
            {
                 able = false;
                 break;
            }
            m /= 2;
        }
        cout << "Case #"<< k <<": ";
        if ( able )
           cout << "ON\n";
           else
           cout << "OFF\n";
    }
    return 0;
}
