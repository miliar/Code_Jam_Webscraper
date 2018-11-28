#include <stdio.h>
int main()
{
    int n;
    int i,j,k;
    freopen("c:\\aaa","r",stdin);
    freopen("c:\\bbb.txt","w",stdout);
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        unsigned int a,b;
        scanf("%d%d",&a,&b);
        printf("Case #%d: %s\n", i, (  b%(1<<a)==( (1<<a)-1)    )?"ON":"OFF");
    }
    return 0;
}
