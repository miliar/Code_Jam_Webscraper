#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstring>

using namespace std;

#define ll long long

ll lcm(ll a, ll b, ll H) {
  if (a/__gcd(a,b) > H/b) {
    return -1;
  }
  return a/__gcd(a,b) * b;
}
ll F[1000];
ll LC[1000];
int main() {
    int T;
    cin>>T;
    for (int t=1;t<=T;t++) {
        ll N,L,H;
        cin>>N>>L>>H;
        ll ans = -1;
        for (int i=0;i<N;i++) {
            cin>>F[i];
        }
        sort(F, F+N);
        memset(LC,-1,sizeof(LC));
        for (int i=L;i<=H;i++) {
            bool good = true;
            for (int j=0;j<N;j++) {
                if (i >= F[j] && i%F[j] == 0 || i < F[j] && F[j]%i == 0) {
                } else {
                    good = false;
                }
            }
            if (good) {
                ans = i;
                break;
            }
        }

        cout << "Case #" << t << ": ";
        if (ans == -1) { 
            cout << "NO" << endl;
        } else {
            cout << ans << endl;
        }

    }
}
