#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

int n;
int caseNumber;

vector < int > x[2];
vector < int > turn;

int pos[2];

void clear() {
        for (int i = 0; i < 2; ++i) {
                x[i].clear();
                pos[i] = 1;
        }
        turn.clear();
}

void read() {
        scanf ( "%d" , &n );

        char tmp[5];
        int a;
        for (int i = 0; i < n; ++i) {
                scanf ( "%s%d" , tmp , &a );

                if ( tmp[0] == 'O' ) {
                        x[0].push_back ( a );
                        turn.push_back ( 0 );
                }

                else {
                        x[1].push_back ( a );
                        turn.push_back ( 1 );
                }
        }
}

inline int get ( int x1 , int x2 ) {
        if ( x1 > x2 )
                return -1;
        if ( x1 == x2 )
                return 0;
        return 1;
}

void solve() {
        int res = 0;
        int p[] = { 0 , 0 };
        int id;

        int i = 0;
        while ( 1 ) {
                id = turn[i];
                if ( i == n )
                        break;

                if ( pos[id] == x[id][ p[id] ] ) {
                        res++;
                        pos[id] = x[id][ p[id] ];
                        p[id]++;

                        if ( pos[id ^ 1] != x[id ^ 1][ p[id ^ 1] ] )
                                pos[id ^ 1] += get ( pos[id ^ 1] , x[id ^ 1][ p[id ^ 1] ] );

                        ++i;
                }
                else {
                        res += abs ( x[id][ p[id] ] - pos[id] );
                        if ( abs ( x[id][ p[id] ] - pos[id] ) >= abs ( x[id ^ 1][ p[id ^ 1] ] - pos[id ^ 1] ) )
                                pos[id ^ 1] = x[id ^ 1][ p[id ^ 1] ];
                        else
                                pos[id ^ 1] += get ( pos[id ^ 1] , x[id ^ 1][ p[id ^ 1] ] ) * abs ( x[id][ p[id] ] - pos[id] );

                        pos[id] = x[id][ p[id] ];
                }
        }

        printf ( "Case #%d: %d\n" , ++caseNumber , res );
}

int main() {
        int t;
        scanf ( "%d" , &t );

        while ( t-- ) {

                clear();
                read();
                solve();
        }

        return 0;
}
