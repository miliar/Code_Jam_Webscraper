#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std ;


int n;
int arr[20];


int main()
{
    FILE *in=fopen("candy.in","r");
    freopen("candy.out","w",stdout);
    int c,c2;
    int tests;
    fscanf(in,"%d",&tests);
    int testn=1;
    while (tests--)
    {
        printf("Case #%d: ",testn);
        testn++;
        fscanf(in,"%d",&n);
        for (c=0;c<n;c++)
            fscanf(in,"%d",&arr[c]);
        int ret=-1;
        for (c=1;c<(1<<n)-1;c++)
        {
            int sum1=0,sum2=0;
            int or1=0,or2=0;
            for (c2=0;c2<n;c2++)
            {
                if (c&(1<<c2))
                {
                    sum1+=arr[c2];
                    or1^=arr[c2];
                }
                else {
                    sum2+=arr[c2];
                    or2^=arr[c2];
                }
            }
            if (or1==or2)
            {
                sum1=max(sum1,sum2);
                ret=max(ret,sum1);
            }
        }
        if (ret==-1)printf("NO\n");
        else printf("%d\n",ret);
    }
//    system("pause");
    return 0;
}


































