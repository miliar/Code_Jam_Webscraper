#include <math.h>
#include <stdint.h>
#include <fstream>
#include <iostream>
#include <set>

using namespace std;


int digit(int n) {
    int c = 0;
    int i = n;
    while (i) {
        ++c;
        i /= 10;
    }
    return c;
}
int shift(int n, int s, int d) {
    int p = pow(10, s);
    return n / p + (n % p) * pow(10, d - s);
}
int check(int s, int e, int n, int d) {
    set<uint32_t> set;
    int first_digit = n / pow(10, d - 1);
    int result = 0;
    for (int i = 1; i < d; ++i) {
        int op_digit = int(n / pow(10, i - 1)) % 10;
        if (op_digit < first_digit || op_digit == 0) {
            continue;
        }
        int shifted = shift(n, i, d);
        if (shifted <= n || shifted > e) {
            continue;
        }
        if (s <= n && n < shifted && shifted <= e) {
            if (set.find(n * 10000 + shifted) == set.end()) {
                result++;
                set.insert(n * 10000 + shifted);
            }
        }
    }
    return result;
}
int main(int argc, char *argv[]) {
    fstream f(argv[1]);
    int count;
    f >> count;
    for (int i = 1; i <= count; ++i) {
        int s, e;
        f >> s >> e;
        int d = digit(s);
        int r = 0;
        for (int j = s; j <= e; ++j) {
            r += check(s, e, j, d);
        }
        cout << "Case #" << i << ": " << r << endl;;
    }
}
