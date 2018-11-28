#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;

#define LL unsigned long long
LL i,k;
long n;
ifstream fin("in.txt");
ofstream fout("out.txt");
long r;

int main() {
    fin >> r;
    for (int now=1;now<=r;now++) {
    fin >> n >> k;
    bool on = true; int t(0);
    do {
        //cout << (k & (1 << t)) << endl;
        if ( (k & (1 << t)) == 0 ) on = false;
        t++;
    } while (--n && on);

    fout << "Case #" << now << ": " << ( (on) ? "ON" : "OFF") << endl;
    }
}
