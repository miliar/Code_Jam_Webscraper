#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

struct case1
{
 long x,y,r;
}cir[2005]={0};

long h[2005]={0};

bool cmp(long x,long y)
{
 return cir[x].r>cir[y].r;
}

int main()
{
 long t;
 long i,j,k;
 long n,w,l;
 long bd=0;
 long cur;
 
 freopen("2.in","r",stdin);
 freopen("2.out","w",stdout);
 
 scanf("%ld",&t);
 for(i=1;i<=t;i++)
   {
    printf("Case #%ld: ",i);
    scanf("%ld%ld%ld",&n,&w,&l);
    for(j=1;j<=n;j++)
      {
       scanf("%ld",&cir[j].r);
       h[j]=j;
      }
    sort(h+1,h+n+1,cmp);
    bd=-200000;
    cur=2000000000;
    for(j=1;j<=n;j++)
      {
       long down=-cir[h[j]].r;
       
       loop:
       
       if(bd+cir[h[j]].r>w)
        bd=-200000;
       
       if(bd<0)
        {
         bd=-cir[h[j]].r;
         cur=2000000000;
        }
       
       for(k=1;k<j;k++)
         if(cir[h[k]].x+cir[h[k]].r>bd&&cir[h[k]].x-cir[h[k]].r<bd+2*cir[h[j]].r)
          {
           if(cir[h[k]].y+cir[h[k]].r>down)
            down=cir[h[k]].y+cir[h[k]].r;
          }
       cir[h[j]].x=bd+cir[h[j]].r;
       cir[h[j]].y=down+cir[h[j]].r;
       if(cir[h[j]].y>l)
        {
         bd+=2*cir[h[j-1]].r;
         down=-cir[h[j]].r;
         goto loop;
        }
       
       if(cur==2000000000)
        cur=down+2*cir[h[j]].r;
       if(down+2*cir[h[j]].r>=cur)
        bd+=2*cir[h[j]].r;
      }
    for(j=1;j<=n;j++)
      printf("%ld %ld%c",cir[j].x,cir[j].y,j==n?'\n':' ');
   }
 
 return 0;
}
