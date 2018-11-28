#include <algorithm>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <fstream>
#include <functional>
#include <iostream>
#include <iomanip>
#include <limits>
#include <map>
#include <memory.h>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdio.h>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

const int T = 31;
const int P = 11;


int can[T][P];
bool surp[T][P];

int main() {
        ios_base::sync_with_stdio(0);

        memset(can, 0, sizeof(can));
        memset(surp, 0, sizeof(surp));
        for (int p = 0; p < P; ++p) {
                for (int i1 = p; i1 < P; ++i1) {
                        for (int i2 = max(i1 - 2, 0); i2 <= i1; ++i2) {
                                for (int i3 = max(i1 - 2, 0); i3 <= i2; ++i3) {
                                        int t = i1 + i2 + i3;
                                        if (t >= T) break;
                                        ++can[t][p];
                                        if (i1 - i3 == 2 || i1 - i2 == 2) surp[t][p] = true;
                                }
                        }
                }
        }


        int tt;
        cin >> tt;
        for (int t = 1; t <= tt; ++t) {
                cout << "Case #" << t << ": ";

                int n, s, p;
                cin >> n >> s >> p;

                int ans = 0, ss = s;
                for (int i = 0; i < n; ++i) {
                        int q;
                        cin >> q;
                        if (can[q][p] == 1 && surp[q][p]) --ss;
                        else if (can[q][p]) ++ans;
                }
                if (ss < 0) ans += s;
                else ans += s - ss;
                cout << ans << endl;
        }

        return 0;
}
