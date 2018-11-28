#include <stdio.h>

int main()
{
    int i,j;
    int n;
    int a,b;
    int cnt;
    int mid;
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        cnt=0;
        scanf("%d%d",&a,&b);
        for(j=a;j<=b;j++)
        {
            if(j>=100)
            {
                mid = j/100 + (j%100)*10;
                if(mid <=b && mid>j)
                {
                    cnt++;
                }
                mid = j/10 + (j%10)*100;
                if(mid <=b && mid>j)
                {
                    cnt++;
                }
            }
            else if(j>=10)
            {
                mid = j/10 + (j%10)*10;
                if(mid <=b && mid>j)
                {
                    cnt++;
                }
            }
        }
        printf("Case #%d: %d\n",i,cnt);
    }
    return 1;
}
