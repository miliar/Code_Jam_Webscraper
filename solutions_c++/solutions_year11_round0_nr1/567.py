#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
using namespace std;

struct oper {
    char k[2];
    int pos;
} arr[105];
int n;

int Aat, Bat;

int next(int cur, char chr) {
    int ret = cur;
    while (ret < n && *arr[ret].k != chr)
        ret++;
    return ret;
}

void moveTo(int &p, int q) {
    if (p < q)
        p++;
    else if (p > q)
        p--;
}

int main() {
    int c, t, ans, i, j, ni, nj, nni, nnj;
    scanf("%d", &t);
    for (c = 1; c <= t; c++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
            scanf("%s%d", arr[i].k, &arr[i].pos);
        ans = 0;
        ni = next(0, 'O');
        nj = next(0, 'B');
        Aat = Bat = 1;
        while (ni < n || nj < n) {
            if (ni < nj) {
                if (Aat != arr[ni].pos)
                    moveTo(Aat, arr[ni].pos);
                else
                    ni = next(ni + 1, 'O');
                if (nj < n)
                    moveTo(Bat, arr[nj].pos);
            } else {
                if (Bat != arr[nj].pos)
                    moveTo(Bat, arr[nj].pos);
                else
                    nj = next(nj + 1, 'B');
                if (ni < n)
                    moveTo(Aat, arr[ni].pos);
            }
            //printf("%d, %d\n", Aat, Bat);
            ++ans;
        }
        printf("Case #%d: %d\n", c, ans);
    }
    return 0;
}
