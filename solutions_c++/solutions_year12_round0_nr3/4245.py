#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>
#include <string.h>

using namespace std;

int i, j, k, l, m, n, a, b, ans, t = 1;

bool startswith(string& a, string b) {
    return a.substr(0, b.size()) == b;
}

bool endswith(string& a, string b) {
    return a.substr(a.size() - b.size(), b.size()) == b;
}

int main(void) {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    cin >> n;
    for(i = 0; i < n; i++) {
        cin >> a >> b;
        ans = 0;
        for(j = a; j < b; j++) {
            for(k = j + 1; k <= b; k++) {
                int auxa = j, auxb = k;
                string tma = "", tmb = "";
                while(auxa && auxb) {
                    tma = (char) (auxa % 10 + '0') + tma;
                    tmb = (char) (auxb % 10 + '0') + tmb;
                    auxa /= 10;
                    auxb /= 10;
                }

                if(tma.size() != tmb.size()) continue;

                bool ok = false;

                for(l = 0; l < tmb.size(); l++) {
                    if(startswith(tma, tmb.substr(l, tmb.size() - l)) && endswith(tma, tmb.substr(0, l))) {
                        ok = true;
                        break;
                    }
                }
                if(ok) {
                    ans += 1;
                }
            }
        }
        cout << "Case #" << (t++) << ": " << ans << endl;
    }
    return 0;
}
