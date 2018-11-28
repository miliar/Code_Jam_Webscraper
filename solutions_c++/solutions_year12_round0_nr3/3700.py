#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<unsigned int> sol;
    unsigned int A, B, T, n, d, sum;
    unsigned int digits[10];
    cin >> T;
    for (unsigned int i = 1; i < T + 1; ++i) {
        cin >> A >> B;
        sum = 0;
        for (unsigned int j = A; j < B + 1; ++j) {
            sol.clear();
            d = 0;
            n = j;
            do {
                digits[d++] = n % 10;
                n /= 10;
            } while (n > 0);
            reverse(digits, digits + d);
            
            for (unsigned int k = 1; k < d; ++k) {
                rotate(digits, digits + 1, digits + d);
                if (digits[0] == 0) {
                    continue;
                }

                n = 0;
                for (unsigned int l = 0; l < d; ++l) {
                    n *= 10;
                    n += digits[l];
                }

                if (n <= B && n > j && find(sol.begin(), sol.end(), n) == sol.end()) {
//                    cout << j << " " << n << endl;
                    sol.push_back(n);
                    ++sum;
                }
            }
        }
        cout << "Case #" << i << ": " << sum << endl;
    }
}
