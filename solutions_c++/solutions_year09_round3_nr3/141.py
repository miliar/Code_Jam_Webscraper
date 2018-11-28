#include <iostream>
#include <algorithm>

using namespace std;

long long pos[1000];
long long d[105][105];

long long cost(int i, int a, int b) {
    long long cst = pos[b+1] - pos[a-1] - 2;
    return cst;
}

long long func(int a, int b) {
    if ( a > b ) return 0;
    if (d[a][b] != -1)
        return d[a][b];
    long long ret = 99999999999999999LL;
    for (int i = a; i <= b; i++) {
        ret = min(ret, func(a, i-1)+func(i+1, b)+cost(i,a,b));
    }
    d[a][b] = ret;
    return ret;
}

int main() {

    int c, p, q;
    cin >> c;

    for (int i = 1; i <= c; i++) {
        cin >> p >> q;
        pos[0] = 0;
        pos[q+1] = p+1;
        for (int j = 1; j <= q; j++) {
            cin >> pos[j];
        }
        sort(pos, pos+(q+2));
        for (int a = 0; a < q+2; a++)
            for (int b = 0; b < q+2; b++)
                d[a][b] = -1;
        cout << "Case #" << i << ": " << func(1, q) << endl;
    }

    return 0;
}

