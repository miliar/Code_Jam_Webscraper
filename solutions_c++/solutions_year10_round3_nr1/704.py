#include<stdio.h>

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    
    int cases,ii,n,i,j,a[1002],b[1002],an;
    
    scanf("%d",&cases);
    for(ii=1;ii<=cases;ii++)
    {
        scanf("%d",&n);
        for(i=1;i<=n;i++)scanf("%d%d",&a[i],&b[i]);
        
        an=0;
        for(i=1;i<=n;i++)for(j=i+1;j<=n;j++)
            if((a[i]<a[j] && b[i]>b[j]) || (a[i]>a[j] && b[i]<b[j]))an++;
        printf("Case #%d: %d\n",ii,an);
    }
    
    fprintf(stderr,"END\n");
    while(1);
    return 0;
}
