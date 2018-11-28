#include <iostream>
#include <vector>
#include <algorithm>

void ReadData(std::vector<long long> &t) {
    int n;
    std::cin >> n;
    t.resize(n);
    for (--n; n >= 0; --n) {
        std::cin >> t[n];
    }
}

void Unique(std::vector<long long> &t) {
    size_t i, j, cnt;
    for (i = 0, j = 0, cnt = t.size(); j != cnt; ) {
        size_t k = j;
        for (; k != cnt && t[j] == t[k]; ++k);
        t[i++] = t[j];
        j = k;
    }
    t.resize(i);
}

long long GCD(long long a, long long b) {
    while (b != 0) {
        long long t = a % b;
        a = b;
        b = t;
    }
    return a;
}

long long GCDD(const std::vector<long long> &t) {
    long long res = abs(t[1] - t[0]);
    for (size_t i = 0, cnt = t.size(); i != cnt; ++i)
        for (size_t j = i + 1; j != cnt; ++j) {
            res = GCD(res, abs(t[i] - t[j]));
        }
    return res;
}

bool Check(const std::vector<long long> &t, long long y, long long T) {
    for (std::vector<long long>::const_iterator it = t.begin(), end = t.end(); it != end; ++it)
        if ((*it + y) % T != 0)
            return false;
    return true;
}

long long Work(std::vector<long long> &t) {
    std::sort(t.begin(), t.end());
    Unique(t);
    long long T = GCDD(t);
    if (T == 0)
        return T;
    long long k = ((t.back() - 1) / T + 1) * T;
    while (!Check(t, k - t.back(), T))
        k += T;
    return k - t.back();
}

void Output(int t, long long res) {
    std::cout << "Case #" << t << ": " << res << std::endl;
}

int main() {
    int t;
    std::cin >> t;
    for (int i = 1; i <= t; ++i) {
        std::vector<long long> t;
        ReadData(t);
        Output(i, Work(t));
    }
    return 0;
}

