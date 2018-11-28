#include <stdio.h>
int main()
{
    int n, i;
    //freopen("C-large.in","r",stdin);
    //freopen("c.out","w",stdout);
    scanf("%d",&n);
    for(i=0; i<n; i++)
    {
        int m, j;
        int psum = 0;
        int csum = 0;
        int min = 100000000;
        int num;
        scanf("%d",&m);
        for(j=0; j<m; j++)
        {
            scanf("%d",&num);
            if(num < min)
                min = num;
            psum = num ^ psum;
            csum = csum + num;
        }
        if(psum != 0)
            printf("Case #%d: NO\n",i+1);
        else
            printf("Case #%d: %d\n",i+1,csum - min);
    }
}