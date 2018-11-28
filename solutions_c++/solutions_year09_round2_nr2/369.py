# include <iostream>

using namespace std;

int n;
string a;
string b;
string res1;
int cnt[ 10 ];

int findFirstLeft( int x )
{
    for ( int i = x; i <= 9; i++ )
        if ( cnt[ i ] > 0 )
           return i;

    return -1;
}

bool findFirst( string a, int x, bool q )
{
       if ( x == n )
          return res1 > a;

       if ( q )
       {
            for ( int i = 0; i <= 9; i++ )
                for ( int j = 0; j < cnt[ i ]; j++ )
                    res1 += string( 1, i+'0' );

            return 1;
       }

       int t = a[ x ] - '0';
       int k = findFirstLeft( t );
       if ( x == 0 && t == 0 )
        k = findFirstLeft( t+1 );

       if ( k == -1 )
          return false;

       if ( k > t )
       {
            res1 += string( 1, k+'0' );
            cnt[ k ]--;

            return findFirst( a, x+1, 1 );
       }
       else
       {
           res1 += string( 1, k+'0' );
           cnt[ k ]--;

           if ( findFirst( a, x+1, 0 ) )
              return 1;

           cnt[ k ]++;
           res1.erase( res1.size()-1 );
           int k = findFirstLeft( t+1 );
           if ( x == 0 && t == 0 )
            k = findFirstLeft( t+2 );

           if ( k == -1 )
              return 0;

           res1 += string( 1, k+'0' );
           cnt[ k ]--;

           return findFirst( a, x+1, 1 );
       }
}

int test;

int main()
{
    scanf( "%d", &test );

    for ( int testnum = 1; testnum <= test; testnum++ )
    {
        cin >> a;
        b = a;
        n = b.size();

        res1 = "";

        memset( cnt, 0, sizeof( cnt ) );
        for ( int i = 0; i < n; i++ )
            cnt[ b[ i ] - '0' ]++;

        if ( !findFirst( a, 0, 0 ) )
        {
            res1 = "";
            a = '0' + a;
            n++;
            memset( cnt, 0, sizeof( cnt ) );
            for ( int i = 0; i < n - 1; i++ )
                cnt[ b[ i ] - '0' ]++;
            cnt[ 0 ]++;

            findFirst( a, 0, 0 );
        }

        cout << "Case #" << testnum << ": " << res1 << endl;
    }

    return 0;
}
