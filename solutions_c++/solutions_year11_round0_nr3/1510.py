#include <iostream>
#include <numeric>
#include <algorithm> 
#include <limits>


int main() {
    int testCount;
    std::cin >> testCount;
    for (int t = 1; t <= testCount; ++t) {
        int pieceCount;
        std::cin >> pieceCount;
        int min = std::numeric_limits<int>::max();
        int x = 0;
        int sum = 0;
        for (int i = 0; i < pieceCount; ++i) {
            int c;
            std::cin >> c;
            x ^= c;
            sum += c;
            min = std::min(min, c);
        }
        sum -= min;
        std::cout << "Case #" << t << ": ";
        if (x) {
            std::cout << "NO";
        } else {
            std::cout << sum;
        }
        std::cout << std::endl;
    }
    return 0;
}
