#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <map>
#include <set>
#include <utility>
#include <climits>

using namespace std;


int main() {

    ofstream out;
    out.open ("C-large.out");
    ifstream in;
    in.open("C-large.in");


    int t;
    in >> t;
    for(int i=0; i<t; ++i) {
        int n;
        in >> n;

        int brojac[33] = {0};
        vector<int> brojevi(n);

        for(int j=0; j<n; ++j) {
            int broj;
            in >> broj;
            brojevi[j] = broj;

            for(int k=0; k<32; ++k)
                brojac[k] += (broj >> k) & 1;
        }

        out << "Case #" << (i+1) << ": ";
        bool ispravno = true;
        for(int k=0; k<32; ++k) {
            if(brojac[k] % 2 == 1) {
                out << "NO" << endl;
                ispravno = false;
                break;
            }
        }

        if(ispravno) {
            int suma = 0;
            int min = INT_MAX;
            for(int j=0; j<n; ++j) {
                suma += brojevi[j];
                if(brojevi[j] < min) {
                    min = brojevi[j];
                }
            }
            out << (suma - min) << endl;
        }
    }

    out.close();
    in.close();
    return 0;
}
