#include <iostream>
#include <vector>
using namespace std;

bool can(int n, vector<int> d) {
    for (int i = 0; i < d.size(); i++)
        if (n % d[i] != 0 && d[i] % n != 0)
            return false;
    return true;
}

int main() {
    int cs;
    cin >> cs;
    for (int cc = 1; cc <= cs; cc++) {
        int n, l, h;
        cin >> n >> l >> h;
        vector<int> d(n);
        for (int i = 0; i < n; i++)
            cin >> d[i];
        bool yes = false;
        int rec;
        for (int i = l; i <= h; i++)
            if (can(i, d)) {
                yes = true;
                rec = i;
                break;
            }
        cout << "Case #" << cc << ": ";
        if (yes)
            cout << rec << "\n";
        else cout << "NO\n";
    }
}
