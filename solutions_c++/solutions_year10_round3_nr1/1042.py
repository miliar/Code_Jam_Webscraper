#include<stdio.h>


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int a[1005],b[1005],i,j,t,n,p=0,count;
    scanf("%d",&t);

    while(t--)
    {
    scanf("%d",&n);

    for(i=0;i<n;i++)
     {
         scanf("%d%d",&a[i],&b[i]);
     }

     count=0;
  for(i=0;i<n;i++)
   for(j=0;j<n;j++)
   if(i!=j && b[i]>b[j] && a[i]<a[j])
     count++;
    printf("Case #%d: ",++p);
    printf("%d\n",count);
    }
    return 0;
}



