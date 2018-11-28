#include <iostream>
#include <fstream>

using namespace std;

int main() {
    fstream fin ("A-large.in", fstream::in);
    int cases; fin >> cases;
    float answers[cases];
    fstream fout ("output.txt", fstream::out);
    for (int t = 0; t < cases; t++) {
        int N;
        fin >> N;
        string grid[N];
        for (int i = 0; i < N; i++)
            fin >> grid[i];
        float WP[N], OWP[N];
        for (int i = 0; i < N; i++) {
            float w, n;
            w = n = 0;
            for (int j = 0; j < N; j++) {
                switch (grid[i][j]) {
                    case '1': w++;
                    case '0': n++;
                    default: break;
                }
            }
            WP[i] = w/n;
        }
        for (int i = 0; i < N; i++) {
            float n, sum;
            n = sum = 0;
            for (int j = 0; j < N; j++) {
                if (grid[i][j] != '.') {
                    float w, nn;
                    w = nn = 0;
                    for (int k = 0; k < N; k++) {
                        if (i == k) continue;
                        switch (grid[j][k]) {
                            case '1': w++;
                            case '0': nn++;
                            default: break;
                        }
                    }
                    sum += w/nn;
                    n++;
                }
            }
            OWP[i] = sum/n;
        }
        fout << "Case #" << t+1 << ":" << endl;
        for (int i = 0; i < N; i++) {
            float n, sum;
            n = sum = 0;
            for (int j = 0; j < N; j++) {
                if (grid[i][j] != '.') {
                    sum += OWP[j]; n++;
                }
            }
            float RPI = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * (sum/n);
            fout << RPI << endl;
        }
    }
    //system("PAUSE");
    return 0;
}
