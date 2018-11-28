#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int t; // number of tests
    cin >> t;
    for (int i = 0; i < t; i++) {
        int sum = 0, xsum = 0, m = 1000*1000;
        int n, c;
        cin >> n;
        for (int j = 0; j < n; j++) {
            cin >> c;
            sum += c;
            xsum ^= c;
            m = min(m, c);
        }
        cout << "Case #" << (i + 1) << ": ";
        if (xsum == 0)
            cout << (sum - m) << endl;    
        else
            cout << "NO" << endl;
    }
    return 0;
}
