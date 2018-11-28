/*
Uses GMP library for handling large integers.
*/

#include <iostream>
#include <fstream>
#include <gmp.h>
#include <gmpxx.h>
#define fori(n) for(int i = 0; i < n; i++)

using namespace std;
typedef mpz_class BigInt;

int ddd[101];

int denom(int n) {
    if (n == 0) return 0;
    if (ddd[n] != 0) return ddd[n];
    else {
        int nn = n;
        ddd[n] = 100;
        if(nn%5 == 0) {
            ddd[n] /= 5;
            nn /= 5;
            if (nn %5 == 0) {
                ddd[n] /= 5;
                nn /= 5;
            }
        }
        if (nn%2 == 0) {
            ddd[n] /= 2;
            nn /= 2;
            if (nn%2 == 0) {
                ddd[n] /= 2;
                nn /= 2;
            }
        }
        return ddd[n];
    }
}

int main() {
    ifstream in("A-large.in");
    ofstream out("a.out");
    fori(101) ddd[i] = 0;
    int Z, p1, p2;
    in >> Z;
    char NN[16];
    BigInt N;
    for(int z = 0; z < Z; z++) {
        out << "Case #" << z+1 << ": ";
        in >> N >> p1 >> p2;

        //cout << NN << " " << p1 << " " << p2 << endl;
		//N = BigInt(NN);
        if (p1 == 0) {
            if (p2 == 100) {
                out << "Broken" << endl;
            }
            else {
                out << "Possible" << endl;
            }
            continue;
        }

        int d1 = denom(p1);

        if (d1 > N) {
            out << "Broken" << endl;
            continue;
        }

        BigInt won = p1*((N/d1) * d1)/100;
        BigInt lost = (100-p1)*((N/d1) * d1)/100;
        //cout << won << ":" << lost << endl;
        if (p2 == 100) {
            if (won == 0 || lost != 0)  out << "Broken" << endl;
            else out << "Possible" << endl;
        }
        else if(p2 == 0) {
            if (won > 0 || lost == 0)  out << "Broken" << endl;
            else out << "Possible" << endl;
        }
        else {
            out << "Possible" << endl;
        }
    }
    //cin.get();

    return 0;
}
