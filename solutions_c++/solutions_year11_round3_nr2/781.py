#include <iostream>
#include <fstream>
#include <sstream>
#include <queue>
#include <utility>

using namespace std;

unsigned long long   length[5000] = {0};
bool boost[5000] = {0};
unsigned long long   l, t, n, c;

unsigned long long  bestTime() {
    unsigned long long  time = 0;
    for (unsigned long long   k = 0; k < n; k++) {
        if (!boost[k])
            time += length[k] * 2;
        else {
            if (time >= t) {
                time += length[k];
            } else if (time + length[k] <= t) {
                time += length[k] * 2;
            } else {
                unsigned long long   diff = t - time;
                unsigned long long   dist = length[k] - diff / 2;
                time = t + dist;
            }
        }
    }
    return time;
}

int main() {
    unsigned long long   tests;
    cin >> tests;

    for (unsigned long long   cn = 1; cn <= tests; cn++) {
        cin >> l >> t >> n >> c;
        for (unsigned long long   i = 0; i < c; i++) {
            unsigned long long   temp;
            cin >> temp;
            for (unsigned long long   j = 0; j + i < n; j += c) {
                length[j + i] = temp;
            }
        }
        unsigned long long   minTime = 900000000;
        if (l == 2) {
            for (unsigned long long   i = 0; i < n; i++) {
                for (unsigned long long   j = i + 1; j < n; j++) {
                    boost[i] = boost[j] = true;
                    unsigned long long   time = bestTime();
                    
                    if (minTime > time)
                        minTime = time;
                    boost[i] = boost[j] = false;
                }
            }
        }
        else if (l == 1) {
            for (unsigned long long   i = 0; i < n; i++) {
                boost[i] = true;
                unsigned long long   time = bestTime();
                
                if (minTime > time)
                    minTime = time;
                boost[i] = false;
            }
        } else if (l == 0) {
            minTime = bestTime();
        } else {
            cout <<" WTF";
        }
        
        
        cout << "Case #" << cn << ": " << minTime << endl;
    }
}