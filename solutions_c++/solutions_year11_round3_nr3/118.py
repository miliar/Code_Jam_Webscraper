#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int tc=1;tc<=t;tc++) {
        int n, l, h;
        cin >> n >> l >> h;

        vector<int> f(n, 0);
        for(int i=0;i<n;i++) {
            cin >> f[i];
        }

        vector<int> v(h+1, 0);

        for(int i=l;i<=h;i++) {
            for(int j=0;j<n;j++) {
                if(f[j]%i == 0 || i%f[j] == 0) {
                    v[i]++;
                }
            }
        }

        int ans = -1;
        for(int i=l;i<=h;i++) {
            if(v[i] == n) {
                ans = i;
                break;
            }
        }

        cout << "Case #" << tc << ": ";
        if(ans == -1) {
            cout << "NO" << endl;
        }
        else {
            cout << ans << endl;
        }
    }

    return 0;
}
