#include <cstdio>
int main()
{
    int t;
    scanf("%d",&t);
    for(int c=1;c<=t;c++)
    {
        int n,k;
        scanf("%d%d",&n,&k);
        printf("Case #%d: %s\n",c,(k+1)%(1<<n)?"OFF":"ON");
    }
}
