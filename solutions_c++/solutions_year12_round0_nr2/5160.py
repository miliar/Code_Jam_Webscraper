#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;
int main()
{ int i,j=0,x,y,p,q,count,counti,d,a[110],e;
 scanf("%d",&i);
 while(j<i)
 { scanf("%d",&x);
   scanf("%d",&p);
   scanf("%d",&q);
   counti=0;
   count=0;
   y=0;
   while(y<x)
  {scanf("%d",&a[y]);
  y++;}
  sort(a,a+x);
  y=0;
  if(p==q && p==0)
  {counti=x;
  goto h;}
  while(y<x)
  { d=a[y]%3;
    e=a[y]/3;
 // printf("%d",d);

    if(a[y]==0)
    goto g;
    if(d==0)
    { if(count<p)
      { if(e+1>=q)
        {counti++;
        count++;}
      }else
       {if(e>=q)
        counti++;}
    }
    else if(d==1)
   { if(count<p)
     {
          if(e+1>=q)
          {counti++;
          count++;}
     }else
     {
         if(e+1>=q)
         counti++;
     }
   }
    else
    { if(count<p)
     {
          if(e+2>=q)
          {counti++;
          count++;}
     }else
     {
         if(e+1>=q)
         counti++;
     }
   } g:
    y++;
  }h:
  printf("Case #%d: %d",j+1,counti);
  if(j<i-1)
  {
      printf("\n");
  }


j++; }
return 0;}


