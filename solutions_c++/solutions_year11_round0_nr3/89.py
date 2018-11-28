#include <iostream>
using namespace std;

const int INF = 1000000000;

int main() {
    int casos;
    cin >> casos;
    for (int cas = 1; cas <= casos; ++cas) {
        int n, m = INF, sum = 0, sum2 = 0;
        cin >> n;
        for (int i = 0; i < n; ++i) {
            int a;
            cin >> a;
            sum += a;
            sum2 = ((~sum2)&a)|(sum2&(~a));
            m = min(m, a);
        }
        cout << "Case #" << cas << ": ";
        if (sum2 != 0) cout << "NO" << endl;
        else cout << sum - m << endl;
    }
}