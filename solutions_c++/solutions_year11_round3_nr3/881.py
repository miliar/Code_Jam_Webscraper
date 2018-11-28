#include <cstdio>
#include <cstring>
#define MAX 110
int t,n,h,l,freq[MAX];
int prueba()
{
    for (int i=l; i<=h; i++)
    {
        int cont=0;
        for (int j=1; j<=n; j++)
        {
            if ((i%freq[j])==0 || (freq[j]%i)==0)
                cont++;
            else
                j=n+1;
        }
        if (cont==n)
            return(i);
    }
    return(-1);
}
int main()
{
    scanf("%d",&t);
    for (int g=1; g<=t; g++)
    {
        scanf("%d%d%d",&n,&l,&h);
        for (int i=1; i<=n; i++)
            scanf("%d",&freq[i]);
        int res=prueba();
        printf("Case #%d: ",g);
        if (res==-1)
            printf("NO\n");
        else
            printf("%d\n",res);
    }
}
