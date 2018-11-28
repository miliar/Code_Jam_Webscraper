#include <stdio.h>
#include <iostream>
#include <string.h>
#define u 11

using namespace std;
int fix[u],fix2[u],l,nn,k,t,i,n;
bool boo;

int main()
{
 freopen("2.in","r",stdin);
 freopen("2.out","w",stdout);

 scanf("%d",&t);
 for (i=1; i<=t; i++)
 {
     memset(fix,0,sizeof(fix));
     scanf("%d",&n);
     nn=n;
     while (nn)
     {
         fix[nn%10]++;
         nn/=10;
     }

   //  cout<<"modis"<<endl;
    // for (l=0; l<10; l++) printf("%d",fix[l]);
     for (l=n+1;;l++)
     {
         memset(fix2,0,sizeof(fix2));
         nn=l;
         while (nn)
         {
          fix2[nn%10]++;
          nn/=10;
         }
       bool boo=true;
       for (k=1; k<10; k++)
        if (fix[k]!=fix2[k]) { boo=false; break; }
      if (boo) { printf("Case #%d: %d\n",i,l); break; }
     }
 }
 return 0;
}
