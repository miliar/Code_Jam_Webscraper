#include<algorithm>
#include<cstdio>
using namespace std;
main()
{
    int T,cases;
    int i,j,k,n,m,t;
    freopen("A-large.in","r",stdin);
    freopen("out","w",stdout);
    scanf("%d",&T);
    for(cases=1;cases<=T;cases++)
    {
        scanf("%d %d",&n,&m);
        n=(1<<n)-1;
        m=m%(n+1); 
//        printf("%d %d\n",n,m);
        printf("Case #%d: ",cases);
        if(m==n)
            puts("ON");
        else
            puts("OFF");
    }
}
