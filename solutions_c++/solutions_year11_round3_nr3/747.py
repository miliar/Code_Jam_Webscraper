#include <iostream>

const size_t MAX = 10000;

int Work() {
    size_t V[MAX];
    size_t N, L, H;
    std::cin >> N >> L >> H;
    for (size_t i = 0; i < N; ++i) {
        std::cin >> V[i];
    }
    for (size_t i = L; i <= H; ++i) {
        bool ok = true;
        for (size_t j = 0; j < N; ++j) {
            if (V[j] % i != 0 && i % V[j] != 0)
                ok = false;
        }
        if (ok)
            return i;
    }
    return -1;
}

void Output(size_t k, int res) {
    std::cout << "Case #" << k << ": ";
    if (res == -1)
        std::cout << "NO";
    else
        std::cout << res;
    std::cout << std::endl;
}

int main() {
    size_t t;
    std::cin >> t;
    for (size_t i = 1; i <= t; ++i) {
        Output(i, Work());
    }
    return 0;
}

