
#include <iostream>
using namespace std;

int freq[100];

int main(void)
{
    int t;
    cin >> t;
    for (int prob=1; prob<=t; prob++) {
        int n, l, h;

        cout << "Case #" << prob << ": ";
        cin >> n >> l >> h;
        for (int j=0; j<n; j++) {
            cin >> freq[j];
        }
        int ans;
        for (ans = l; ans <= h; ans++) {
            for (int j=0; j<n; j++) {
                if (ans % freq[j] != 0 && freq[j] % ans != 0) {
                    goto next;
                }
            }
            goto ok;
        next:
            ;
        }

        cout << "NO" << endl;
        continue;
    ok:
        cout << ans << endl;
    }
}
