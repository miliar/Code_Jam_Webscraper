#include <iostream>

bool Check(int n, int k) {
    return (k & ((1 << n) - 1)) == ((1 << n) - 1) ? true : false;
    int pn = (1 << n);
    return k % pn >= pn / 2;
}

int main() {
    int t;
    std::cin >> t;
    for (int i = 1; i <= t; ++i) {
        int n, k;
        std::cin >> n >> k;
        std::cout << "Case #" << i << ": " << (Check(n, k) ? "ON" : "OFF") << std::endl;
    }
    return 0;
}

