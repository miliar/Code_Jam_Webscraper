#include <iostream>
#include <math.h>

using namespace std;

double calc(char *g, int z, int n) {
    double t = 0, w = 0;
    for(int i = 0; i < n; i++) {
        if(i == z) continue;
        if(g[i] == '1') {
            t++; w++;
        } else if(g[i] == '0') t++;
    }
    return w/t;
}

int main() {
    unsigned int t;

    cin >> t;

    for(double tt = 0; tt < t; tt++) {
        int n;
        cin >> n;

        char games[101][101];
        double wp[101];
        double owp[101];
        double oowp[101];
        for(int i = 0; i < n; i++) {
            cin >> games[i];
            double t = 0, w = 0;
            for(int j = 0; j < n; j++) {
                if(games[i][j] == '1') {
                    t++; w++;
                } else if(games[i][j] == '0') t++;
            }
            wp[i] = w/t;
        }

        for(int i = 0; i < n; i++) {
            double t = 0, avg = 0;
            for(int j = 0; j < n; j++) {
                if(games[i][j] != '.') {
                    avg += calc(games[j], i, n);
                    t++;
                }
            }
            owp[i] = avg / t;
        }

        for(int i = 0; i < n; i++) {
            double t = 0, avg = 0;
            for(int j = 0; j < n; j++) {
                if(games[i][j] != '.') {
                    avg += owp[j];
                    t++;
                }
            }
            oowp[i] = avg / t;
        }

        cout << "Case #" << tt+1 << ":" << "\n";
        
        for(int i = 0; i < n; i++) {
            double rpi = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
            cout << rpi << '\n';
        }

    }

    return 0;
}
