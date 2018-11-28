#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void) {
    int testCount;
    cin >> testCount;
    for (int testNo = 1; testNo <= testCount; ++testNo) {
        int A, B;
        cin >> A >> B;
        int l = 1;
        int r = 10;
        int cd = 1;
        int res = 0;
        for ( ; A <= B; ++A) {
            while (r <= A) {
                l *= 10;
                r *= 10;
                ++cd;
            }
            int cc = A;
            for (int i = 0; i < cd - 1; i++) {
                cc = cc / 10 + (l * (cc%10));
                if (cc <= B && cc > A)
                    ++res;
                if (cc == A)
                    break;
            }
        }
        cout << "Case #" << testNo << ": " << res << endl;
    }
    return 0;
}
