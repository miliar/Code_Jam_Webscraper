#include<algorithm>
#include<cstdio>
using namespace std;


int a[1111];

int
main()
{
    int t;
    scanf("%d",&t);
    for(int tc = 1; tc <= t; tc ++){
        int n;
        scanf("%d",&n);
        for(int i = 0; i < n; i ++)
            scanf("%d",&a[i]);

        int ans = 0;
        for(int i = 1; i < (1<<n)-1; i ++){
            int sum1 = 0, sum2 = 0;
            int sum3 = 0, sum4 = 0;
            for(int j = 0; j < n; j ++)
                if(i & (1<<j)){
                    sum1 ^= a[j];
                    sum3 += a[j];
                }else{
                    sum2 ^= a[j];
                    sum4 += a[j];
                }
            if(sum1 == sum2)
                ans = max(ans, max(sum3,sum4));
        }
        printf("Case #%d: ",tc);
        if(ans == 0) printf("NO\n");
        else printf("%d\n",ans);
    }
    return 0;
}
