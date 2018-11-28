#include <cmath>
#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const double PI = acos(-1.0);

typedef struct pos_t {
    int x, y;
    int r;
    int id;
};

const int DX[] = {0, 1, 1, 1, 0, -1, -1, -1};
const int DY[] = {1, 1, 0, -1, -1, -1, 0, 1};

bool r_cmp(const pos_t &a, const pos_t &b) {
    return a.r > b.r;
}
bool id_cmp(const pos_t &a, const pos_t &b) {
    return a.id < b.id;
}

int N, W, L;
pos_t circle[1111];

bool is_ok(int x, int y, int r, int n) {
    if (x < 0 || y < 0 || x > W || y > L) return false;
    for (int i = 0; i < n; i++) {
        long long dx = circle[i].x - x, dy = circle[i].y - y;
        long long dd = circle[i].r + r;
        if (dx*dx + dy*dy < dd * dd) {
            return false;
        }
    }
    return true;
}

int main() {
    FILE *fin, *fout;    
    fin = fopen("D:\\TopCoder\\gcj2012\\R2\\B-large.in", "r");
    fout = fopen("D:\\TopCoder\\gcj2012\\R2\\B.out", "w");
    int T;
    fscanf(fin, "%d\n", &T);
    for (int ca = 1; ca <= T; ca++) {
        fscanf(fin, "%d %d %d", &N, &W, &L);
        for (int i = 0; i < N; ++i) {
            fscanf(fin, "%d", &circle[i].r);
            circle[i].id = i;
        }
        sort(circle, circle+N, r_cmp);
        for (int i = 0; i < N; ++i) {
            if (i == 0) {
                circle[i].x = 0, circle[i].y = 0;
            } else if (i == 1) {
                circle[i].x = W, circle[i].y = L;
                if (!is_ok(W, L, circle[i].r, 1)) {
                    cout << "Error" << endl;///
                }
            }/* else if (i == 2) {
                circle[i].x = 0, circle[i].y = L;
            } else if (i == 3) {
                circle[i].x = W, circle[i].y = 0;
            }
            */
            if (i < 2) continue;
            bool flag = false;
            for (int j = 0; j < i; ++j) {
                int dd = circle[i].r + circle[j].r;
                for (int ix = 0; ix < 8; ++ix) {
                    int x = circle[j].x + DX[ix]*dd, y = circle[j].y + DY[ix]*dd;
                    if (is_ok(x, y, circle[i].r, i)) {
                        circle[i].x = x, circle[i].y = y;
                        flag = true;
                        goto OK;
                    }
                }
            }
OK:
            if (!flag) cout << "Error" << endl;//
            continue;
        }
        
        
        sort(circle, circle+N, id_cmp);
        fprintf(fout, "Case #%d:", ca);
        for (int i = 0; i < N; ++i) {
            fprintf(fout, " %d %d", circle[i].x, circle[i].y);
        }
        fprintf(fout, "\n");
    }
    
    fclose(fin);
    fclose(fout);
    return 0;
}
