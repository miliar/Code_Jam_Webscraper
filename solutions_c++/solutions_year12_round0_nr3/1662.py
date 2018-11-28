#include <iostream>
#include <cmath>

using namespace std;

int count_recycle_pair(int minimum, int maximum) {
    int figures = (int)log10(minimum);
    int count = 0;
    int mul = 1;
    //cout << minimum << " - " << maximum << " : " << figures << " // " << mul << endl;
    for (int i = 0; i < figures; i++) mul *= 10;
    for (int x = minimum; x <= maximum; x++) {
        int r = x;
        for (int j = 0; j < figures; j++) {
            r = (r / 10) + (r % 10) * mul;
            if (r > x && minimum <= r && r <= maximum) {
                //cout << x << " => " << r << endl;
                count++;
            } else if (r == x) {
                break;
            }
        }
    }
    return count;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int A, B;
        cin >> A >> B;
        cout << "Case #" << (i + 1) << ": " << count_recycle_pair(A, B) << endl;
    }
    return 0;
}
