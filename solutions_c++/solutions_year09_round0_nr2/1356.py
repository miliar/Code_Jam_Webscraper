#include <iostream>
#include <stack>

using namespace std;

typedef struct {
    int r;
    int c;
    int v;
    int l;
} NODE;

int main() {
    NODE g[100][100];
    stack< pair<int, int> > s;
    char m[27];
    int case_num;

    cin  >> case_num;
    for (int i = 1; i <= case_num; i++) {

        for (int j = 0; j < 27; j++) m[j] = 0;

        int r, c;
        cin >> r >> c;

        for (int j = 0; j < r; j++)
            for (int k = 0; k < c; k++) {
                cin >> g[j][k].v;
                g[j][k].l = 0;
            }

        int label = 1;
        for (int j = 0; j < r; j++) {
            for (int k = 0; k < c; k++) {
                int least = g[j][k].v;

                if (j != 0)
                    if (g[j-1][k].v < least)
                        least = g[j-1][k].v;
                if (k != 0)
                    if (g[j][k-1].v < least)
                        least = g[j][k-1].v;
                if (k+1 != c)
                    if (g[j][k+1].v < least)
                        least = g[j][k+1].v;
                if (j+1 != r)
                    if (g[j+1][k].v < least)
                        least = g[j+1][k].v;

                if (least != g[j][k].v) {
                    if (j+1 != r) {
                        if (g[j+1][k].v == least) {
                            g[j][k].r = j + 1;
                            g[j][k].c = k;
                        }
                    }
                    if (k+1 != c) {
                        if (g[j][k+1].v == least) {
                            g[j][k].r = j;
                            g[j][k].c = k + 1;
                        }
                    }
                    if (k != 0) {
                        if (g[j][k-1].v == least) {
                            g[j][k].r = j;
                            g[j][k].c = k - 1;
                        }
                    }
                    if (j != 0) {
                        if (g[j-1][k].v == least) {
                            g[j][k].r = j - 1;
                            g[j][k].c = k;
                        }
                    }
                }
                else {
                    g[j][k].l = label++;
                }
            }
        }

        for (int j = 0; j < r; j++) {
            for (int k = 0; k < c; k++) {
                int tmpk = k;
                int tmpj = j;
                int tmptmp;
                while (g[tmpj][tmpk].l == 0) {
                    s.push(make_pair(tmpj, tmpk));
                    tmptmp = tmpj;
                    tmpj = g[tmpj][tmpk].r;
                    tmpk = g[tmptmp][tmpk].c;
                }
                int tmpl = g[tmpj][tmpk].l;
                while (!s.empty()) {
                    g[s.top().first][s.top().second].l = tmpl;
                    s.pop();
                }
            }
        }

        char now_map = 'a';
        for (int j = 0; j < r; j++) {
            for (int k = 0; k < c; k++) {
                if (m[g[j][k].l] == 0) {
                    m[g[j][k].l] = now_map;
                    g[j][k].l = now_map;
                    now_map++;
                }
                else {
                    g[j][k].l = m[g[j][k].l];
                }
            }
        }

        cout << "Case #" << i << ":" << endl;

        for (int j = 0; j < r; j++) {
            for (int k = 0; k < c; k++) {
                cout << (char) g[j][k].l;
                if (k < c - 1) {
                    cout << " ";
                }
            }
            cout << endl;
        }

    }
    return 0;
}
