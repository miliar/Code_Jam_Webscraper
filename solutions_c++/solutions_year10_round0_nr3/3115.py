#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>

using namespace std;


int main() {

    ifstream in;
    ofstream out;
    out.open("C-large.out");
    in.open("C-large.in");

    int t;
    in >> t;

    for(int i=0; i<t; ++i) {
        int r, k, n;
        in >> r >> k >> n;

        //vraca kolika je zarada i na koju poziciju skace sa i-te
        vector <pair<int, int> > sviSkokovi;

        vector <int> grupe;
        for(int j=0; j<n; ++j) {
            int g;
            in >> g;
            grupe.push_back(g);
            //cout << "dodajem u grupu " << g << endl;
        }

        if(n == 1) {
            out << "Case #" << (i+1) << ": " << r*grupe[0] << endl;
            continue;
        }

        //izracunaj sve
        for(int j=0; j<n; ++j) {
            int suma = grupe[j];
            for(int l=(j+1)%n; ; l = (l+1)%n) {
                if(suma + grupe[l] > k || l == j) {
                    sviSkokovi.push_back(make_pair(suma, l));
                    //cout << "Na poziciji " << j << " mogu napraviti skok velicine " << suma << " na poziciju " << l << endl;
                    break;
                }
                else suma += grupe[l];
            }
        }

        int poz = 0;
        long long euros = 0LL;
        while(r--) {
            euros += (long long) sviSkokovi[poz].first;
            poz = sviSkokovi[poz].second;
        }

        out << "Case #" << (i+1) << ": " << euros << endl;
    }
    return 0;
}


