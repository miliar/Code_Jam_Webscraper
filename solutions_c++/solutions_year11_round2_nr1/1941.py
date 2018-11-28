#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <fstream>

using namespace std;

static int N;

static char WL[100][100];
static double WP[100];
static double OWP[100];
static double OOWP[100];
static double RPI[100];



static void
process(double *wp, bool stop=false)
{
    int total_g[N];
    int g_won[N];
    memset(total_g, 0, N * sizeof(int));
    memset(g_won, 0, N * sizeof(int));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (WL[i][j] == '1') {
                g_won[i]++;
                total_g[i]++;
            } else if (WL[i][j] == '0') {
                total_g[i]++;
            }
        }
    }
    for (int i = 0; i < N; ++i) {
        wp[i] = g_won[i] / ((double)total_g[i]);
    }
    if (stop) {
        return;
    }

    for (int c = 0; c < N; ++c) {
        char prev[N];
        for (int r = 0; r < N; ++r) {
            prev[r] = WL[r][c];
            WL[r][c] = '.';
        }
        double wp2[N];
        process(wp2, true);
        for (int r = 0; r < N; ++r) {
            WL[r][c] = prev[r];
        }
        double totalwp2 = 0.0;
        int wp2count = 0;
        for (int r = 0; r < N; ++r) {
            if (r == c || prev[r] == '.') {
                continue;
            }
            totalwp2 += wp2[r];
            wp2count++;
        }
        OWP[c] = totalwp2 / ((double)wp2count);
    }

    for (int c = 0; c < N; ++c) {
        double totalowp = 0.0;
        int owpcount = 0;
        for (int r = 0; r < N; ++r) {
            if (r == c || WL[r][c] == '.') {
                continue;
            }
            totalowp += OWP[r];
            owpcount++;
        }
        OOWP[c] = totalowp / ((double)owpcount);
    }
    for (int c = 0; c < N; ++c) {
        RPI[c] = 0.25 * wp[c] + 0.50 * OWP[c] + 0.25 * OOWP[c];
    }
}

int
main(int argc, char **argv)
{
    if (argc < 2) {
        printf("%s input.in\n", argv[0]);
        exit(EXIT_FAILURE);
    }
    ifstream f(argv[1]);
    string tmp;
    int T;
    f >> T;
    for (int i = 0; i < T; i++) {
        f >> N;
//        cout << N << endl;
        getline(f, tmp);
        cout << "Case #" << (i + 1) << ":" << endl;
//        cout << N << endl;
        for (int j = 0; j < N; j++) {
            string line;
            getline(f, line);
            memcpy(WL[j], line.c_str(), N);
        }
        process(WP);
        for (int j = 0; j < N; ++j) {
            cout << RPI[j] << endl;
        }
    }
    return 0;
}
