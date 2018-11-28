#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string.h>
#define u 100000000

using namespace std;

char s[200][200];
long m[200][200], x, l,t, test, k, K;

bool check(long a)
{long i, j, k, boo;

 for (i=0; i<x; i++)
  for (j=0; j<x; j++)
  {
   boo = 1;
   for (k=0; k<K; k++)
     if (i+k>=x || m[i+k][j]!=a) boo = 0;      
   if (boo) return true;
   
   boo = 1;
   for (k=0; k<K; k++)
     if (j+k>=x || m[i][j+k]!=a) boo = 0;      
   if (boo) return true;

   boo = 1;
   for (k=0; k<K; k++)
     if (i+k>=x || j+k>=x || m[i+k][j+k]!=a) boo = 0;      
   if (boo) return true;

   boo = 1;
   for (k=0; k<K; k++)
     if (i-k<0 || k+j>=x || m[i-k][j+k]!=a) boo = 0;
     
   if (boo) return true;
 }
 
 
 return false;
}

int main()
{
    freopen("a-small.in","r",stdin);
    freopen("a-large.out","w",stdout);
    scanf("%d",&t);
    
    for (test = 1; test<=t; test++)
    {
        printf("Case #%d: ", test);
        scanf("%d %d\n",&x,&K);
        memset(m,0,sizeof(m));
        for (l=0; l<x; l++) gets(s[l]);
        long cur;
        for (l=0; l<x; l++)
        {
            cur = 0;
            for (k=x-1; k>=0; k--)
             if (s[l][k]!='.') 
             {
              if (s[l][k]=='R') m[x-1-cur][x-l-1] = 1; else m[x-1-cur][x-l-1] = 2;
              cur++;
             }      
        }
               
        long p1 = check(1), p2 = check(2);
        if (p1 && p2) puts("Both"); else
        if (p1) puts("Red"); else
        if (p2) puts("Blue"); else puts("Neither");
        
        
         
    }
    return 0;    
}
