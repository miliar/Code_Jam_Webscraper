#include<stdlib.h>
#include<stdio.h>
int main()
{
    freopen("A-small.in","r",stdin);
    freopen("A-small.out","w",stdout);
    int i,j,a[100][2],n,m,k=0;
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
         scanf("%d",&m);
         for(j=0;j<m;j++)
         {
            scanf("%d%d",&a[j][0],&a[j][1]);
         }
         for(int w=0;w<m;w++)
         {
                 for(int p=w+1;p<m;p++)
                 {
                         if(((a[w][0]<a[p][0])&&(a[w][1]>a[p][1]))||((a[w][0]>a[p][0])&&(a[w][1]<a[p][1])))
                         k++;
                 }
         }
         printf("Case #%d: %d\n",i,k);
         k=0;
    }
    
    
     
    system("pause");
    return 0;
}


