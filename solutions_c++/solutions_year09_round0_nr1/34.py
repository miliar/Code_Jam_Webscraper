#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int dict[5000][15];
bool valid[5000];

int main() {
    int l, d, n; cin >> l >> d >> n;
    for (int i = 0; i < d; i++) {
        string s; cin >> s;
        for (int j = 0; j < l; j++) dict[i][j] = 1 << (s[j]-'a');
    }

    for (int i = 1; i <= n; i++) {
        string p; cin >> p;
        cout << "Case #" << i << ": ";

        int res = d;
        memset(valid, true, sizeof(valid));

        for (int j = 0, idx = 0; j < l; j++) {
            int m = 0;
            if (p[idx] == '(') {
                idx++;
                while (p[idx] != ')')
                    m |= (1 << p[idx++]-'a');
                idx++;
            } else {
                m = 1 << (p[idx++]-'a');
            }

            for (int k = 0; k < d; k++) if (valid[k]) {
                if (!(dict[k][j] & m)) {
                    valid[k] = false;
                    res--;
                }
            }
        }
        cout << res << endl;
    }
    return 0;
}

