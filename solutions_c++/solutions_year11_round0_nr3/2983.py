#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int T, tc, N;
int C[20];
bool selected[20];
int maxv;

int myadd(int a, int b) {
    int aa[30];
    int r, t;
    memset(aa, 0, sizeof(aa));
    t = 0;
    while (a > 0) {
        aa[t] += a % 2;
        aa[t] %= 2;
        a /= 2;
        t++;
    }
    t = 0;
    while (b > 0) {
        aa[t] += b % 2;
        aa[t] %= 2;
        b /= 2;
        t++;
    }
    r = 0;
    for (t = 29; t >= 0; t--) {
        r *= 2;
        r += aa[t];
    }
    return r;   
}

void check() {
    int a, b, aa, bb;
    aa = a = bb = b = 0;
    int i;
    int scount = 0;
    for (i = 0; i < N; i++) {
        if (selected[i]){
            a = myadd(a, C[i]);
            aa += C[i];
            scount++;
        } else {
            b = myadd(b, C[i]);
            bb += C[i];
        }
    }
    if (scount == 0 || scount == N) return;
    if (a == b) {
        if (aa > maxv) maxv = aa;
        if (bb > maxv) maxv = aa;
    }
}

void work(int k) {
    if (k >= N) {
        check();
        return;
    }
    selected[k] = false;
    work(k + 1);
    selected[k] = true;
    work(k + 1);
}

int main() {
    freopen("E:\\C-small-attempt0.in", "r", stdin);
    freopen("E:\\C-small.out", "w", stdout);
    cin >> T;
    int i;
    for (tc = 1; tc <= T; tc++) {
        cin >> N;
        for (i = 0; i < N; i++) cin >> C[i];
        maxv = -1;
        work(0);


        cout << "Case #" << tc << ": ";
        if (maxv == -1) cout << "NO";
        else cout << maxv;

        cout << endl;
    }

    return 0;
}
