#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int R = 110, C = 110;

// [Union Set]
// {version}
// 2009-09-02
//{

// Rank is depth. Index begin with 0.
template<int SIZE>
class USet {
    int n, t, p[SIZE], r[SIZE];
    void P(int &x) {
        for(;x != p[t = x]; x = p[x], p[t] = (x != p[x] ? p[x] : x));
    }
public:
    int Roo(int x) {
        P(x); 
        return x; 
    }
    void Clr(int n) {
        this->n = n;
        for(int i = 0; i < n; r[p[i++] = i] = 0);
    }
    void Uni(int x, int y) {
        P(x); P(y);
        if(x != y) {
            if (r[y] < r[x]) swap(x,y);
            else if (r[x] == r[y]) ++r[y];
            p[x] = y;
        }
    }
    bool Sam(int x, int y) {
        P(x); P(y);
        return x == y;
    }
};

//}
// end of [Union Set]

USet<R * C> _ust;
int _off[4][2] = {-1, 0, 0, -1, 0, 1, 1, 0};
char _ans[R][C];
int _g[R][C];
int _r, _c;
int _end;

int Inx(int r, int c) {
    return r * _c + c;
}

void Pos(int inx, int &r, int &c) {
    r = inx / _c;
    c = inx % _c;
}

int To(int r, int c) {
    int i, j = -1;
    int tr, tc;
    for (i = 0; i < 4; ++i) {
        tr = r + _off[i][0];
        tc = c + _off[i][1];
        if (tr < 0 || tr == _r || tc < 0 || tc == _c) continue;
        if (j < 0 || _g[tr][tc] < _g[r + _off[j][0]][c + _off[j][1]]) {
            j = i;
        }
    }
    tr = r + _off[j][0];
    tc = c + _off[j][1];
    if (_g[r][c] <= _g[tr][tc]) {
        return r * _c + c;
    }
    return tr * _c + tc;
}

int main() {
    // freopen("B-large.in", "r", stdin);
    // freopen("out.txt", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for (int tci = 1; tci <= tc; ++tci) {
        scanf("%d%d", &_r, &_c);
        _end = _r * _c;
        _ust.Clr(_end);
        int i, j;
        for (i = 0; i < _r; ++i) {
            for (j = 0; j < _c; ++j) {
                _ans[i][j] = 0;
            }
        }
        for (i = 0; i < _r; ++i) {
            for (j = 0; j < _c; ++j) {
                scanf("%d", _g[i] + j);
            }
        }
        for (i = 0; i < _r; ++i) {
            for (j = 0; j < _c; ++j) {
                _ust.Uni(Inx(i, j), To(i, j));
            }
        }
        char ch = 'a';
        for (i = 0; i < _r; ++i) {
            for (j = 0; j < _c; ++j) {
                if (0 != _ans[i][j]) continue;
                // for (k = i; k < _r; ++k) {
                    // for (l = j; l < _c; ++l) {
                        // if (_ust.Sam(Inx(i, j), Inx(k, l))) {
                            // _ans[k][l] = ch;
                        // }
                    // }
                // }
                int roo = _ust.Roo(Inx(i, j));
                int r, c;
                Pos(roo, r, c);
                if (0 == _ans[r][c]) {
                    _ans[r][c] = ch++;
                }
                _ans[i][j] = _ans[r][c];
            }
        }
        printf("Case #%d:\n", tci);
        for (i = 0; i < _r; ++i) {
            for (j = 0; j < _c; ++j) {
                if (0 != j) putchar(' ');
                putchar(_ans[i][j]);
            }
            putchar('\n');
        }
    }
    return 0;
}
