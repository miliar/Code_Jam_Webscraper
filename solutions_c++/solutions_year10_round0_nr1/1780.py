#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

int main()
{
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int t,n,k,q;
  scanf("%d",&t);
  for (int i=0;i<t;i++){
   scanf("%d%d",&n,&k);
   q=1;
   for (int j=0;j<n;j++) q*=2;
   k%=q;
   if (k+1==q) printf("Case #%d: ON\n",i+1);
   else printf("Case #%d: OFF\n",i+1);

  }
  return 0;
}
