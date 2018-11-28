#include <cstdio>
#include <iostream>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <string>
#include <vector>

using namespace std;

long long mul( long long a, long long b )
{
    a *= b;
    if( a>100003 )
        a %= 100003;
    return a;
}
long long add( long long a, long long b )
{
    a += b;
    if( a>100003 )
        a %= 100003;
    return a;
}

long long C[501][251];
long long cmb( long long a, long long b )
{
//    cout << "solving.. " << a << ", " << b << endl;
    if( a>500 ) {
  //      cout << "foul" << endl;
        return 0xFFFFFFFF;
    }
    if( a < 0 ) {
        return 0;
    }
    if( a < b ) {
    //    cout << "foul" << endl;
        return 0;
    }
    if( a == b ) {
//        cout << "a=b" << endl;
        return 1;
    }
    if( b == 0 ) {
  //      cout << "b=0" << endl;
        return 1;
    }
    if( (b<<1) > a ) {
    //    cout << "b=a-b" << endl;
        b = a - b;
    }
    if( b == 1 ) {
      //  cout << "b==1" << endl;
        return a;
    }
        
    if( C[a][b] != 0xFFFFFFFF ) {
        return C[a][b];
    }
    //else if( C[a][b] == 0xFFFFFFFF ) {
    //cout << "find: ( " << a-1 << ", " << b << " )   ( " << a-1 << ", " << b-1 << " )" << endl;
    long long x = cmb( a-1, b );
    long long y = cmb( a-1, b-1 );
//    cout << "(x,y) =" << x << ", " << y << endl;
    x = add( x, y );
//    cout << x << endl;
    C[a][b] = x;
    return C[a][b];
}

long long r[501][501][3];
long long p[501];

int main()
{
    for( int i=0; i<501; i++ )
        for( int j=0; j<251; j++ )
            C[i][j] = 0xFFFFFFFF;
            
    for( int i=0; i<501; i++ ) {
        for( int j=0; j<=i; j++ ) {
            cmb( i, j );
        }
    }

    r[2][0][0] = 1;
    r[2][0][1] = 2;
    r[2][0][2] = 1;
    
    for( long long i=3; i<501; i++ ) {
        r[i][0][0] = 1;
        r[i][0][1] = i;
        r[i][0][2] = 1;
        for( long long j=1; j<i-1; j++ ) {
            r[i][j][0] = j+1;
            r[i][j][1] = i;
            long long sum = 0;
            long long a = i-j-2, b=j-1, k=0;
            for( ; ; ) {
                sum = add( sum, mul( cmb(a, b), r[j+1][k][2] ) );
                if( b>0 ) {
                    b--; k++;
                } else {
                    break;
                }
            }
            r[i][j][2] = sum;
        }
    }
    for( long long i=2; i<501; i++ ) {
        p[i] = 0;
        for( long long j=0; j<i-1; j++ ) {
            p[i] = add( p[i], r[i][j][2]);
//            cout << r[i][j][2] << " ";
        }
//        cout << endl;
    }
  /*  cout << p[2] << endl;
    cout << p[3] << endl;
    cout << p[4] << endl;
    cout << p[5] << endl;
    cout << p[6] << endl;
    cout << p[7] << endl;
    return 0;
    */
    int T;
    
    cin >> T;

    for(int i=1; i<=T; i++) {
        int N;
        cin >> N;
        cout << "Case #" << i << ": " << p[N] << endl;
    }
    
    //cin >> T;
    return 0;
}
