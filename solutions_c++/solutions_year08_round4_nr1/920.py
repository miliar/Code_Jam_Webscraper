#include <iostream>
#include <fstream>
using namespace std;

const int IMPOSSIBLE = 10001;
const int MAXM = 10001;
bool g[MAXM], c[MAXM], v[MAXM];
int cheat0[MAXM], cheat1[MAXM];
int in_nodes;

int min2(const int& a, const int& b) {
    if (a > b)
        return b;
    else
        return a;
}

int min3(const int& a, const int& b, const int& c) {
    int t = min2(a, b);
    if (c < t)
        return c;
    else
        return t;
}

int main() {
    ifstream fin("A-large.in");
    int n;
    fin >> n;
    for (int x = 1; x <= n; x++) {
        // input
        int m;
        fin >> m;
        bool goal;
        fin >> goal;
        in_nodes = (m - 1) / 2;
        for (int i = 1; i <= in_nodes; i++) {
            fin >> g[i] >> c[i];
        }
        for (int i = 1; i <= (m + 1) / 2; i++)
            fin >> v[i + in_nodes];
        // init
        for (int i = in_nodes; i > 0; i--) {
            if (g[i])
                v[i] = v[i * 2] & v[i * 2 + 1];
            else
                v[i] = v[i * 2] | v[i * 2 + 1];
        }
        for (int i = in_nodes + 1; i <= m; i++) {
            if (v[i]) {
                cheat0[i] = IMPOSSIBLE;
                cheat1[i] = 0;
            } else {
                cheat0[i] = 0;
                cheat1[i] = IMPOSSIBLE;
            }
        }
        // dp
        for (int i = in_nodes; i > 0; i--) {
            int left = i * 2;
            int right = left + 1;
            if (!c[i]) {
                if (g[i]) {
                    cheat1[i] = cheat1[left] + cheat1[right];
                    cheat0[i] = min3(cheat0[left] + cheat0[right],
                                     cheat1[left] + cheat0[right],
                                     cheat0[left] + cheat1[right]);
                } else {
                    cheat0[i] = cheat0[left] + cheat0[right];
                    cheat1[i] = min3(cheat1[left] + cheat1[left],
                                     cheat0[left] + cheat1[right],
                                     cheat1[left] + cheat0[right]);
                }
            } else {
                int and_cheat1 = cheat1[left] + cheat1[right];
                int or_cheat1 = min3(cheat1[left] + cheat1[left],
                                     cheat0[left] + cheat1[right],
                                     cheat1[left] + cheat0[right]);
                int and_cheat0 = min3(cheat0[left] + cheat0[right],
                                      cheat1[left] + cheat0[right],
                                      cheat0[left] + cheat1[right]);
                int or_cheat0 = cheat0[i] = cheat0[left] + cheat0[right];
                if (g[i]) {
                    or_cheat1++;
                    or_cheat0++;
                } else {
                    and_cheat1++;
                    and_cheat0++;
                }
                cheat0[i] = min2(and_cheat0, or_cheat0);
                cheat1[i] = min2(and_cheat1, or_cheat1);
            }
        }
        cout << "Case #" << x << ": ";
        if (goal)
            if (cheat1[1] > m)
                cout << "IMPOSSIBLE";
            else
                cout << cheat1[1];
        else
            if (cheat0[1] > m)
                cout << "IMPOSSIBLE";
            else
                cout << cheat0[1];
        cout << endl;
    }
}
