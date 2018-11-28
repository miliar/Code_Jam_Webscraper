#include <iostream>

using namespace std;

int N;

void ReadData() {
    cin >> N;
}

int Rank(int mask, int n) {
    int res = 0;
    for (int i = 0; i < n; ++i)
        if (mask & (1 << i))
            ++res;
    return res;
}

bool Check(int mask, int n) {
    if (mask & 1)
        return false;
    if (n == 1)
        return true;
    if ((mask & (1 << (n - 1))) == 0)
        return false;
    int r = Rank(mask, n);
    return Check(mask, r);
}

int Work() {
    int res = 0;
    for (int i = 0; i < (1 << N); ++i)
        if (Check(i, N))
            ++res;
    return res % 100003;
}

void Output(int t, int res) {
    cout << "Case #" << t << ": " << res << endl;
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        ReadData();
        Output(i, Work());
    }
    return 0;
}

