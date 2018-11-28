#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> numbers(100);
    int t;
    scanf("%d", &t);
    for (int ti = 0; ti < t; ti++) {
        int a, b;
        scanf("%d%d", &a, &b);
        
        int result = 0;
        for (int x = a; x <= b; x++) {
            numbers.clear();
            int q = 10;
            for (; q <= x; q *= 10) {
            }
            for (int p = 10; p < x; p *= 10) {
                int y = (x / p) + (x % p) * (q / p);
                if (y > x && y >= a && y <= b && (x % p) >= p / 10 && find(numbers.begin(), numbers.end(), y) == numbers.end()) {
                    numbers.push_back(y);
                    result++;
                }
            }
        }
        printf("Case #%d: %d\n", ti + 1, result);
    }
    return 0;
}
