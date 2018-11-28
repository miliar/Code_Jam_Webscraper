#include<iostream>
#include<string.h>
#include<stdio.h>
#include<algorithm>
using namespace std;
int a[600][600];
char s[666];
int main()
{
    freopen("B-small-attempt2.in","r",stdin);
    freopen("B.out","w",stdout);
    int i,j,k,n,m,d,cs,qq=0,q=0;
    scanf("%d",&cs);
    while (cs--)
    {
       scanf("%d%d%d",&n,&m,&d); 
       gets(s);
       for (i=1;i<=n;i++)
       {
           gets(s);
           for (j=1;j<=m;j++)
           a[i][j]=s[j-1]-48;
       }
       int mm=max(n,m);
       bool flag=false;
       while (mm>=3)
       {
           for (i=1;i<=n-mm+1;i++)
           {for (j=1;j<=m-mm+1;j++)
           {
               bool b=true;
               int x=0,y=0,sum=0;
               for (k=i;k<i+mm;k++)
               {
                   for (q=j;q<j+mm;q++)
                   {
                      if (k==i&&q==j||k==i+mm-1&&q==j||k==i&&q==j+mm-1||k==i+mm-1&&q==j+mm-1)
                      continue;
                  //    if (a[k][q]>d+9||a[k][q]<d) {b=false;break;}
                      x+=a[k][q]*(k-i);
                      y+=a[k][q]*(q-j);
                      sum+=a[k][q];
                   }
               }
               x*=2;y*=2;
               if ((mm-1)*sum!=x||(mm-1)*sum!=y) continue;
               flag=true;
               printf("Case #%d: %d\n",++qq,mm);
               break;
           }
           if (flag) break;
           }
           if (flag) break;
           mm--;
       }
       if (!flag)
       printf("Case #%d: IMPOSSIBLE\n",++qq);
    }
}
             
