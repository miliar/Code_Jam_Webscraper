#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>

using namespace std;

int data[1001];
long long sum[2000];
int step[1001];
long long cyclc;
long long ss;
int num;
int top;
int pp;
bool halt;
int main()
{
    //freopen("C-large.in", "r", stdin);
    //freopen("C-large.out", "w", stdout);
    int T, r, k, n;
    scanf("%d", &T);
    for (int tt = 1; tt <= T; ++tt) {
        scanf("%d%d%d", &r, &k, &n);
        ss = 0;
        for (int i = 0; i < n; ++i) {
            scanf("%d", &data[i]);
            ss += data[i];
        }
        memset(step, -1, sizeof(step));
        memset(sum, 0, sizeof(sum));
        top = 0;
        halt = false;
        cyclc = 0;
        num = 0;
        int pos = 0;
        for (int i = 1; ; ++i) {
            if (step[pos] >= 0) {
                cyclc = sum[i - 1] - sum[step[pos] - 1];
                num = i - step[pos];
                pp = step[pos];
                break;
            }
            long long s = 0;
            int next = pos;
            while (s + data[next] <= k && s + data[next] <= ss) {
                s += data[next];
                next = (next + 1) % n;
            }
            if (s == 0) {
                halt = true;
                break;
            }
            sum[i] = sum[i - 1] + s;
            step[pos] = i;
            pos = next;
            top++;
        }
        long long ans = 0;
        if (halt) {
            ans = sum[top];
        } else if (r <= top) {
            ans = sum[r];
        } else {
            ans = sum[top];
            ans += ((r - top) / num) * cyclc;
            if ((r - top) % num) ans += sum[pp + (r - top) % num - 1] - sum[pp - 1];
        }
        printf("Case #%d: %I64d\n", tt, ans);
    }
    return 0;
}
