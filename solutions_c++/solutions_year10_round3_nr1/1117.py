#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

int main() {
    ifstream cin("in.txt");
    ofstream cout("outA.txt");
    int T, N, M, h1, h2;
    double ha[2000], hb[2000];
    cin >> T;
    for (int k = 0; k < T; k++) {
        cout << "Case #" << k+1 << ": ";
        cin >> N;
        for (int i = 0; i < N; i++) {
            cin >> ha[i] >> hb[i];
        }
        long long cnt = 0;
        for (int i = 0; i < N; i++) {
            double D = hb[i] - ha[i];
            for (int j = 0; j < N; j++) {
                if (i == j ) continue;
                double b = hb[j] - ha[i];
                double a = ha[j] - ha[i];
                double div = D - b + a;
                if (div == a) continue;
                double dd = a / div;
                if (dd > 0 && dd < 1) cnt++;
            }
        }
        if (cnt % 2 == 1) {cout << "error!"; return 0;}
        cout << cnt/2 << endl;
    }
}