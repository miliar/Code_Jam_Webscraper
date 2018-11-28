#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <iostream>

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define ford(i, n )for(int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for(int i = (int)(a); i <= (int)(b); ++i)

#define pb push_back

using namespace std;

typedef vector<char> vc;

const int n = 4;

string s[n];

int check(const vc& v) {
    int x=0, y=0, t=0;
    forn(i, v.size())
        if(v[i]=='X') ++x;
        else if( v[i]=='O') ++y;
        else if( v[i]=='T') ++t;
    if( x + t == 4) return 1;
    if( y + t == 4) return -1;
    return 0;
}

void win(int x) {
    if( x == 1) 
        puts("X won");
    else
        puts("O won");
}

void solve() {
    int r;
    forn(z, 2) {
        vc v;
        forn(i, n) if( z == 0 ) v.pb(s[i][i]); else v.pb(s[i][n-1-i]);
        r = check(v); if( r ) { win(r); return ; }
    }
    forn(j, n) {
        vc v;
        forn(i, n) v.pb(s[i][j]);
        r = check(v); if( r ) { win(r); return ; }
    }
    forn(i, n) {
        vc v;
        forn(j, n) v.pb(s[i][j]);
        r = check(v); if( r ) { win(r); return ; }
    }
    forn(i, n) forn(j, n) if( s[i][j] == '.' ) { puts("Game has not completed"); return ; }
    puts("Draw");
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    fore(t, 1, T) {
        forn(i, n) cin >> s[i];
        cout << "Case #" << t << ": ";
        solve();
    }
    return 0;
}
