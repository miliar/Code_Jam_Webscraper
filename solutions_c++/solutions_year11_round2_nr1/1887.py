#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
#include "iostream"

using namespace std;

char m[100][100];
double wp[100];
double xwp[100][100];
double owp[100];
double oowp[100];
int N;

double compute_wp(int team) {
    int sum = 0;
    int count = 0;
    for (int j = 0; j < N; ++j) {
        if (m[team][j] != -1) {
            sum += m[team][j];
            count++;
        }
    }
    return (double)sum/(double)count;
}

void compute_xwp(int team) {
    for (int i = 0; i < N; ++i) {
        if (i != team) {
            int sum = 0;
            int count = 0;
            for (int j = 0; j < N; ++j ) {
                if (j != team) {
                    if (m[i][j] != -1) {
                        sum += m[i][j];
                        count++;
                    }
                }
            }
            xwp[team][i] = (double)sum/(double)count;
        }
    }
}

double compute_owp(int team)
{
    double sum = 0.0;
    int count = 0;
    for (int i = 0; i < N; ++i)  {
        if (m[team][i] != -1) {
            count++;
            sum += xwp[team][i];
        }
    }
    return sum/count;
}

int main() {
    int T; scanf("%d\n", &T);
    for (int Ti = 1; Ti <= T; ++Ti) {
        fprintf(stderr, "Case #%d of %d...\n", Ti, T);
        scanf("%d\n", &N);
        fprintf(stderr, "%d\n", N);
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                char c; scanf("%c",&c);
                if (c == '.') m[i][j] = -1;
                else if (c == '1') m[i][j] = 1;
                else m[i][j] = 0;
            }
            scanf("\n");
        }

        for (int i = 0; i < N; ++i) {
            wp[i] = compute_wp(i);
        }
        for (int i = 0; i < N; ++i) {
            compute_xwp(i);
        }
        for (int i = 0; i < N; ++i) {
            owp[i] = compute_owp(i);
        }
        for (int i = 0; i < N; ++i) {
            double sum = 0.0;
            int count = 0;
            for (int j = 0; j < N; ++j) {
                if (m[i][j] != -1) {
                    sum += owp[j];
                    count++;
                }
            }
            oowp[i] = sum/count;
        }

        printf("Case #%d:\n", Ti);
        for (int i = 0; i < N; ++i)
            printf("%.12f\n", 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]);
    }
    return 0;
}

