#include <iostream>
#include <algorithm>
using namespace std;
long long r,n,m,cer1,cer2,totsum,rd;
struct asdf
{      
       long long num,jmp,sum,tmp,tmps,add;
};
asdf a[2000];
void init()
{
     memset(a,0,sizeof(a));
     int i,k,j;
     long long sum,tmp=0,x,y;
     scanf("%d%d%d",&i,&j,&k);
     r=j;m=i;n=k;
     totsum=0;
     for (i=0;i<n;i++)
     {
         scanf("%d",&k);
         a[i].num=k;
         totsum+=a[i].num;
     }
     for (i=0;i<n;i++)
     {
         a[i].add=-1;a[i].tmp=a[i].tmps=0;
         if (r>=totsum)
         {
             a[i].jmp=i;
             a[i].sum=totsum;
             continue;
         }
         k=r;
         j=i;
         while (a[j].num<=k)
         {
               k-=a[j].num;
               a[i].sum+=a[j].num;
               j++;j%=n;
         }
         a[i].jmp=j;
     }
     long long z=1;
     sum=0;
     x=0;y=a[0].jmp;
     a[0].tmps=0;
     a[0].tmp=1;
     if (y==0)
     {
          a[0].tmp=1;
          a[0].add=a[0].sum;    
          return;
     }
     while (a[y].tmp==0)
     {
           a[y].tmp=(++z);
           sum+=a[x].sum;
           a[y].tmps=sum;
           x=y;y=a[y].jmp;
     }
     a[y].tmp=z+1-a[y].tmp;
     sum+=a[x].sum;
     a[y].add=sum-a[y].tmps;
}
void work()
{
     long long ans=0;
     int i,k,j;
     long long x,y,z;
     x=0;
     while (m!=0)
     {
           if (a[x].add!=-1&&a[x].tmp<=m)
           {
               ans+=a[x].add*(m/a[x].tmp);
               m%=a[x].tmp;
               continue;
           }
           ans+=a[x].sum;
           x=a[x].jmp;
           m--;
     }
     cout<<ans;
}
int main()
{
   // freopen("i.txt","r",stdin);
  //  freopen("o.txt","w",stdout);
    int tt,i,k,j;
    k=0;
    for (scanf("%d",&tt);tt;tt--)
    {
        k++;
        printf("Case #%d: ",k);
        init();
        work();
        puts("");
    }
}
