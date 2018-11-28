#include <iostream>
using namespace std;

int main() {
    int cases;
    cin >> cases;
    for(int c = 1; c <= cases; c++) {
        int min_t = 1000001;
        int xor_t = 0;
        int result = 0;
        int n;
        cin >> n;
        for(int i = 0; i < n; i++) {
            int t;
            cin >> t;
            result += t;
            xor_t ^= t;
            if(t < min_t) min_t = t;
        }
        result -= min_t;

        cout << "Case #" << c << ": ";
        if(xor_t == 0) {
            cout << result << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    return 0;
}
