#include <iostream>

using namespace std;

int main() {
    int t; cin >> t;
    for (int i = 1; i <= t; i++) {
        int n, s, p;
        cin >> n >> s >> p;
        int risp = 0;
        while (n--) {
            int tot; cin >> tot;
            if (tot == 0) {
                if (p == 0) risp++;
            } else if (tot % 3 == 0) {
                if (tot / 3 >= p) risp++;
                else if (s && tot / 3 + 1 >= p) {
                    risp++;
                    s--;
                }
            } else if (tot % 3 == 1) {
                if (tot / 3 + 1 >= p)
                    risp++;
            } else if (tot % 3 == 2) {
                if (tot / 3 + 1 >= p)
                    risp++;
                else if (s && tot / 3 +2 >= p) {
                    risp++;
                    s--;
                }
            }
        }
        cout << "Case #" << i << ": " << risp << "\n";
    }


}
