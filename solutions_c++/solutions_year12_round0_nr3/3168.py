#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstring>
#include <map>
#include <cmath>
#include <set>
using namespace std;

char was[2000001];

int main()
{
    int tests;
    cin >> tests;

    for (int test = 1; test <= tests; test++) {
        int a, b;
        cin >> a >> b;

        int res = 0;
        for (int i = max(10, a), p = 100; i <= b; i++) {
            if (i / p > 0) p *= 10;
            int bs = 10, h = p / 10;
            while (bs < p) {
                int f = (i % bs) * h + i / bs;
                if (f > i && f <= b && !was[f]) {
                    was[f] = 1;
                    res++;
                }
                h /= 10,
                bs *= 10;
            }
            bs = 10, h = p / 10;
            while (bs < p) {
                int f = (i % bs) * h + i / bs;
                if (f > i && f <= b) was[f] = 0;
                h /= 10,
                bs *= 10;
            }
        }

        cout << "Case #" << test << ": " << res << endl;
    }
}
