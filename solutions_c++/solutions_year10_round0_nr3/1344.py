#include <iostream>

using namespace std;

int main() {
    unsigned int t, r, k, n, *g;
    cin >> t;
    for(int num = 1; num != t+1; num++) {
        cin >> r >> k >> n;
        g = new unsigned int[n];
        for(int i = 0; i != n; i++)
            cin >> g[i];
        unsigned int s = 0,
                     i = 0;
        unsigned long x, y = 0;
        while(s != r) {
            x = 0;
            int j = 0;
            while(x+g[i] <= k && j < n) {
                x += g[i];
                i = (i+1)%n;
                j++;
            }
            y += x;
            s++;
        }
        cout << "Case #" << num << ": " << y << endl;
        delete [] g;
    }
    return 0;
}
