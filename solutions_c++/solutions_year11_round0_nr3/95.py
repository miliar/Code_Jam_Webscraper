#include <algorithm>
#include <stdio.h>
#include <stack>
#include <queue>
#include <vector>
#include <string>
#include <map>
#include <set>
using namespace std;
int a,mi,xo,sum;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
     int N;
   scanf("%d",&N);
   for(int _r=0;_r<N;_r++)
   {
       xo=0;
       mi=1<<30;
       sum=0;
       int n;
       scanf("%d",&n);
       for(int c=0;c<n;c++)
       {
        scanf("%d",&a);
        xo^=a;
        mi=min(mi,a);
        sum+=a;
       }
       printf("Case #%d: ",_r+1);
       if(xo) printf("NO\n");
       else
       printf("%d\n",sum-mi);
   }
}
