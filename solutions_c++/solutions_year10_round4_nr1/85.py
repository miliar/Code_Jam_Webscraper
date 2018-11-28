#include <cstdio>
#include <algorithm>
using namespace std;
const int L=105;
int table[L][L],tmp[L][L];
main()
{
   int n,i,j,k,l;
   int cases,t;
   int done,test;
   int ans[10],v,h;

   scanf("%d",&cases);
   for(t=1;t<=cases;t++)
   {
      scanf("%d",&n);
      for(i=0;i<n;i++)
         for(j=0;j<=i;j++)
            scanf("%d",&table[i-j][j]);

      for(i=n-1;i>=0;i--)
         for(j=1;j<=i;j++)
            scanf("%d",&table[n-j][j+n-i-1]);

      test=4;
      for(l=0;l<test;l++)
      {
         for(i=n;i>=1;i--)
         {
            done=1;
            for(j=0;j<i && done;j++)
               for(k=0;k<i && done;k++)
                  if(table[j][k]!=table[i-k-1][i-j-1])
                     done=0;
            if(done) break;
         }
         ans[l]=i;
         memmove(tmp,table,sizeof(tmp));

         for(i=0;i<n;i++)
            for(j=0;j<n;j++)
               table[i][j]=tmp[j][n-i-1];
      }
      v=max(ans[0],ans[2]);
      h=max(ans[1],ans[3]);
      printf("Case #%d: %d\n",t,(n-v+n-h+n)*(n-v+n-h+n)-n*n);
   }
}
