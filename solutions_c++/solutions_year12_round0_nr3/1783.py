#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <sstream>
using namespace std;

int A, B;
int f[10];

int tryout(int num) {
    int ret = 0;
    ostringstream sout;
    sout << num;
    string str = sout.str();
    int n = int(str.size());
    int m = 0;
    for (int st = 1; st < int(str.size()); ++st) {
        if (str[st] == '0') continue;
        int tmp = 0;
        for (int i = 0; i < int(str.size()); ++i) {
            int ind = (st + i) % n;
            tmp *= 10;
            tmp += str[ind] - '0';
        }
        if (tmp > B || tmp < A || tmp <= num) continue;
        bool found = false;
        for (int i = 0; i < m; ++i) {
            if (f[i] == tmp) {
                found = true;
                break;
            }
        }
        if (!found) {
            f[m] = tmp;
            ++m;
            ++ret;
        }
    }
    return ret;
}

void solve(int test) {
    cin >> A >> B;
    int ret = 0;
    for (int num = A; num <= B; ++num) {
        ret += tryout(num);
    }
    printf("Case #%d: %d\n", test, ret);
}

int main() {
    int nTests;
    cin >> nTests;
    for (int test = 1; test <= nTests; ++test) {
        solve(test);
    }
    return 0;
}
