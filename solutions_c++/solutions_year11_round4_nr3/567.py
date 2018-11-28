#include <iostream>
#include <string.h>

using namespace std;

int T;
int n;
int c = 0;

long long gcd(long long x, long long y) {
    if (y == 0) return x; 
    return gcd(y, x % y);
}

bool b[1000000];
int q[1000000];

int main() {
    cin >> T;
    while (T--) {
        c = c + 1;
        cin >> n;
        for (int i=2; i <= 1000001; i++) {
        if (!b[i])
        {
            q[++tot]=i;
            for (int j=i+i;j<=1000001;j+=i)
                b[j]=true;
            }
        }
        int ans=0;
        for (int i=1;i<=tot;++i) {
            long long m = (long long) q[i] * (long long) q[i];
            if ( m > n) break;
            else{
                while (m <= n)
                {
                    m *= q[i];
                    ans ++;
                }
            }
        cout << "Case #" << c << ": " << ans << endl;
    }
    return 0;
}