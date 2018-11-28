#include <stdio.h>

int arr[20];
int main () {
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int T,cs,num,i,j,sum,left,right,lsum,ans;
    scanf("%d",&T);
    for (cs = 1; cs <= T; cs++) {
        scanf("%d",&num);
        sum = 0;
        ans = 0;
        for (i = 0; i < num; i++) {
            scanf("%d",&arr[i]);
            sum += arr[i];
        }
        //for (i = 0; i < num; i++) {
        //    printf("%d ",arr[i]);
        //}
        for (i = 1; i < 1<<num - 1; i++) {
            left = right = lsum = 0;
            for (j = 0; j < num; j ++) {
                if (i & (1<<j)) {
                    lsum += arr[j];
                    left ^= arr[j];
                } else {
                    right ^= arr[j];
                }
            }
            if (left == right) {
                /*for (j = 0; j < num; j ++) {
                    if (i & (1<<j)) {
                        printf("%d ",arr[j]);
                    }
                }
                puts("");*/
                if (sum - lsum > lsum) {
                    lsum = sum - lsum;
                }
                if (lsum > ans) {
                    ans = lsum;
                }
            }
        }
        printf("Case #%d: ",cs);
        if (!ans) {
            puts("NO");
        } else {
            printf("%d\n",ans);
        }
    }
    return 0;
}
