#include <iostream>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

int main(void) {
    int t, n, s, p, val, res, cnt = 1;
    vector<int> inp, maxcapa, posib;

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> t;

    while (t--) {
        inp.clear();
        maxcapa.clear();
        posib.clear();
        res = 0;

        cin >> n >> s >> p;
        for (int i = 0; i < n; i++) {
            cin >> val;
            inp.push_back(val);

            if (val == 0) {
                maxcapa.push_back(0);
                posib.push_back(0);
                if (val >= p) res++;
            } else if (val == 1) {
                maxcapa.push_back(1);
                posib.push_back(0);
                if (val >= p) res++;
            } else if (val % 3 == 0) {
                maxcapa.push_back(val / 3);
                if ((val / 3) >= p) {
                    res++;
                    posib.push_back(0);
                } else posib.push_back(1);
            } else {
                maxcapa.push_back((val / 3) + 1);
                if (((val / 3) + 1) >= p) {
                    res++;
                    posib.push_back(0);
                } else if (val % 3 == 1) posib.push_back(0);
                else posib.push_back(1);
            }
        }
        //cout << res << " " << s << "\n";
        for (int i = 0; i < inp.size(); i++) {
            //cout << "1. " << inp[i] << " " << maxcapa[i] << " " << posib[i] << "\n";
            if (posib[i] == 1 && s && (maxcapa[i] + 1) >= p) {
                res++;
                s--;
                //cout << s << "\n";
            }
        }
        cout << "Case #" << cnt << ": ";
        cout << res << "\n";
        cnt++;
    }

    return 0;
}

