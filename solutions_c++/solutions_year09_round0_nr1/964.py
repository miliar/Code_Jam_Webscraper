#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <set>

#define REP(i, n) for ( int i = 0; i < (n); i++ ) 
#define FOR(i, a, b) for ( int i = (a); i < (b); i++ ) 

using namespace std;

int L, D, N;
vector<string> dict;

int main() {
    scanf("%d %d %d", &L, &D, &N);

    REP(i, D) {
        char word[50];
        scanf(" %s", word);
        dict.push_back( string(word) );
    }

    REP(i, N) {
        char pat[1000];
        scanf(" %s", pat);

        vector< set<char> > pos(L);
        int idx = 0;
        REP(j, L) {
            if ( pat[idx] == '(' ) {
                idx++;
                while ( pat[idx] != ')' ) {
                    pos[j].insert(pat[idx]);
                    idx++;
                }
            } else {
                pos[j].insert(pat[idx]);
            }
            idx++;
        }

        int res = 0;

        REP(j, D) {
            int ok = 1;

            REP(k, L) {
                if ( pos[k].find(dict[j][k]) == pos[k].end() ) {
                    ok = 0;
                    break;
                }
            }

            if ( ok ) res++;
        }

        printf("Case #%d: %d\n", i+1, res);
    }

    return 0;
}
