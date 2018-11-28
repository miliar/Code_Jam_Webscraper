#include <cstring>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;

int n, numo[100];
char map[100][101];
double w[100], ow[100], oow[100];

int main() {
    FILE *fin = fopen("A-small-attempt0.in", "r");
    FILE *fout = fopen("out.txt", "w");
    int test;
    fscanf(fin, "%d", &test);
    for (int i = 1; i <= test; ++i) {
        fprintf(fout, "Case #%d:\n", i);
        fscanf(fin, "%d", &n);
        for (int j = 0; j < n; ++j)
            fscanf(fin, "%s", map[j]);
        for (int j = 0; j < n; ++j) {
            int win = 0;
            numo[j] = 0;
            for (int k = 0; k < n; ++k) {
                if (map[j][k] == '.') continue;
                if (map[j][k] == '1') ++win;
                ++numo[j];
            }
            w[j] = (double) win / (double) numo[j];
        }
        for (int j = 0; j < n; ++j) {
            double sum = 0;
            for (int k = 0; k < n; ++k) {
                if (map[k][j] == '.') continue;
                else if (map[k][j] == '0') sum += w[k] * numo[k] / (numo[k] - 1);
                else sum += (w[k] * numo[k] - 1) / (numo[k] - 1);
            }
            ow[j] = sum / numo[j];
        }
        for (int j = 0; j < n; ++j) {
            double sum = 0;
            for (int k = 0; k < n; ++k)
                if (map[j][k] != '.') sum += ow[k];
            oow[j] = sum / numo[j];
        }
        for (int j = 0; j < n; ++j)
            fprintf(fout, "%lf\n", 0.25 * w[j] + 0.50 * ow[j] + 0.25 * oow[j]);
    }
    fclose(fout);
    fclose(fin);
    return 0;
}
