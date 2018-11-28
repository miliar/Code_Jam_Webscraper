#include<stdio.h>

int main(void){
    int T;

    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    scanf("%d",&T);

    for(int t = 0; t<T; t++)
    {
        int n,s,p;
        scanf("%d%d%d",&n,&s,&p);
        int cnt = 0;
        int a, sc = 0;
        for(int i = 0; i<n; i++)
        {
            scanf("%d",&a);

            if(a >= 3*p - 2)
            {
                cnt++;
            }
            else if(sc<s)
            {
                int x = 3*p - 4;
                if(a>p && x <= a)
                {
                    cnt++;
                    sc++;
                }
            }
        }

        printf("Case #%d: %d\n", t+1, cnt);
    }
    return 0;
}
