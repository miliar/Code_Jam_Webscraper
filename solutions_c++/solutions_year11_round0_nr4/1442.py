#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

int main()
{
  freopen("goro.in","r",stdin);
  freopen("goro.out","w",stdout);
  int t,to=0;
  scanf("%d",&t);
  while(t--)
  {
    to++;
    printf("Case #%d: ",to);
    int n,i,a[1001],b[1001],check=0;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
      scanf("%d",&a[i]);
      b[i]=a[i];
    }
    sort(b,&b[n]);
    for(i=0;i<n;i++)
      if(a[i]!=b[i]) check++;
    printf("%d.000000\n",check);
  }
  return 0;
}
