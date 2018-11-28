#include<iostream>
using namespace std;

template <typename T> inline bool checkmax(T &a, const T &b) {
    return a < b ? a = b, 1 : 0;
}
typedef long long LL;

const int maxn = 10000 + 10;
LL d[maxn], l[maxn], f[maxn];
LL D;
int T, n;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin>>T;
    for (int t = 1; t <= T; t++) {
        memset(f, 0, sizeof (f));
        cin>>n;
        for(int i = 0; i < n; i++)
            cin>>d[i]>>l[i];
        cin>>D;
        f[0] = d[0];
        for (int i = 0; i < n; ++i) {
            LL range = d[i] + f[i];
            for (int j = i + 1; j < n && range >= d[j]; j++) {
                checkmax(f[j], min(d[j] - d[i], l[j]));
            }
        }
        bool ans = false;
        for (int i = n - 1;i >= 0; --i) {
            if (d[i] + f[i] >= D) {
                ans = true;
                break;
            }
        }
        if (ans) cout<<"Case #"<<t<<": "<<"YES"<<endl;
        else cout<<"Case #"<<t<<": "<<"NO"<<endl;
    }
    return 0;
}