#include <iostream>
using namespace std;

int main() {
int total = 0;
cin >> total;
for (int i = 1; i <= total; ++i) {
    int m = 0;
    cin >> m;
    int temp = 0;
    int sum = 0;
    int min = 100000000;
    int xor_sum = 0;
    for (int j = 0; j < m; ++j) {
        cin >> temp;
        xor_sum ^= temp;
        sum += temp;
        if (temp < min) min = temp;
    }
    if (xor_sum == 0) {
        cout << "Case #" << i << ": " << (sum - min) << endl;
    }
    else {
        cout << "Case #" << i << ": " << "NO" << endl;
    }
}

return 0;
}
