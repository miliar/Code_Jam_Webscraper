#include <iostream>
using namespace std;

int n, d[2000], rec;

void recur(int l, int a, int b, int v, bool ha, bool hb) {
    if (l >= n) {
        if (ha && hb && a == b && v > rec)
            rec = v;
    } else {
        recur(l + 1, a ^ d[l], b, v + d[l], true, hb);
        recur(l + 1, a, b ^ d[l], v, ha, true);
    }
}

int main() {
    int cs;
    cin >> cs;
    for (int cc = 1; cc <= cs; cc++) {
        cin >> n;
        for (int i = 0; i < n; i++)
            cin >> d[i];
        rec = -1;
        recur(0, 0, 0, 0, false, false);
        cout << "Case #" << cc << ": ";
        if (rec < 0)
            cout << "NO";
        else cout << rec;
        cout << "\n";
    }
}
