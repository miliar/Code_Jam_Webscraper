#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

int main() {
    ifstream fin;
    ofstream fout;
    fin.open("B2.in");
    fout.open("B2.out");
    int t;
    fin >> t;
    for (int cas = 1; cas <= t; ++cas) {
        fout << "Case #" << cas << ": ";
        int n, s, p, res = 0;
        fin >> n >> s >> p;
        for (int i = 0; i < n; ++i) {
            int k;
            fin >> k;
            if (k >= 3*p-2) {
                res++;
                continue;
            }
            if (k >= 3*p-4 and s > 0 and p > 1) {
                res++;
                s--;
                continue;
            }
        }
        fout << res << endl;
    }
    system ("pause");
}
