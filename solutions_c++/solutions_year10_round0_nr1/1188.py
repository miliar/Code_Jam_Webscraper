#include <iostream>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int n, k;
        cin >> n >> k;
        bool allon = true;
        for (int i = 0; i < n; i++) {
            if ((k & 1) == 0) allon = false;
            k >>= 1;
        }
        cout << "Case #" << t << ": " << (allon ? "ON" : "OFF") << endl;
    }
    return 0;
}
