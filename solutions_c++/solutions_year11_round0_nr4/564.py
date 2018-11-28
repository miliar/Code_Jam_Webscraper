#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>

using namespace std;

int n, arr[1005];
double ans;

int main() {
    int t, c, i;
    //freopen("D:\\D-small.in","r",stdin);
    //freopen("D:\\D-small.out","w",stdout);
    scanf("%d", &t);
    for (c = 1; c <= t; c++) {
        scanf("%d", &n);
        for (ans=i = 0; i < n; i++) {
            scanf("%d", arr + i);
            if (arr[i]!=i+1)
                ans++;
        }
        printf("Case #%d: %.6lf\n", c, ans);
    }
    return 0;
}
