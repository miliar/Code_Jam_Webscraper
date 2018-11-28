/*
ID: dhxav
PROG: 1
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <ctime>
#include <cstdlib>
#include <utility>
#include <queue>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define fornd(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define forabd(i, a, b) for (int i = (int)(b); i >= (int)(a); i--)

int min(int a, int b) {
    return a<b? a:b;
}

int main() {
    ifstream fin ("A-large.in");
    ofstream fout ("A-large.out");

    int T;
    fin >> T;

    forn (i, T) {
        int N;
        fin >> N;

        vector <int> d(N), l(N);
        forn (j, N) fin >> d[j] >> l[j];

        int D;
        fin >> D;

        vector <int> poss(N);
        bool possible = false;

        poss[0] = d[0];

        if (l[0]>=d[0]) forn (j, N) {
            //fout << j << " " << poss[j] << endl;
            if (poss[j]+d[j]>=D) {
                possible = true;
                break;
            }

            int ct = j+1;
            while (ct<N) {
                if (poss[j]<d[ct]-d[j])
                    break;
                //fout << "test" << endl;
                if (poss[ct]<min(d[ct]-d[j], l[ct]))
                    poss[ct] = min(d[ct] - d[j], l[ct]);
                //fout << d[ct] << " " << d[j] << " " << l[ct] << endl;
                ct++;
            }
        }

        fout << "Case #" << i+1 << ": ";
        if (possible) fout << "YES" << endl;
        else fout << "NO" << endl;
    }

    system("PAUSE");
}


