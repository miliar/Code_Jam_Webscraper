#include <cstdio>
#include <cstring>
#include <iostream>
#include <set>
using namespace std;

const int MAXN = 256;

char combine[MAXN][MAXN];
set < char > inverse[MAXN];

string input;

int nCombine;
int nInverse;
int n;

int caseNumber;

void clear() {
        int i , j;
        for (i = 0; i < MAXN; ++i) {
                for (j = 0; j < MAXN; ++j)
                        combine[i][j] = '.';
                inverse[i].clear();
        }
}

void read() {
        scanf ( "%d" , &nCombine );

        char t[16];
        int i;

        for (i = 0; i < nCombine; ++i) {
                scanf ( "%s" , t );
                combine[ t[0] ][ t[1] ] = t[2];
                combine[ t[1] ][ t[0] ] = t[2];
        }

        scanf ( "%d" , &nInverse );

        for (i = 0; i < nInverse; ++i) {
                scanf ( "%s" , t );
                inverse[ t[0] ].insert ( t[1] );
                inverse[ t[1] ].insert ( t[0] );
        }
        scanf ( "%d" , &n );
        cin >> input;
}

void solve() {
        string s = "";
        string ans = "";

        char tmp;
        int i , j;
        bool ok;

        for (i = 0; i < n; ++i) {
                s.push_back ( input[i] );
                ok = 1;

                if ( (int)s.length() > 1 ) {
                        tmp = combine[ s[ s.length() - 2 ] ][ s[ s.length() - 1 ] ];
                        if ( tmp != '.' ) {
                                s.resize ( s.length() - 2 );
                                s.push_back ( tmp );
                                ok = 0;
                        }
                }
                if ( !ok ) continue;
                for (j = 0; j < (int)s.length(); ++j)
                        if ( inverse[ input[i] ].count ( s[j] ) ) {
                                s.clear();
                                break;
                        }
        }
        ans = "[";
        for (i = 0; i < (int)s.length(); ++i) {
                if ( i )
                        ans += ", ";
                ans += s[i];
        }
        ans += "]";

        printf ( "Case #%d: %s\n" , ++caseNumber , ans.c_str() );
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
