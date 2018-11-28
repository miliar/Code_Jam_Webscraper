#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

long power(long n) {
    return n < 10 ? 1 : 10 * power(n / 10);
}

int main ()
{
    cout.sync_with_stdio(false);
    long cases, a, b;
    vector<long> repeats;
    cin >> cases;
    for (long i = 1; i <= cases; ++i) {
        cin >> a >> b;
        long total = 0;
        for (long j = a; j <= b; ++j) {
            repeats.clear();
            long p = power(j);
            long rond = p;
            long num = j;
            while (rond > 0) {
                num = 10 * (num % p) + num / p;
                if (num > j && num <= b
                    && find(repeats.begin(), repeats.end(), num) == repeats.end()) {
                    total++;
                    repeats.push_back(num);
                }
                rond /= 10;
            }
        }
        cout << "Case #" << i << ": " << total << "\n";
    }
    return 0;
}