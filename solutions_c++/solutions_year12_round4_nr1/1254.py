#include<fstream>
#include <cstring>
#include <cmath>
#include <iomanip>
using namespace std;

ifstream cin("A-Large.in");
ofstream cout("A-Large.out");

template <typename T> inline bool checkmax(T &a, const T &b) {
    return a < b ? a = b, 1 : 0;
}
typedef long long LL;

const int maxn = 10000 + 10;
LL d[maxn], l[maxn], f[maxn];
LL D;
int T, n;

int main() {
    cin >> T;
    for (int test = 1; test <= T; test++) {
        cout << "Case #" << test << ": ";
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
        if (ans) cout<<"YES"; else cout<<"NO";
        cout << endl;
    }
    return 0;
}
