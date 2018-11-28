#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int T,  E,  X,  Y;
vector<pair<int, int> > A,  B;
vector<pair<int, int> >::iterator   iter;

int x,  y,  a,  b;
pair<int, int>  p;
            
int main() {
    
    freopen( "B-large.in", "r", stdin );
    freopen( "small_out.txt", "w", stdout );
    
    cin >> T;
    for( int t = 1; t <= T; ++t ) {

        cin >> E >> X >> Y;
        
        A.clear();
        B.clear();
        
        for( int i = 0; i < X; ++i ) {
            scanf( "%d:%d", &x, &y );
            p.first = 60 * x + y;
            scanf( "%d:%d", &x, &y );
            p.second = 60 * x + y + E;
            A.push_back( p );
        }
        
        for( int i = 0; i < Y; ++i ) {
            scanf( "%d:%d", &x, &y );
            p.first = 60 * x + y;
            scanf( "%d:%d", &x, &y );
            p.second = 60 * x + y + E;
            B.push_back( p );
        }
        
        a = b = 0;
/*
for( int l = 0; l < A.size(); ++l ) {
    p = A[l];
    printf( "A: <%d:%d> - <%d:%d>\n", p.first/60,p.first%60,p.second/60,p.second%60 );
}
for( int l = 0; l < B.size(); ++l ) {
    p = B[l];
    printf( "B: <%d:%d> - <%d:%d>\n", p.first/60,p.first%60,p.second/60,p.second%60 );
}
*/
        while( true ) {
            if( A.empty() && B.empty() )  break;
            if( A.empty() ) { b += B.size(); break; }
            if( B.empty() ) { a += A.size(); break; }
            sort( A.begin(), A.end() );
            sort( B.begin(), B.end() );
            int tm;
            vector<pair<int, int> > *swh,   *tmp;
            if( A[0] <= B[0] ) {
                tm = A[0].first;
                swh = &A;
                tmp = &B;
                ++a;
            }
            else {
                tm = B[0].first;
                swh = &B;
                tmp = &A;
                ++b;
            }
            while( 1 ) {
                iter = lower_bound( swh -> begin(), swh -> end(), make_pair( tm, tm ) );
                if( iter == swh -> end() )  break;
                tm = iter -> second;
                swap( *iter, swh -> back() );
/*
p = swh->back();
printf( "<%d:%d> - <%d:%d>\n", p.first/60,p.first%60,p.second/60,p.second%60 );
*/
                swh -> pop_back();
                sort( swh -> begin(), swh -> end() );
                swap( swh, tmp );
            }
        }
        
//        cout << A.size() << "       "<<B.size()<<endl;
        printf( "Case #%d: ", t );
        
        cout << a << ' ' << b << endl;
        
    }
    
//    system( "pause" );
    
}
