#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
typedef long long int64;
int t, r, k, n;
int a[1010];
int round[1010];
int follow[1010];
int people[1010];
int main() {
    scanf("%d", &t);
    int Case = 1;
    while(t--) {
        scanf("%d%d%d", &r, &k, &n);
        for(int i = 0; i < n; i++) scanf("%d", &a[i]);
        memset(round, -1, sizeof(round));
        int i;
        int begin = 0;
        int64 res = 0;
        for(i = 0; i < r; i++) {
            if(round[begin] >= 0) break;
            int sum = 0, money = 0;
            int old = begin;
            int np = 0;
            while(np++ < n && sum + a[begin] <= k) {
                sum += a[begin];
                money += a[begin];
                begin = (begin + 1) % n;
            }
            round[old] = i;
            follow[old] = money;
            people[i] = old;
            res += money;
        }
        printf("Case #%d: ", Case++);
        if(i < r) {
            int64 ans = 0;
            int period = i - round[begin];
            int leftround = (r - i) / period;
            for(int j = 0; j < round[begin]; j++) ans += follow[people[j]];
            int64 sum = 0;
            for(int j = round[begin]; j < i; j++) sum += follow[people[j]];
            ans += sum * (leftround + 1);
            for(int j = 0; j < (r - i) % period; j++) ans += follow[people[j + round[begin]]];
            cout << ans << endl;
        } else {
            cout << res << endl;
        }
    }
    return 0;
}


