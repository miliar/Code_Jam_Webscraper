#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

struct State {
    int r, c1, c2, p;

    friend bool operator<(const State &s1, const State &s2) {
        if ( s1.r != s2.r ) return s1.r < s2.r;
        if ( s1.c1 != s2.c1 ) return s1.c1 < s2.c1;
        if ( s1.c2 != s2.c2 ) return s1.c2 < s2.c2;
        return s1.p < s2.p;
    }
};

map<State, int> dist, boja;
struct pqcmp {
    bool operator()(const State &s1, const State &s2) const {
        if ( dist[s1] != dist[s2] ) return dist[s1] < dist[s2];
        return s1 < s2;
    }
};

int R, C, F;
char cave[51][51];
void expand(State &S) {
    while ( S.c1 > 0   && cave[S.r][S.c1-1] == '.' && cave[S.r+1][S.c1-1] == '#' ) --S.c1;
    while ( S.c2 < C-1 && cave[S.r][S.c2+1] == '.' && cave[S.r+1][S.c2+1] == '#' ) ++S.c2;
}

void putq(set<State, pqcmp> &pq, State S, int nd, int F) {
    // fall
    int cnt = F;
    while ( S.r < R-1 && cave[S.r+1][S.p] == '.' ) {
        if ( cnt-- == 0 ) return;
        ++S.r; S.c1 = S.c2 = S.p;
    }
    expand(S);

    int &b = boja[S], &d = dist[S];
    if ( b == 2 ) return;
    if ( b == 1 && nd >= d ) return;

    if ( b == 1 ) pq.erase(S);
    d = nd;
    b = 1;
    pq.insert(S);
    // fprintf(stderr, "  sirim se u (r=%d, c1=%d, c2=%d, p=%d, nd=%d)\n", S.r, S.c1, S.c2, S.p, nd);
}

int main(void) { 
    cin.sync_with_stdio(0);

    int CASES; cin >> CASES;
    for ( int tt=1; tt<=CASES; ++tt ) { // caret here
        cin >> R >> C >> F;
        for ( int i=0; i<R; ++i ) cin >> cave[i];

        dist.clear(); boja.clear();
        State start = {0, 0, 0, 0};
        expand(start);
        set<State, pqcmp> pq;
        dist[start] = 0;
        boja[start] = 1;
        pq.insert(start);

        int ans = -1;
        while ( !pq.empty() ) {
            State S = *pq.begin(); pq.erase(pq.begin());
            boja[S] = 2;

            const int r = S.r, c1 = S.c1, c2 = S.c2, p = S.p, d = dist[S];
            // fprintf(stderr, "r=%d, c1=%d, c2=%d, p=%d, d=%d\n", r, c1, c2, p, d);

            if ( r == R-1 ) { ans = dist[S]; break; }

            if ( p > 0   && (cave[r][p-1] == '.' || p > c1)) putq(pq, (State){r, c1, c2, p-1}, d, F);
            if ( p < C-1 && (cave[r][p+1] == '.' || p < c2)) putq(pq, (State){r, c1, c2, p+1}, d, F);

            int left = p, right = p;
            while ( left  > 0   && (cave[S.r][left-1]  == '.' || left > c1)  && cave[S.r+1][left-1] == '#' ) --left;
            while ( right < C-1 && (cave[S.r][right+1] == '.' || right < c2) && cave[S.r+1][right+1] == '#' ) ++right;
            
            if ( right-left > 0 ) {
                for ( int a=left; a<=right; ++a ) {
                    for ( int b=a; b<=right; ++b ) {
                        if ( a == left && b == right ) continue;
                        // for ( int m=a; m<=b; ++m )
                        if ( a != left )  putq(pq, (State){r+1, a, b, a}, d+(b-a+1), F-1);
                        if ( b != right ) putq(pq, (State){r+1, a, b, b}, d+(b-a+1), F-1);
                    }
                }
            }
        }

        cout << "Case #" << tt << ": ";
        if ( ans == -1 ) cout << "No";
        else cout << "Yes " << ans;
        cout << "\n";
    }

    return 0;
} 
