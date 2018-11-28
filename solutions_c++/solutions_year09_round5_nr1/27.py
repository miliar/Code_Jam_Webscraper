#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>
#include <cstring>

using namespace std;

template <typename T> string itosb( T x, int base = 10 ) { string s; if ( x == 0 ) return "0"; int sign = x < 0 ? -1 : 1; while ( x != 0 ) { int digit = sign * ( x % base ); x /= base; if ( digit < 10 ) s.push_back( '0' + digit ); else s.push_back( 'A' + digit - 10 ); } if ( sign == -1 ) s.push_back( '-' ); reverse( s.begin(), s.end() ); return s; }
template<typename Set, typename Element> inline bool inset( const Set &S, const Element &E ) { return S.find(E) != S.end(); }
template <typename T> inline int get_bit ( const T &x, int index ) { return (int)((x >> index) & 1); }

typedef long long packed_state;
typedef vector<pair<int, int> > unpacked_state;

int R, C;
char ploca[15][15];
int nboxes;

unpacked_state unpack_state(packed_state pst) {
    vector<pair<int, int> > ret;
    for ( int i=0; i<nboxes; ++i ) {
        int x = pst & 15; pst >>= 4;
        int y = pst & 15; pst >>= 4;
        ret.push_back(pair<int, int>(x, y));
    }
    return ret;
}

packed_state pack_state(const unpacked_state &ust) {
    packed_state ret = 0;
    for ( int i=nboxes-1; i>=0; --i ) {
        ret <<= 4; ret |= ust[i].second; 
        ret <<= 4; ret |= ust[i].first; 
    }
    return ret;
}

bool is_stable(const unpacked_state &ust) {
    queue<int> q;
    q.push(0);
    int seen = 1;
    while ( !q.empty() ) {
        pair<int, int> pos = ust[q.front()]; q.pop();

        for ( int i=0; i<nboxes; ++i ) {
            if ( get_bit(seen, i) ) continue;
            if ( abs(ust[i].first-pos.first) + abs(ust[i].second-pos.second) == 1 ) {
                q.push(i);
                seen |= 1<<i;
            }
        }
    }
    return seen == (1<<nboxes)-1;
}

bool is_free(const unpacked_state &ust, int r, int c) {
    // fprintf(stderr, "is_free(%d, %d)\n", r, c);
    if ( r < 0 || r >= R ) return 0;
    if ( c < 0 || c >= C ) return 0;
    if ( ploca[r][c] == '#' ) return 0;
    for ( int i=0; i<nboxes; ++i ) {
        if ( make_pair(r, c) == ust[i] )
            return 0;
    }
    return 1;
}

void normalize(unpacked_state &ust) {
    sort(ust.begin(), ust.end());
}

int main(void) { 
    cin.sync_with_stdio(0);

    int CASES; cin >> CASES;
    for ( int tt=1; tt<=CASES; ++tt ) { // caret here
        cin >> R >> C;

        unpacked_state start, end;
        for ( int i=0; i<R; ++i ) {
            cin >> ploca[i];
            for ( int j=0; j<C; ++j ) {
                if ( strchr("ow", ploca[i][j]) != NULL ) start.push_back(make_pair(i, j));
                if ( strchr("xw", ploca[i][j]) != NULL ) end.push_back(make_pair(i, j));
            }
        }
        normalize(start);
        assert(start.size() == end.size());
        nboxes = start.size();
        // cerr << start << endl;
        // cerr << itosb(pack_state(start), 2) << endl;
        // cerr << unpack_state(pack_state(start)) << endl;

        map<packed_state, int> dist;
        queue<packed_state> q;
        q.push(pack_state(start));
        dist[pack_state(start)] = 0;
        while ( !q.empty() ) {
            packed_state pust = q.front(); q.pop();
            unpacked_state ust = unpack_state(pust);
            if ( ust == end ) break;

            // cerr << ust << endl;

            int d = dist[pust];
            bool s = is_stable(ust);

            for ( int i=0; i<nboxes; ++i ) {
                static const int dr[] = { -1, 0, 1, 0 };
                static const int dc[] = { 0, 1, 0, -1 };
                int r = ust[i].first, c = ust[i].second;
                for ( int dir=0; dir<4; ++dir ) {
                    if ( !is_free(ust, r+dr[dir], c+dc[dir]) ||
                         !is_free(ust, r-dr[dir], c-dc[dir]) ) continue;

                    static unpacked_state nust; nust = ust;
                    nust[i].first += dr[dir]; nust[i].second += dc[dir];
                    if ( !s && !is_stable(nust) ) continue;

                    normalize(nust);
                    packed_state pnust = pack_state(nust);
                    if ( inset(dist, pnust) ) continue;

                    q.push(pnust);
                    dist[pnust] = d+1;
                }
            }
        }

        cout << "Case #" << tt << ": " << (inset(dist, pack_state(end)) ? dist[pack_state(end)] : -1) << "\n";
    }

    return 0;
} 
