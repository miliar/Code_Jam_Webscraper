#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int a[1001];
int mat[1001][1001];
long long stack[1<<20];
int top;

int main() {
    int t, n, k, m;
    freopen("/home/isilme/C-large.in", "r", stdin);
    freopen("/home/isilme/C.out", "w", stdout);
    while(cin >> t) {
        long long sum, acc;
        for(int i = 1; i <= t; i++) {
            cin >> n >> k >> m;
            sum = 0;
            for(int i = 0; i < m; i++) {
                cin >> a[i];
                sum += a[i];
            }
            if(sum <= k) {
                printf("Case #%d: %lld\n", i, sum * n);
                continue;
            }
            memset(mat, 0xff, sizeof(mat));
            int last = 0, prev = -1, curr = 0;
            top = 0;
            sum = 0;
            acc = 0;
            int ht, ct;
            long long h, c;
            while(true) {
                sum += a[curr];
                if(sum > k) {
                    if(mat[last][prev] > -1) {
                        ht = mat[last][prev];
                        h = stack[ht];
                        ct = top - mat[last][prev];
                        c = acc - h;
                        break;
                    } else mat[last][prev] = top;
                    sum -= a[curr];
                    stack[top++] = acc;
                    acc += sum;
                    sum = a[curr];
                    last = curr;
                }
                prev = curr;
                curr = (curr + 1) % m;
            }
            //printf("[ht %d] [ct %d] [h %lld] [c %lld]", ht, ct, h, c);
            long long ans = 0;
            if(n <= ht) {
                ans += stack[n];
            } else {
                ans += stack[ht];
                //cout << "ht ans " << ans << endl;
                n -= ht;
                ans += n / ct * c;
                n %= ct;
                ans += stack[ht + n] - stack[ht];
            }
            printf("Case #%d: %lld\n", i, ans);
        }
    }
    return 0;
}
