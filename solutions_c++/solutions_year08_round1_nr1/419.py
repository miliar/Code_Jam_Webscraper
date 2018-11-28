#include <stdio.h>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
using namespace std;
long long ar1[1000],ar2[1000],h;
int main()
{
scanf("%lld",&h);
for(int kk=0;kk<h;kk++)
{
  long long n,res=0;
  scanf("%lld",&n);
  for(int r=0;r<n;r++)   
     scanf("%lld",&ar1[r]);  
for(int r=0;r<n;r++)   
     scanf("%lld",&ar2[r]);       
   sort(ar1,ar1+n);
   sort(ar2,ar2+n);
   reverse(ar2,ar2+n);
   for(int r=0;r<n;r++)
      res+=ar1[r]*ar2[r];
      printf("Case #%d: %lld\n",kk+1,res);
   }   
  return 0;
}
