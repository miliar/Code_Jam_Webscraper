#include <iostream>
#include <vector>

using namespace std;

typedef long long int ll;
typedef vector<ll> vi;

struct node {
    ll price;
    int next;
    node(ll p=0, int n=0) : price(p), next(n) {}
};

typedef vector<node> vn;

int main() {
    int T;
    cin >> T;
    for (int c=1; c<=T; ++c) {
        ll R, k, N;
        cin >> R >> k >> N;
        vi g(N);
        ll tot=0;
        for (int i=0; i<N; ++i) {
            cin >> g[i];
            tot += g[i];
        }
        if (tot <= k) {
            cout << "Case #" << c << ": " << R*tot  << "\n";
            continue;
        }

        vn v(N);
        int a=0, b=0;
        ll s=0;
        for (b=0;; ++b %= N) {
            s += g[b];
            while (s > k) {
                v[a].price = (s - g[b]);
                v[a].next = b;
                s -= g[a];
                ++a;
                if (a==N) goto donepre;
            }
        }

      donepre:

        ll sum = 0;
        int ind=0;
        for (int i=0; i<R; ++i) {
            sum += v[ind].price;
            ind = v[ind].next;
        }
        cout << "Case #" << c << ": " << sum << "\n";
    }
}
