#include<iostream>

using namespace std;

long long C[44][44];

double P(int c, int n, int i, int j) {
    if(j > n or j < 0) return 0;
    return double(C[i][n-j]) * C[c-i][j] / C[c][n];
}

double E(int c, int n) {
    if(n == c) return 1;
    double dp[44][44];

    for(int i=0; i<=c; i++) {
        for(int j=0; j<=c; j++) dp[i][j] = 0;
    }

    for(int d=1; d<=c-n; d++) {
        for(int i=n; i+d<=c; i++) {
            // compute dp[i][i+d];
            for(int j=1; j<=n and j<=d; j++) {
                double loop = P(c, n, i, 0);
                double go = P(c, n, i, j);
                dp[i][i+d] += go / (1 - loop) * (1 / (1 - loop)  + dp[i+j][i+d]);
            }
        }
    }

    return 1 + dp[n][c];
}

int main() {
    int n, c, T;

    C[0][0] = 1;
    for(int i=1; i<=40; i++) {
        C[i][0] = C[i][i] = 1;
        for(int j=1; j<i; j++) {
            C[i][j] = C[i-1][j-1] + C[i-1][j];
        }
    }

    cin >> T;
    for(int t=1; t<=T; t++) {
        cin >> c >> n;

        printf("Case #%d: %.10f\n", t, E(c, n));
    }
}

