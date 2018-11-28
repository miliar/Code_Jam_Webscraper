#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;
#define REP(i, n) for(int i = 0; i <(n); i++)

#define SORT(x) sort(x.begin(), x.end())

typedef long long LL;

LL a[11111];
int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);

    for(int tcase = 1; tcase <= t; tcase++) {
        int n;
        scanf("%d", &n);

        REP(i, n) {
            cin>>a[i];
        }


        LL ans = 0;

        bool ok = false;
        for(int i = 1; i < ((1<<n)-1); i++) {
            LL sum1, sum2;
            sum1 = sum2 = 0;
            LL orsum1, orsum2;
            orsum1=orsum2=0;
            for(int j = 0; j < n; j++) {
                if(i&(1<<j)) {
                    orsum1 ^= a[j];
                    sum1 += a[j];
                } else {
                    orsum2 ^= a[j];
                    sum2 += a[j];
                }
            }

            if(orsum1==orsum2) {
                ans = max(ans, max(sum1, sum2));
                ok = true;
            }
        }

        cout<<"Case #"<<tcase<<": ";
        if(ok) cout<<ans<<"\n";
        else cout<<"NO\n";
    }
}


