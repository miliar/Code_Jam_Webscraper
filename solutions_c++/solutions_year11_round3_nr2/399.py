// 3  5  3  5  3  5  3  5
// 6 16 22 32 38 48 54 64
// 0 0  1   5  3  5  3  5
// 64 - 5 - 5 = 54

#include <iostream>

using namespace std;

inline int min(const int a, const int b) {
    if (a < b) return a;
    else return b;
}

int main() {
    int tcases = 0;
    cin >> tcases;
    
    for (int i = 1; i <= tcases; ++i) {
        unsigned long L, t, N, C;
        cin >> L >> t >> N >> C;
        // start process
        unsigned long total = 0;
        unsigned long dist[1024];
        for (unsigned long  j = 0; j < 1000; ++j) {
            dist[j] = 0;
        }
        unsigned long savetimes[10001] = {0};
        for (unsigned long  j = 0; j < 10001; ++j) {
            savetimes[j] = 0;
        }
        for (unsigned long  j = 0; j < C; ++j) {
            cin >> dist[j];
        }
        //cout << L << "\t" << t << "\t" << N << "\t" << C << endl;
        for (unsigned long  j = 0; j < N; ++j) {
            total += (dist[j % C] * 2);
            //cout << dist[j % C] << "\t" << total << "\t";
            if (total <= t) {
                savetimes[0]++;
                //cout << 0 << "\t";
            }
            else {
                int st = min(dist[j % C], (total - t) / 2);
                savetimes[st]++;
                //cout << st << "\t";
            }
            //cout << endl;
        }
        int leftL = L;
        unsigned long totalsave = 0;
        for (unsigned long  j = 10000; leftL >= 0 && j >= 1; --j) {
            if (savetimes[j] <= leftL) {
                totalsave += (j * savetimes[j]);
            }
            else {
                totalsave += (j * leftL);
            }
            leftL -= savetimes[j];
        }
        cout << "Case #" << i << ": " << (total - totalsave) << endl;
    }
}

