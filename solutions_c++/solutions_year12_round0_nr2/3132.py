#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstring>
#include <map>
#include <cmath>
#include <set>
using namespace std;

int sp[40];
int op[40];

int main()
{
    int tests;

    cin >> tests;

    memset(sp, -1, sizeof(sp));
    memset(op, -1, sizeof(op));

    op[0] = 0, op[1] = 1, op[29] = op[30] = 10;
    for (int i = 2; i < 29; i++) {
        if (i % 3 == 0) {
            op[i] = i / 3;
            sp[i] = i / 3 + 1;
        }
        else if (i % 3 == 1) {
            op[i] = i / 3 + 1;
            sp[i] = (i - 4) / 3 + 2;
        }
        else {
            op[i] = i / 3 + 1;
            sp[i] = i / 3 + 2;
        }
    }

    for (int test = 1; test <= tests; test++) {
        int n, s, p;
        cin >> n >> s >> p;

        int add1 = 0, add0 = 0, min1 = 0, res = 0;
        for (int i = 0; i < n; i++) {
            int d;
            cin >> d;
            bool c1 = false, c2 = false;
            if (sp[d] >= p) c1 = true;
            if (op[d] >= p) c2 = true, res++;

            if (sp[d] > 0) {
                if ((c1 && c2) || (!c1 && !c2)) add0++;
                if (c1 && !c2) add1++;
                if (!c1 && c2) min1++;
            }
        }

        res += min(s, add1);
        s -= min(s, add1);
        s -= min(s, add0);
        res -= min(s, min1);

        cout << "Case #" << test << ": " << res << endl;
    }
}
