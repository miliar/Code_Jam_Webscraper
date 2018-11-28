#include <stdio.h>
#include <string.h>

long array[10000][3],test,n,i,j,mx,a,b,t=0;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%ld",&test);
    while(test--)
    {
        memset(array,0,sizeof(array));
        scanf("%ld",&n);
        mx=0;
        for(i=1;i<=n;++i)
            scanf("%ld %ld",&array[i][0],&array[i][1]);


        for(i=1;i<=n;++i)
        {
            for(j=i+1;j<=n;++j)
            {
                    if((array[i][0]-array[j][0])*(array[i][1]-array[j][1])<0)
                        ++mx;
            }
        }
        printf("Case #%ld: %ld\n",++t,mx);
    }
    return 0;
}
