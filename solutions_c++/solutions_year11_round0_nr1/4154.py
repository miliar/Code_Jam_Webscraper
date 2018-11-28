#include <iostream>
using namespace std;

int main() {
    int cs;
    cin >> cs;
    for (int cc = 1; cc <= cs; cc++) {
        int n;
        cin >> n;
        char t[n];
        int p[n];
        for (int i = 0; i < n; i++)
            cin >> t[i] >> p[i];
        int dirb[n + 1], diro[n + 1];
        for (int i = n - 1; i >= 0; i--)
            if (t[i] == 'B') {
                dirb[i] = p[i];
                diro[i] = diro[i + 1];
            } else {
                dirb[i] = dirb[i + 1];
                diro[i] = p[i];
            }
        int b = 1, o = 1, r = 0;
        for (int i = 0; i < n; i++) {
            if (t[i] == 'B') {
                int temp = abs(p[i] - b) + 1;
                if (diro[i] > o) {
                    o = min(diro[i], o + temp);
                } else o = max(diro[i], o - temp);
                b = p[i];
                r += temp;
            } else {
                int temp = abs(p[i] - o) + 1;
                //cout << "temp = " << temp << "\n";
                if (dirb[i] > b) {
                    b = min(dirb[i], b + temp);
                } else b = max(dirb[i], b - temp);
                o = p[i];
                r += temp;
            }
            //cout << r << " " << b << " " << o << "\n";
        }
        cout << "Case #" << cc << ": " << r << "\n";
    }
}
