#include <iostream>
#include <cstring>
#include <stack>
#include <queue>
#include <cstdlib>
#include <vector>
using namespace std;

int T;
long long R, k, N;
long long G[1000];

int main (void) {
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> R >> k >> N;
        for (int j = 0; j < N; j++) {
            cin >> G[j];
        }
        int times = 0;
        int euro = 0;
        int tmpk = 0;
        int index = 0;
        int sindex = 0;
        while (times < R) {
            while (tmpk + G[index] <= k) {
                tmpk += G[index];
                index++;
                if (index >= N) { index = 0; }
                if (index == sindex) { break; }
                //cout << "debug:" << tmpk << ' ';
            }
            sindex = index;
            euro += tmpk;
            tmpk = 0;
            times++;
        }
        cout << "Case #" << (i + 1) << ": "<< euro << endl;
    }
    return 0;
}

void dump() {
    cout << R << ' ' << k << ' ' << N << endl;
    for (int j = 0; j < N; j++) {
        cout << G[j] << ' ';
    }
    cout << endl;
}
