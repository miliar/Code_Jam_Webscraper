#include <iostream>
#include <map>


const size_t MAX = 1000;
size_t D[MAX], N, T;

struct TPos {
    size_t T, L, I;
    TPos(size_t t = 0, size_t l = 0, size_t i = 0)
        : T(t)
        , L(l)
        , I(i)
    {}
    bool operator < (const TPos &b) const {
        if (T != b.T)
            return T < b.T;
        if (L != b.L)
            return L < b.L;
        return I < b.I;
    }
};

std::map<TPos, size_t> Hash;

size_t Do(size_t t, size_t l, size_t i) {
    //std::cout << "Do(" << t << ", " << l << ", " << i << ")" << std::endl;
    if (i == N)
        return 0;
    size_t &res = Hash[TPos(t, l, i)];
    if (res == 0) {
        if (t + D[i] < T || l == 0) {           // can not boost
            res = D[i] + Do(t + D[i], l, i + 1);
        } else {
            res = D[i] + Do(t + D[i], l, i + 1);
            size_t wb = T > t ? T - t : 0;
            //std::cout << t << " " << T << " " << wb << " " << wb + (D[i] - wb) / 2 << std::endl;
            size_t r = wb + (D[i] - wb) / 2 + Do(t + wb + (D[i] - wb) / 2, l - 1, i + 1);
            if (res > r)
                res = r;
        }
    }
    return res;
}

size_t Work() {
    Hash.clear();
    size_t L, C, A[MAX];
    std::cin >> L >> T >> N >> C;
    for (size_t i = 0; i < C; ++i)
        std::cin >> A[i];
    for (size_t i = 0; i < N; ++i)
        D[i] = A[i % C] * 2;
    return Do(0, L, 0);
}

void Output(size_t k, size_t res) {
    std::cout << "Case #" << k << ": " << res << std::endl;
}

int main() {
    size_t t;
    std::cin >> t;
    for (size_t i = 1; i <= t; ++i)
        Output(i, Work());
    return 0;
}

