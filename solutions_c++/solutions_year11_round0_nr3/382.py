#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <queue>
#include <cmath>

using namespace std;

#define MAX 1000

int main() {
    int T, N;
    unsigned long long int sumxor = 0, sum = 0;
    int elem;
    int minelem = 10000000;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> N;
        minelem = 10000000;
        sumxor = 0;
        sum = 0;
        for (int j = 0; j < N; j++) {
            cin >> elem;
            sumxor ^= elem;
            sum += elem;
            if (elem < minelem) minelem = elem;
        }
        if (sumxor != 0) cout << "Case #" << i + 1 << ": NO" << endl;
        else cout << "Case #" << i + 1 << ": " << sum - minelem << endl;
    }
    return 0;
}

