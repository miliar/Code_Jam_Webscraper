// another fine solution by misof
// #includes {{{
#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
using namespace std;
// }}}

/////////////////// PRE-WRITTEN CODE FOLLOWS, LOOK DOWN FOR THE SOLUTION ////////////////////////////////

// pre-written code {{{
#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define SIZE(t) ((int)((t).size()))
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

int R, C, D;
vector< vector<int> > vstup;
vector< vector<int> > klasicke;
vector< vector<int> > rastie_dole;
vector< vector<int> > rastie_hore;
vector< vector<int> > rastie_doprava; 
vector< vector<int> > rastie_dolava;

vector< vector<int> > prefix_sums(const vector< vector<int> > &M) {
    int R=SIZE(M), C=SIZE(M[0]);
    vector< vector<int> > answer( R+1, vector<int>(C+1,0) );
    REP(r,R) REP(c,C) answer[r+1][c+1] = answer[r+1][c] + answer[r][c+1] - answer[r][c] + M[r][c];
    return answer;
}

vector< vector<int> > ovahuj(const vector< vector<int> > &M) {
    int R=SIZE(M), C=SIZE(M[0]);
    vector< vector<int> > answer( R, vector<int>(C,0) );
    REP(r,R) REP(c,C) answer[r][c] = 2 * r * M[r][c];
    return answer;
}

vector< vector<int> > hore_nohami(const vector< vector<int> > &M) {
    vector< vector<int> > answer(M);
    reverse( answer.begin(), answer.end() );
    return answer;
}

vector< vector<int> > transponuj(const vector< vector<int> > &M) {
    int R=SIZE(M), C=SIZE(M[0]);
    vector< vector<int> > answer( C, vector<int>(R,0) );
    REP(r,R) REP(c,C) answer[c][r] = M[r][c];
    return answer;
}

int sucet_obdlznika(const vector<vector<int> > &prefixy, int r0, int c0, int r1, int c1) {
    return prefixy[r1][c1] - prefixy[r1][c0] - prefixy[r0][c1] + prefixy[r0][c0];
}

bool over(int r0, int c0, int K) {
    int x_suma = sucet_obdlznika(rastie_dole,r0,c0,r0+K,c0+K) - (2*r0 + K - 1) * sucet_obdlznika(klasicke,r0,c0,r0+K,c0+K);
    int y_suma = sucet_obdlznika(rastie_doprava,r0,c0,r0+K,c0+K) - (2*c0 + K - 1) * sucet_obdlznika(klasicke,r0,c0,r0+K,c0+K);

    x_suma += (K-1)*vstup[r0][c0] + (K-1)*vstup[r0][c0+K-1] - (K-1)*vstup[r0+K-1][c0] - (K-1)*vstup[r0+K-1][c0+K-1];
    y_suma += (K-1)*vstup[r0][c0] + (K-1)*vstup[r0+K-1][c0] - (K-1)*vstup[r0][c0+K-1] - (K-1)*vstup[r0+K-1][c0+K-1];

    return (x_suma==0) && (y_suma==0);

    /*
    int half = (K+1)/2;
    int prva_x_suma = sucet_obdlznika(rastie_hore,r0,c0,r0+half,c0+K) - (R-1-r0-half)*sucet_obdlznika(klasicke,r0,c0,r0+half,c0+K);
    int druha_x_suma = sucet_obdlznika(rastie_dole,r0+K-half,c0,r0+K,c0+K) - (r0+K-half-1)*sucet_obdlznika(klasicke,r0+K-half,c0,r0+K,c0+K);
    prva_x_suma -= half * vstup[r0][c0] + half * vstup[r0][c0+K-1];
    druha_x_suma -= half * vstup[r0+K-1][c0] + half * vstup[r0+K-1][c0+K-1];
    if (prva_x_suma != druha_x_suma) return false;
    // cout << "x sumy sedia na " << r0 << " " << c0 << " " << K << endl;

    int prva_y_suma = sucet_obdlznika(rastie_dolava,r0,c0,r0+K,c0+half) - (C-1-c0-half)*sucet_obdlznika(klasicke,r0,c0,r0+K,c0+half);
    int druha_y_suma = sucet_obdlznika(rastie_doprava,r0,c0+K-half,r0+K,c0+K) - (c0+K-half-1)*sucet_obdlznika(klasicke,r0,c0+K-half,r0+K,c0+K);
    prva_y_suma -= half * vstup[r0][c0] + half * vstup[r0+K-1][c0];
    druha_y_suma -= half * vstup[r0][c0+K-1] + half * vstup[r0+K-1][c0+K-1];
    if (prva_y_suma != druha_y_suma) return false;
    // cout << "aj y sumy sedia na " << r0 << " " << c0 << " " << K << endl;
    */

    return true;
}

int main() {
    int T;
    cin >> T;
    FOR(t,1,T) {
        cin >> R >> C >> D;
        vstup.clear();
        vstup.resize(R, vector<int>(C));
        REP(r,R) {
            string line;
            cin >> line;
            REP(c,C) vstup[r][c] = line[c]-'0';
        }

        klasicke = prefix_sums(vstup);
        rastie_dole = prefix_sums( ovahuj(vstup) );
        rastie_hore = prefix_sums( hore_nohami(ovahuj(hore_nohami(vstup))) );
        rastie_doprava = prefix_sums( transponuj(ovahuj(transponuj(vstup))) );
        rastie_dolava = prefix_sums( transponuj(hore_nohami(ovahuj(hore_nohami(transponuj(vstup))))) );

        int answer = 0;
        REP(r,R) REP(c,C) {
            for (int k=max(3,answer); r+k<=R && c+k<=C; ++k) {
                if (over(r,c,k)) {
                    answer = max(answer,k);
                }
            }
        }
        if (answer == 0) {
            printf("Case #%d: IMPOSSIBLE\n",t);
        } else {
            printf("Case #%d: %d\n",t,answer);
        }
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
