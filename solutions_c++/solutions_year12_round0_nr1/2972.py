#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

char mapping[26] = {
    'y', 'h', 'e', 's', 'o',
    'c', 'v', 'x', 'd', 'u',
    'i', 'g', 'l', 'b', 'k',
    'r', 'z', 't', 'n', 'w',
    'j', 'p', 'f', 'm', 'a', 'q'
};

//#define DEBUG

int main() {

    unsigned T;
    scanf("%u", &T);
#ifdef DEBUG
    cout << " T = " << T << endl;
#endif
    string G;
    getline(cin, G);

    for (unsigned tt=0U; tt<T; ++tt) {
        getline(cin, G);
#ifdef DEBUG
        cerr << " G = " << G << endl;
#endif
        for (unsigned ii=0U; ii<G.size(); ++ii) {
#ifdef DEBUG
            cerr << " int val = " << (int) G[ii] << endl;
#endif
            if (G[ii] != ' ') {
                G[ii] = mapping[(int)G[ii]-97];
            }
        }
        cout << "Case #" << tt+1 << ": " << G << endl;
    }

    return 0;
}
