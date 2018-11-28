#include <stdio.h>
#include <algorithm>
#include <iostream>
using namespace std;

long a[1000],b[1000],t,n,l;
main()
{
  freopen("scalar.in","r",stdin);
  freopen("scalar.out","w",stdout);      
  scanf("%d",&t);
  for (long i=0; i<t; i++)
  {
   scanf("%d",&n);
   for (l=0; l<n; l++)
    scanf("%d",&a[l]);
   for (l=0; l<n; l++)
    scanf("%d",&b[l]);
   sort(a,a+n); sort(b,b+n);
   long long ans=0,o;
   for (l=0; l<n; l++) 
    { o=a[l]; o*=b[n-l-1]; ans+=o; }
   cout<<"Case #"<<i+1<<": "<<ans<<endl;
  }
} 
