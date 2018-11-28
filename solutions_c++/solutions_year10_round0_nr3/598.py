#include <iostream>
using namespace std;
const int N = 1000;
int r, k, n; int g[N]; long long s[N];
int d[N]; long long f[N];
long long ans;

long long sum(int l, int r){
    if (l == 0) return s[r];
    if (l <= r) return s[r] - s[l-1];
    return s[n-1] - s[l-1] + s[r];
}

void init(){
    cin >> r >> k >> n;
    for (int i=0;i<n;i++){
        cin >> g[i];
    }
    memset(s, 0, sizeof(0));
}

void solve(){
    int i;

    // Special Case..
    s[0] = g[0];
    for (i=1;i<n;i++)
        s[i] = s[i-1] + g[i];
    if (s[n-1] <= k) {ans = s[n-1] * r; return; }

    f[0] = 0;
    memset(d, 0, sizeof(d));

    ans = 0;
    int p = 0, q;
    for (i=1;i<=r;i++){
        if (d[p]!=0){
            int height = i - d[p] ;
            long long tail = f[(r-(d[p]-1)) % height + (d[p]-1)];
            long long body = (f[d[q]]-f[d[p]-1]) * ((r-(d[p]-1))/height);
            ans = body + tail;
            return;
        }

        q = p;
        while (sum(q, p)<=k){
            p = (p + 1) % n;
        }
        d[q] = i;
        f[i] = f[i-1] + (sum(q, p) - g[p]);
        //cout << i << "  (" << q << "," << p << ") : " << f[i] << endl;
    }
    ans = f[r];
}

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int i, T;
    cin >> T;
    for (i=1;i<=T;i++){
        init(); solve();
        cout << "Case #" << i << ": " << ans << endl;
    }

}
