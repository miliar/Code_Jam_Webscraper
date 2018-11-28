#include <iostream>
#include <vector>
using namespace std;

int main()
{
    size_t T;
    cin >> T;

    for ( size_t t = 0; t < T; ++t )
    {
        size_t N, K;
        cin >> N;
        cin >> K;
        vector< bool > snapper;
        snapper.reserve( N );
        size_t i;
        for ( i = 0; i < N; ++i )
        {
            snapper.push_back( false );
        }
        for ( i = 0; i < K; ++i )
        {
            size_t j = 0;
            while ( j < N && snapper[j] )
            {
                ++j;
            }
            size_t m;
            for ( m = 0; m < j ; ++m )
            {
                snapper[m] = false;
            }
            if ( j < N )
                snapper[j] = true;

        }
        for ( i = 0; i < N; ++i )
        {
            if ( ! snapper[i] )
                break;
        }
        if ( i == N )
            cout << "Case #" << t + 1 << ": " << "ON" << endl;
        else
            cout << "Case #" << t + 1 << ": " << "OFF" << endl;

    }
    return 0;
}
