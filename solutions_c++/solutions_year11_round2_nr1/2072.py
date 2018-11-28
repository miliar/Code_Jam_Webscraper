#include <iostream>

#include <fstream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

typedef vector<int> TIV;
typedef vector<short> TSV;

static const int MAX = 100;

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");

    int numCases = 0;
    in >> numCases;

    for(int c = 0; c < numCases; c++) {

        long double wp[MAX];
        long double owp[MAX];
        TSV oponents[MAX];
        char games[MAX][MAX];
        memset( wp, 0, sizeof(wp) );
        memset( owp, 0, sizeof(owp) );
        memset( games, 0, sizeof(games));

        short n = 0;
        in >> n;
        for(short i = 0; i < n; i++) {
            short won = 0;
            char r = 0;
            for(short j = 0; j < n; j++) {
                in >> r;
                if(r == '1') {
                    won++;
                }

                if( r != '.' ) {
                    oponents[i].push_back(j);
                }
                games[i][j] = r;
            }
            wp[i] = (long double)won / (long double)oponents[i].size();
        }

        for(short i = 0; i < n; i++) {
            TSV::iterator it = oponents[i].begin();
            long double cowp = 0.;
            for(; it!=oponents[i].end(); ++it){
                TSV::iterator oit = oponents[*it].begin();
                short won = 0;
                short played = 0;
                for(;oit != oponents[*it].end(); ++oit){
                    if(*oit != i){
                        if(games[*it][*oit] == '1'){
                            won++;
                        }
                        if(games[*it][*oit] != '.'){
                            played++;
                        }
                    }
                }
                cowp += ((long double)won / (long double)played);
            }
            owp[i] = cowp / (long double)oponents[i].size();
        }

        out << "Case #" << c + 1 << ":" << endl;
        for(short i = 0; i < n; i++) {
            TSV::iterator it = oponents[i].begin();
            long double coowp = 0.;
            for(;it!=oponents[i].end(); ++it){
                coowp += owp[*it];
            }
            long double rpi = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * (coowp / (long double)oponents[i].size());
            out.precision(12);
            out << fixed << rpi << endl;
        }
    }

    in.close();
    out.close();
    return 0;
}
