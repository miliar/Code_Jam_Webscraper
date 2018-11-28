//Written by imon
//26-04-10
#include<stdio.h>
#include<math.h>

int main()
{
    freopen("A-small-attempt.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t, i;
    long long n, k, j, l, m, p, chk, prev = 0;

    scanf("%d", &t);
    for(i=1; i<=t; i++)
    {
        scanf("%lld%lld", &n, &k);

        for(j =1, l=1; l<n; j=prev*2+1, l++)
        {
            prev = j;
            //printf("%lld ", j);                 //debugg
        }
        p=j;
        for(m = 2; j < k ; m++)
        {
            j++;
            j = j + p;
            //j++;
        }
        if(j==k)
            printf("Case #%d: ON", i);
        else
            printf("Case #%d: OFF", i);
        /*else if(k<j)
        {
            printf("Case #%d: OFF", i);
        }
        else
        {
            //chk = k-j;
            if(k%j==0)
                printf("Case #%d: ON", i);
            else
                printf("Case #%d: OFF", i);
        }*/
        if(i!=t)
            printf("\n");
    }
    return 0;
}


