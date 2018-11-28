#include <cstdio>
#include <algorithm>
using namespace std;
FILE *in, *out;
int a[1500];
int main()
{
  int T,t,i,n,xorul,sum;
  in=fopen("candy.in","r");
  out=fopen("candy.out","w");
  fscanf(in,"%d",&T);
  for (t=1;t<=T;t++)
  {
    fscanf(in,"%d",&n);
    xorul=sum=0;
    for (i=1;i<=n;i++)
    {
      fscanf(in,"%d",&a[i]);
      sum+=a[i];
      xorul^=a[i];
    }
    sort(a+1,a+n+1);
    fprintf(out,"Case #%d: ",t);
    if (!xorul)
      fprintf(out,"%d\n",sum-a[1]);
    else
      fprintf(out,"NO\n");
  }
  fclose(in);
  fclose(out);
  return 0;
}
