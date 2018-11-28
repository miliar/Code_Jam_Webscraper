#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef unsigned long long ull;

ull gcd( ull a, ull b )
{
    if ( a == 0 ) return b;
    if ( b == 0 ) return a;
    while ( true )
    {
        a = a % b;
        if ( a == 0 ) return b;
        b = b % a;
        if ( b == 0 ) return a;
    }
}

int main()
{
    int num_cases;
    cin >> num_cases;

    vector<ull> t(1000);
    vector<ull> diff(1000);

    for ( int case_num = 0; case_num < num_cases; case_num++ )
    {
        int N;
        cin >> N;
        for ( int i = 0; i < N; i++ )
            cin >> t[i];
        
        sort( t.begin(), t.begin()+N );

        for ( int i = 0; i < N-1; i++ )
            diff[i] = t[i+1] - t[i];

        for ( int i = 1; i < N-1; i++ )
            diff[0] = gcd( diff[0], diff[i] );

        cout << "Case #" << case_num + 1 << ": ";
        ull rem = t[0] % diff[0];
        if ( rem == 0 )
            cout << 0 << endl;
        else 
            cout << diff[0] - rem << endl;
    }

    return EXIT_SUCCESS;
}
