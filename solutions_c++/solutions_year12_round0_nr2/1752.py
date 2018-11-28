#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cstdio>
using namespace std;

int main() {
    int nTests;
    cin >> nTests;
    for (int test = 1; test <= nTests; ++test) {
        int n, s, p;
        cin >> n >> s >> p;
        int ret = 0;
        for (int i = 0; i < n; ++i) {
            int num;
            cin >> num;
            int maxx = num / 3;
            int rem = num % 3;
            if (rem > 0) ++maxx;
            if (maxx >= p) {
                ++ret;
                continue;
            }
            if (maxx + 1 >= p) {
                if (rem != 1 && s > 0 && num >= 2) {
                    --s;
                    ++ret;
                }
            }
        }
        printf("Case #%d: %d\n", test, ret);
    }
    return 0;
}
