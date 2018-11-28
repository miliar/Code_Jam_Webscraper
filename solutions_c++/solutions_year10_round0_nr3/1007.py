#include <iostream>

using namespace std;

int main() {
    unsigned int T;
    unsigned int R; // run R times a day
    unsigned int k; // hold k people at once
    unsigned int N; // # groups
    unsigned int * g;   // groups
    unsigned int * to;  // index
    unsigned int * sz;  // most # people

    cin >> T;

    for(unsigned int t = 1; t <= T; t++) {
        cin >> R >> k >> N;

        g = new unsigned int [N];
        to = new unsigned int [N];
        sz = new unsigned int [N];

        for(unsigned int i = 0; i < N; i++) {
            cin >> g[i];
        }

        for(unsigned int i = 0; i < N; i++){
            unsigned int x = g[i];
            for(unsigned int j = i+1; ; j++) {
                if (j == N)
                    j = 0;
                if (j == i) {
                    to[i] = i;
                    sz[i] = x;
                    break;
                }
                
                x += g[j];

                if(x > k) {
                    to[i] = j;
                    sz[i] = x-g[j];
                    break;
                }
            }
        }

        /*
        for(unsigned int i = 0; i < N; i++) {
            cout << g[i] << '\t';
        }
        cout << endl; 
        for(unsigned int i = 0; i < N; i++) {
            cout << to[i] << '\t';
        }
        cout << endl; 
        for(unsigned int i = 0; i < N; i++) {
            cout << sz[i] << '\t';
        }
        cout << endl; 
        */

        unsigned int rvn = 0;
        for (unsigned int i = 0, j = 0; i < R; i++) {
            rvn += sz[j];
            j = to[j];
        }

        cout << "Case #" << t << ": " << rvn << endl;

        delete[] g;
        delete[] to;
        delete[] sz;
    }

    return 0;
}
