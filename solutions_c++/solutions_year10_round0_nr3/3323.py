/* 
 * File:   main.cpp
 * Author: pchambino
 *
 * Created on May 8, 2010, 10:31 PM
 */

#include <iostream>

using namespace std;

/*
 * 
 */
int main() {

    int T, R, k, K, Knext ,N, g, y;

    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> R >> k >> N;

        int G[N];
        for (g = 0; g < N; g++) {
            cin >> G[g];
        }

        g = 0;
        y = 0;
        for (int j = 0; j < R; j++) {
            K = 0;
            for (int l = 0; l < N; l++) { // So it won't repeat groups
                Knext = K + G[g];
                if (Knext < k) {
                    K = Knext;
                    if (++g == N)
                        g = 0;
                } else if (Knext == k) {
                    K = Knext;
                    if (++g == N)
                        g = 0;
                    break;
                } else {
                    break;
                }
            }

            y += K;
        }

        cout << "Case #" << (i+1) << ": " << y << endl;
    }

    return 0;
}

