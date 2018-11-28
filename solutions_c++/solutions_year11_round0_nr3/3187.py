#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>
using namespace std;

int c[1000];

int main()
{
    ifstream fin("in.dat");
    ofstream fout("out.dat");
    int i, j, test, T, N, C, D;
    fin >> T;
    for (test = 1; test <= T; test++) {
        fin >> N;
        for (i = 0; i < N; i++) fin >> c[i];

        int res = 0;
        for (i = 1; i < (1 << N) - 1; i++) {
            int s1 = 0, s2 = 0, xs1 = 0, xs2 = 0;
            for (j = 0; j < N; j++)
                if (i & 1 << j) s1 += c[j], xs1 ^= c[j];
                else s2 += c[j], xs2 ^= c[j];
            if (xs1 == xs2) res = max(res, max(s1, s2));
        }

        fout << "Case #" << test << ": ";
        if (res) fout << res;
        else fout << "NO";
        fout << endl;
    }
    return 0;
}
