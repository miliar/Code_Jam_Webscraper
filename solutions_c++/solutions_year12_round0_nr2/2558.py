#include<iostream>
#include<cstdio>
#include<algorithm>
#include<fstream>
using namespace std;
int t,q,i,n,s,p,a[256],l,r,ans,br;

int main()
{
  FILE *in=fopen("B-large.in","r");
  FILE *out=fopen("B-large.out","w");
  fscanf(in,"%d",& t);
  for(q=1;q<=t;q++)
  {
    ans=0;
    br=0;
    fscanf(in,"%d%d%d",& n,& s,& p);

    l=p+2*(p-2);
    if (l < 0) l=0;
    if (l < p) l=p;
    r=3*p-2;
    if (r < 0) r=0;

    for(i=1;i<=n;i++)
    {
      fscanf(in,"%d",& a[i]);
      if (a[i] >= r) ans++;
      else
      if (a[i] >= l) br++;
    }

    ans+=min(s,br);
    fprintf(out,"Case #%d: %d\n", q, ans);
  }
return 0;
}
