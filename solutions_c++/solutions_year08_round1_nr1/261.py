#include <iostream>
#include <algorithm>
using namespace std;

long long T,  N;

long long X[800], Y[800], G[800][800];

int main() {
    
    freopen( "A-large.in", "r", stdin );
    freopen( "ans.txt", "w", stdout );
    
    cin >> T;
    for( long long t = 1; t <= T; ++t ) {
        cin >> N;
        for( long long i = 0; i < N; ++i )
            cin >> X[i];
        for( long long i = 0; i < N; ++i )
            cin >> Y[i];
        sort( X, X + N );
        sort( Y, Y + N );
        long long mx = 0;
        for( long long i = 0; i < N; ++i )
            mx += X[i] * Y[N-i-1];
        printf( "Case #%d: ", t );
        cout << mx << endl;
    }
    
    
}
