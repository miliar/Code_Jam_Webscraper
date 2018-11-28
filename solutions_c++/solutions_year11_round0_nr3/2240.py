#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int num[10000];

int main() {
    int t, n;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for (int cases = 1; cases <= t; ++cases) {
        int sum = 0;
        scanf("%d",&n);
        for (int i = 0; i < n; ++i) {
            scanf("%d",&num[i]);
            sum = sum ^ num[i];
        }
        if (sum != 0) {
           printf("Case #%d: NO\n",cases);
           continue;
        } else {
           sum = 0;
           int minn = 2000000;
           for (int i = 0; i < n; ++i) {
               minn = min(minn, num[i]);
               sum += num[i];
           }
           printf("Case #%d: %d\n",cases, sum - minn);
        }
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
