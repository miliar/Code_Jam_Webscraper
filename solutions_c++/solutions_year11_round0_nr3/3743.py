#include <vector>
#include <cstdio>
#include <iostream>

using namespace std;

int main ()
{
    int T, N, c;
    vector<int> numbers;
    int min_value = 1e9;
    int total_xor = 0, number, total_sum = 0;

    cin >> T;
    for (int t = 0; t < T; ++t) {
        cin >> N;
        total_xor = 0;
        total_sum = 0;
        min_value = 1e9;

        for (int i = 0; i < N; ++i) {
            cin >> number;

            total_xor ^= number;
            total_sum += number;

            if (number < min_value) {
                min_value = number;
            }
        }

        cout << "Case #" << (t + 1) << ": ";

        if (total_xor == 0) {
            cout << (total_sum - min_value) << endl;
        } else {
            cout << "NO" << endl;
        }
    }

    return 0;
}
