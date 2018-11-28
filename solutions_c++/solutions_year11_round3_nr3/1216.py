#include <stdio.h>
#include <stdlib.h>
int oth[10001];
int cmp(const void *x, const void *y)
{
    return *(int *)x - *(int *)y;
}
int main()
{
    freopen("in.in","r",stdin);
    freopen("result.out","w",stdout);
    int t;
    int n,lower,upper;
    scanf("%d", &t);
    for(int tcase=1; tcase <=t; tcase++)
    {
        printf("Case #%d: ", tcase);
        scanf("%d%d%d", &n, &lower, &upper);
        for(int i=0; i<n; i++)
            scanf("%d", &oth[i]);
        qsort(oth, n, sizeof(int), cmp);
        int find=0;
        for(int i=lower; i<=upper; i++)
        {
            if(!find)
                for(int j=0; j<n; j++)
                {
                    if(i%oth[j]!=0 && oth[j]%i!=0)
                        break;
                    if(j==n-1)
                    {
                        find = 1;
                        printf("%d\n",i);
                    }
                }
            else
                break;
        }
        if(!find)
            printf("NO\n");
    }
    fclose(stdout);
    return 0;
}
