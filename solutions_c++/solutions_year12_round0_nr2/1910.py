/*
ID: dhxav
PROG: dancing_with_the_googlers
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
#include <map>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define fornd(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define forabd(i, a, b) for (int i = (int)(b); i >= (int)(a); i--)
#define CONST 10000

int main() {    ifstream fin ("B-large.in");
    ofstream fout ("B-large.out");

    int T;
    fin >> T;

    forn (i,T)
    {
        int N, S, p, ti;
        int ans = 0;
        fin >> N >> S >> p;

        forn (j,N)
        {
            fin >> ti;
            if (ti>=3*p-2) ans++;
            else if (S>0 && ti>=3*p-4 && ti>1)
            {
                ans++;
                S--;
            }
        }

        fout << "Case #" << i+1 << ": " << ans << endl;
    }
}


