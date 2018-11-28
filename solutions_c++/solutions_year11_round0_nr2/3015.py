#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>
using namespace std;

char res[100];

int main()
{
    ifstream fin("in.dat");
    ofstream fout("out.dat");
    int i, j, test, T, N, C, D;
    fin >> T;
    for (test = 1; test <= T; test++) {
        map < pair < char, char>, char > comb;
        set < pair <char, char> > opp;
        string s;
        int rs = 0;
        fin >> C;
        for (i = 0; i < C; i++) {
            fin >> s;
            comb[make_pair(s[0], s[1])] = comb[make_pair(s[1], s[0])] = s[2];
        }

        fin >> D;
        for (i = 0; i < D; i++) {
            fin >> s;
            opp.insert(make_pair(s[0], s[1])), opp.insert(make_pair(s[1], s[0]));
        }

        fin >> N >> s;

        for (i = 0; i < N; i++) {
            if (rs) {
                pair <char, char> p(res[rs - 1], s[i]);
                if (comb[p]) res[rs - 1] = comb[p];
                else {
                    for (j = 0; j < rs; j++)
                        if (opp.count(make_pair(res[j], s[i]))) break;
                    if (j == rs) res[rs++] = s[i];
                    else rs = 0;
                }
            }
            else res[rs++] = s[i];
        }

        fout << "Case #" << test << ": [";
        if (rs) fout << res[0];
        for (i = 1; i < rs; i++) fout << ", " << res[i];
        fout << "]" << endl;
    }
    return 0;
}
