#include <algorithm>
#include <stdio.h>
#include <stack>
#include <queue>
#include <vector>
#include <string>
#include <map>
#include <set>
using namespace std;
int a;
char pal[10];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
     int N;
   scanf("%d",&N);
   for(int _r=0;_r<N;_r++)
   {
      int n;
      scanf("%d",&n);
      int O=1,B=1,TO=0,TB=0,last=-1;
      for(int r=0;r<n;r++)
       {
         scanf("%s %d",pal,&a);
         if(  pal[0]=='O' ) {
            if ( last==1) TO=max( TB+1,TO+abs(a-O)+1 );
            else TO+=abs(a-O)+1;
            O=a;
            last=0;
         }
         else {
            if ( last==0) TB=max( TO+1,TB+abs(a-B)+1 );
            else TB+=abs(a-B)+1;
            B=a;
            last=1;
         }
       }
       printf("Case #%d: %d\n",_r+1,max(TO,TB));
   }
}
