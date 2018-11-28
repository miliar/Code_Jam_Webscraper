#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <set>
#include <algorithm>

using namespace std;

int T ,  A , B;

bool RabinKarp ( string text , string pattern , int q ) {

    int M = pattern.length();
    int N = text.length();

    long long p = 0;
    long long t = 0;
    long long h = 1;

    //h = pow(d,M-1)%q
    for ( int i = 0; i < M-1; ++i ) {
     h = (h*256)%q;
    }

    for ( int i = 0; i < M; ++i ) {
     p = ( 256*p + pattern[i] ) % q;
     t = ( 256*t + text[i] ) % q;
    }

    for ( int i = 0; i <= (N-M); ++i ) {

     if ( p == t ) {
      //check
       int j = 0;
       for ( j = 0; j < M; ++j ) {
        if ( text[i+j] != pattern[j] )
         break;
       }

       //Found!?
       if ( j == M ) {
        return ( true );//printf ( "%d\n" , i );
       }

     }

     //calc next hash starting from i+1
     if ( i < N-M ) {
      t = (256*(t-text[i]*h) + text[i+M])%q;
      if ( t < 0 ) {
       t = ( t + q );
      }
     }

    }

    return ( false );

}

bool recycle ( int n , int m ) {

    string a = "";
    string b = "";

    while ( n > 0 ) {
     a += (n%10);
     n /= 10;
    }

    while ( m > 0 ) {
     b += (m%10);
     m /= 10;
    }

    if ( a.length() != b.length() ) return ( false );

    for ( int j = 0; j < b.length(); ++j ) {

     b.push_back(b[0]);
     b.erase(b.begin());
     if ( RabinKarp ( a , b , 99991 ) ) return ( true );


    }

    return ( false );

}

int how_many ( int A , int B ) {

   int ret = 0;

   //set< pair<int,int> > s;

   for ( int n = A; n <= B; ++n )
    for ( int m = n+1; m <= B; ++m )
     if ( n < m )
      //if ( s.find( make_pair(n,m) ) == s.end() )
       if ( recycle(n,m) )
        ++ret;// , s.insert(make_pair(n,m));

    return ( ret );

}

int main ( ) {

   freopen("in.txt","r",stdin);
   freopen("out.out","w",stdout);

   scanf ( "%d" , &T );

   for ( int i = 1; i <= T; ++i ) {

    scanf ( "%d %d" , &A , &B );

    printf ( "Case #%d: %d\n" , i , how_many(A,B) );

/*
    int ans = 0;

    for ( int j = A; j <= B; ++j )
     for ( int k = j+1; k < B; ++k )
      if ( recycle(i,j) )
       ++Best;
*/

    //for ( int i = 1; i <= 1000; ++i )

   }

   return 0;

}
