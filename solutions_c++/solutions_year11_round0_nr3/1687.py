#include <iostream>
#include <cstdio>

using namespace std;

int a[1010];

int main()
{
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int tt = 0; tt < t; tt++){
        int n;
        scanf("%d", &n);
        int ans = 0;
        int sum = 0;
        for(int i = 0; i < n; i++){
            scanf("%d", &a[i]);
            ans ^= a[i];
            sum += a[i];
        }
        printf("Case #%d: ", tt + 1);
        if(ans == 0){
            for(int i = 0; i < n; i++){
                ans = max(ans, max(a[i], sum - a[i]));
            }
            printf("%d\n", ans);
        }
        else{
            printf("NO\n");
        }
    }
    return 0;
}
