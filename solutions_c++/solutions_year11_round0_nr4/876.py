#include <iostream>
#include <algorithm>

size_t Work() {
    size_t n, res = 0, a;
    std::cin >> n;
    for (size_t i = 1; i <= n; ++i) {
        std::cin >> a;
        if (i != a)
            ++res;
    }
    return res;
}

void Output(size_t k, size_t res) {
    std::cout << "Case #" << k << ": " << res << std::endl;
}

int main() {
    size_t t;
    std::cin >> t;
    for (size_t i = 1; i <= t; ++i) {
        Output(i, Work());
    }
    return 0;
}

