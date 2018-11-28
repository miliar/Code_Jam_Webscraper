#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;
int ii,t,index,i,n,a,dam;
char c;
int I[3],svla[3];
int main()
{
freopen("A-large.in","r",stdin);
freopen("A-large.out","w",stdout);
cin>>t;
for(ii=1;ii<=t;ii++)
   {
   printf("Case #%d: ",ii);
   cin>>n;
   I[0] = 1;
   I[1] = 1;
   svla[0] = 0;
   svla[1] = 0;
   for(i=0;i<n;i++)
      {
      cin>>c>>a;
      if(c == 'O')
         index = 0;
      else
         index = 1;
      int kk = 0;
      if(svla[index] < svla[!index] )
         {
         kk = svla[!index] - svla[index];
         if(kk >= abs(I[index] - a) + 1) dam = 1;
         else dam = abs(I[index] - a) + 1 - kk;
         svla[index] = svla[!index] + dam;
         }
      else
         svla[index] += abs(I[index] - a) + 1;
      I[index] = a;
      }
   printf("%d\n",max(svla[0],svla[1]));
   }
return 0;
}
