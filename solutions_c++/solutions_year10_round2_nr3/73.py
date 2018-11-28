#include <iostream>
using namespace std;
const long long mm = 100003;
long long C[600][600];
long long a[600][600], b[600];
int i, j, cn, k, ci, n;

int main()
{
    freopen( "C-large.in", "r", stdin );
    freopen( "C-large.out", "w", stdout );
    memset( C, 0, sizeof(C) );
    C[0][0] = 1;
    for ( i = 1; i <= 500; i++ )
    for ( j = 0; j <= i; j++ ) C[i][j] = (C[i-1][j-1]+C[i-1][j])%mm;
    scanf( "%d", &cn );
    a[2][1] = 1;
    for ( i = 3; i <= 500; i++ )
    {
        a[i][1] = 1;
        for ( j = 2; j < i; j++ )
        {
            a[i][j] = 0;
            for ( k = 1; k < j; k++ )
                a[i][j] = (a[i][j]+a[j][k]*C[i-j-1][j-k-1])%mm;
        }
    }
    for ( i = 2; i <= 500; i++ )
    {
        b[i] = 0;
        for ( j = 1; j < i; j++ ) b[i] = (b[i]+a[i][j])%mm;
    }
    //for ( i = 2; i <= 250; i++ ) cout << i << ' ' << b[i] << endl;

    for ( ci = 1; ci <= cn; ci++ )
    {
        scanf( "%d", &n );
        cout << "Case #" << ci << ": " << b[n] << endl;
    }

    return 0;
}
