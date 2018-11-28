#include <iostream>
#include <cstdlib>
#include <climits>

using namespace std;

int main() {
    int N, T, c;
    long sum, min, XOR;
    cin >> T;
    for(int t=1; t<=T; ++t) {
        sum = XOR = 0;
        min = LONG_MAX;
        cin >> N;
        for(int n=1; n <= N; ++n) {
            cin >> c;
            if(c < min)
                min = c;
            XOR ^= c;
            sum += c;
        }
        cout << "Case #"<< t << ": ";
        if(XOR != 0)
            cout << "NO";
        else
            cout << sum - min;
        cout  << endl;
    }
    return 0;
}
