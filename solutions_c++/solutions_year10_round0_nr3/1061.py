#include <iostream>
#include <queue>
using namespace std;

int main() {
    int T, R, k, N, g[1000], val[1000], skp[1000];
    cin >> T;
    
    for(int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        cin >> R >> k >> N;
        for(int i = 0; i < N; ++i) {
            cin >> g[i];
        }
        for(int i = 0; i < N; ++i) {
            for(skp[i] = val[i] = 0; skp[i] < N; ++skp[i]) {
                if(val[i] + g[(i + skp[i]) % N] > k) {
                    break;
                }
                else {
                    val[i] += g[(i + skp[i]) % N];
                }
            }
        }
        long long ans = 0;
        int pos = 0;
        for(int i = 0; i < R; ++i) {
            ans += val[pos];
            pos = (pos + skp[pos]) % N;
        }
/*
cout << "val[] = ";
for(int i = 0; i < N; ++i) cout << val[i] << ' '; puts("");
cout << "skp[] = ";
for(int i = 0; i < N; ++i) cout << skp[i] << ' '; puts("");
        int seq[1000], vsq[1000], amt[1000], flg[1000], top = 0, pos = 0, ans = 0;
        memset(flg, -1, sizeof(flg));
        seq[top] = pos;
        vsq[top] = ans;
        amt[pos] = ans;
        flg[pos] = top++;
        for(; top <= R; ++top) {
            ans += val[pos];
            pos = (pos + skp[pos]) % N;
            if(flg[pos] != -1) {
                int loop = top - flg[pos];
                int lval = ans - vsq[flg[pos]];
                ans += lval * (N - top);
                break;
            }
            seq[top] = pos;
            vsq[top] = ans;
            amt[pos] = ans;
            flg[pos] = top;
        }
        
cout << "top = " << top << endl;
cout << "seq[] = ";
for(int i = 0; i < top; ++i) cout << seq[i] << ' '; puts("");
cout << "pos = " << pos << endl;
cout << "amt[] = ";
for(int i = 0; i < N; ++i) cout << amt[i] << ' '; puts("");
cout << "flg[] = ";
for(int i = 0; i < N; ++i) cout << flg[i] << ' '; puts("");
cout << "ans = " << ans << endl;
*/
        cout << ans << endl;
    }
}
