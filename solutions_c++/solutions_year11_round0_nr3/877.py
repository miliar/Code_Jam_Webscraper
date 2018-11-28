#include <iostream>
#include <vector>
#include <algorithm>

int Work() {
    size_t n;
    std::cin >> n;
    std::vector<int> c(n);
    int sum = 0, xum = 0, m = 10000000;
    for (size_t i = 0; i < n; ++i) {
        std::cin >> c[i];
        if (c[i] < m)
            m = c[i];
        sum += c[i];
        xum ^= c[i];
    }
    if (xum != 0)
        return -1;
    else
        return sum - m;
}

void Output(size_t k, int res) {
    std::cout << "Case #" << k << ": ";
    if (res != -1)
        std::cout << res;
    else
        std::cout << "NO";
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

