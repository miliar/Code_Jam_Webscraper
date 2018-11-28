#include<stdio.h>
int main()
    {
        freopen("D-small-attempt2 (2).in","r",stdin);
        freopen("AAA.out","w",stdout);
        int T;
        scanf("%d",&T);
        for(int ii = 1 ; ii <=T;ii++)
            {
                int n;
                scanf("%d",&n);
                int ans = 0;
                for(int i = 1 ; i<= n;i++)
                    {
                        int t;
                        scanf("%d",&t);
                        if(t != i) ans++;
                    }
                printf("Case #%d: %d.000000\n" , ii,ans);
            }

        return 0;
    }
