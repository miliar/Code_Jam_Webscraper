#include <iostream.h>
#include <math.h>

int main() {
    unsigned int n, t;

    cin >> t;

    for(double qq = 0; qq < t; qq++) {
        int n, c, d, s = 0;
        int C[100][100] = {0,}, D[100][100] = {0,}, Z[111] = {0,};
        char N[111];

        cin >> c;
        for(int i = 0; i < c; i++) {
            char c1,c2,c3;
            cin >> c1 >> c2 >> c3;
            C[c1][c2] = C[c2][c1] = c3;
        }

        cin >> d;
        for(int i = 0; i < d; i++) {
            char d1, d2;
            cin >> d1 >> d2;
            D[d1][d2] = D[d2][d1] = 1;
        }

        cin >> n;
        for(int i = 0; i < n; i++) {
            char z;
            cin >> z;
            if(s > 0 && C[N[s-1]][z]) {
//printf("C[%c][%c]=%c s=%d\n", N[s-1], z, C[N[s-1]][z], s);
                Z[N[s-1]]--;
                N[s-1] = C[N[s-1]][z];
                Z[N[s-1]]++;
                continue;
            }
            for(int j = 0; j < s; j++) {
//printf("D[%c][%c]=%d Z[%c]=%d\n", N[j], z, D[N[j]][z], z, Z[z]);
                if(D[N[j]][z]) {
//printf("D[%c][%c]\n", N[j], z);
                    for(int k = 0; k < 101; k++)
                        Z[k] = 0;
                    s = -1;
                    break;
                }
            }
            if(s == -1) {
                s = 0;
                continue;
            }
            N[s++] = z;
            Z[z]++;
        }

        cout << "Case #" << qq+1 << ": ["; 
        for(int i = 0; i < s; i++) {
            if(i) cout << ", ";
            cout << N[i];
        }
        cout << "]\n";
    }

    return 0;
}
