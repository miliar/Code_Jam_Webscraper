#include <fstream>

using namespace std;

long long min(long long a, long long b) {
    if (a > b) return b;
    else return a;
}

int main()
{
    ifstream fin("B-small-attempt0.in");
    ofstream fout("B-small-attempt0.out");

    int t;
    fin >> t;
    for (int cont = 1; cont <= t; ++cont) {
        int l, n, c;
        long long t;
        fin >> l >> t >> n >> c;
        int a[c];
        for (int i = 0; i != c; ++i) {
            fin >> a[i];
        }
        int dist[n + 1];
        dist[0] = 0;
        for (int i = 1; i <= n; ++i) {
            dist[i] = a[(i - 1) % c];
        }

        long long map[n + 1][l + 1];
        map[0][0] = 0;
        for (int i = 1; i <= n; ++i) {
            map[i][0] = map[i - 1][0] + 2 * dist[i];
        }
        for (int i = 1; i <= l; ++i) {
            map[0][i] = 0;
        }

        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= l; ++j) {
                long long temp = 0;
                if (map[i - 1][j - 1] < t) {
                    if (t - map[i - 1][j - 1] >= 2 * dist[i]) temp = 2 * dist[i];
                    else temp = dist[i] + (t - map[i - 1][j - 1]) / 2;
                }
                else {
                    temp = dist[i];
                }
                map[i][j] = min(map[i - 1][j - 1] + temp, map[i - 1][j] + 2 * dist[i]);
            }
        }

        fout << "Case #" << cont << ": " << map[n][l] << endl;
    }


    fin.close();
    fout.close();
    return 0;
}
