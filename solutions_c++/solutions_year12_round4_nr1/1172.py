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

int minimum(int a, int b) {
    return a<b? a:b;
}

int main() {
    ifstream fin ("a");
    ofstream fout ("out.txt");

    int T;
    fin >> T;
    forn (i, T) {
        int N;
        fin >> N;
        vector <int> d(N), l(N);
        forn (j, N)
            fin >> d[j] >> l[j];
        int D;
        fin >> D;
        vector <int> position(N);
        bool status = false;
        position[0] = d[0];
        if (l[0]>=d[0]) forn (j, N) {
            if (position[j]+d[j]>=D) {
                status = true;
                break;
            }

            int ct = j+1;
            while (ct<N) {
                if (position[j]<d[ct]-d[j])
                    break;
                if (position[ct]<minimum(d[ct]-d[j], l[ct]))
                    position[ct] = minimum(d[ct] - d[j], l[ct]);
                ct++;
            }
        }
        fout << "Case #" << i+1 << ": ";
        if (status) fout << "YES" << endl;
        else fout << "NO" << endl;
    }
}


