#include<cstdio>
#include<climits>
#include<algorithm>

using namespace std;

int main() {
    int zw;
    scanf("%d", &zw);
    for(int tc=1; tc<=zw; tc++) {
        int n;
        scanf("%d", &n);
        long long int x = 0;
        long long int sum = 0;
        long long int minn = LONG_MAX;
        for(int i=0; i<n; i++) {
            long long int a;
            scanf("%lld", &a);
            x^=a;
            sum += a;
            minn = min(minn, a);
        }
        printf("Case #%d: ", tc);
        if(x != 0)
            printf("NO\n");
        else
            printf("%lld\n", sum-minn);
    }
    return 0;
}
