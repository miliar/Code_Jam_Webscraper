#include <cctype>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int L = 20, D = 5010, N = 510, M = 30;

char _dic[D][L];
bool _flg[L]['z' + 1];
int _end, _len;

int Find(char s[]) {
    int i, j;
    for (i = 0, j = 0; i < _len; ++i, ++j) {
        fill_n(_flg[i], 'z' + 1, false);
        if (islower(s[j])) {
            _flg[i][s[j]] = true;
        }
        else {
            for (++j; ')' != s[j]; ++j) {
                _flg[i][s[j]] = true;
            }
        }
    }
    int cnt = 0;
    for (i = 0; i < _end; ++i) {
        for (j = 0; j < _len; ++j) {
            if (!_flg[j][_dic[i][j]]) break;
        }
        if (j == _len) {
            ++cnt;
        }
    }
    return cnt;
}

int main() {
    // freopen("A-large.in", "r", stdin);
    // freopen("out.txt", "w", stdout);
    int n;
    scanf("%d%d%d\n", &_len, &_end, &n);
    int i;
    for (i = 0; i < _end; ++i) {
        gets(_dic[i]);
    }
    char s[M * L];
    for (i = 0; i < n; ++i) {
        gets(s);
        printf("Case #%d: %d\n", i + 1, Find(s));
    }
    return 0;
}
