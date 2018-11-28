#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
string sc[50], sd[50], s;
int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int cas, c, d, n;
    scanf("%d", &cas);
    for (int T = 1; T <= cas; T++) {
        scanf("%d", &c);
        for (int i = 0; i < c; i++) {
            cin >> sc[i];
        }
        scanf("%d", &d);
        for (int i = 0; i < d; i++) {
            cin >> sd[i];
        }
        scanf("%d", &n);
        cin >> s;
        int now = 0;
        string t;
        bool changed = 1;
        while (now < s.size()) {
            t += s[now++];
            bool isc = 1;
            while (isc && t.size() >= 2) {
                int len = t.size();
                isc = 0;
                for (int i = 0; i < c; i++) {
                    if ((t[len - 2] == sc[i][0] && t[len - 1] == sc[i][1]) ||
                        (t[len - 2] == sc[i][1] && t[len - 1] == sc[i][0])) {
                        t.erase(t.size() - 1);
                        t[t.size() - 1] = sc[i][2];
                        isc = 1;
                        break;
                    }
                }
            }
            if (!isc) {
                for (int i = 0; i < d; i++) {
                    if (t.find(sd[i][0]) != string::npos && t.find(sd[i][1]) != string::npos) {
                        t = "";
                        break;
                    }
                }
            }
        }
        printf("Case #%d: [", T);
        for (int i = 0; i < t.size(); i++) {
            putchar(t[i]);
            if (i != t.size() - 1) printf(", ");
        }
        printf("]\n");
    }
}
