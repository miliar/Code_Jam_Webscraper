#include<cstdio>
#include<algorithm>
using namespace std;
int a[1005];

int main()
{
    int cas,n,tmp,t,i,j;

    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    scanf("%d",&cas);
    for(j = 1;j <= cas;j++)
    {
        scanf("%d",&n);
        tmp = 0;
        for(i = 0;i < n;i++)
        {
            scanf("%d",&t);
            tmp = tmp ^ t;
            a[i] = t;
        }
        printf("Case #%d: ",j);
        if(tmp != 0)
            printf("NO\n");
        else
        {
            tmp = 0;
            sort(a,a+n);
            for(i = 1;i < n;i++)
                tmp += a[i];
            printf("%d\n",tmp);
        }
    }

    return 0;
}
