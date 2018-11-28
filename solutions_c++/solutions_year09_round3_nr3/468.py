#include <iostream>
#include <stdio.h>
#include <map>
#include <math.h>
#include <vector>
#include <algorithm>
#include <string>
#define u 200
using namespace std;

int t,fix[u],m[u],q,i,k,l,cur,ans,n;

int main()
{
    freopen("C.in","r",stdin);
    freopen("Cbrute.out","w",stdout);
    scanf("%d",&t);
    for (i=1; i<=t; i++)
    {
     memset(fix,0,sizeof(fix));
     scanf("%d%d",&n,&q);
     for (l=0; l<q; l++) { scanf("%d",&m[l]); m[l]--; }
     ans=1000000000;
     do
     {
       cur=0;
       memset(fix,0,sizeof(fix));
       for (l=0; l<q; l++)
       {
          fix[ m[l] ]=1;
          k=m[l]-1;
          while (k>=0 && fix[k]==0) { k--; cur++; }
          k=m[l]+1;
          while (k<n && fix[k]==0) { k++; cur++; }
       }
       if (cur<ans) ans=cur;
     }
     while (next_permutation(m,m+q));
     printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
