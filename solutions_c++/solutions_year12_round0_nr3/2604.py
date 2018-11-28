#include<iostream>
#include<cstdio>
#include<algorithm>
#include<fstream>
using namespace std;
int t,q,i,j,a,b,cop,br,x,y,n,m;
long long ans;
int pow10[16];
int v,h[128],g[128];
bool fl;

int main()
{
  FILE *in=fopen("C-large.in","r");
  FILE *out=fopen("C-large.out","w");
  fscanf(in,"%d",& t);

  pow10[0]=1;
  for(i=1;i<=11;i++) pow10[i]=pow10[i-1]*10;

  for(q=1;q<=t;q++)
  {
      fscanf(in,"%d%d",& a,& b);
      ans=0;
      for(n=a;n<b;n++)
      {
          v=0;
          br=0;
          cop=n;
          while(cop!=0) { br++;cop/=10;}
          for(i=1;i<=br-1;i++)
          {
              x=n%pow10[i];
              y=n/pow10[i];
              m=x*pow10[br-i]+y;
              if (m<=b && m>n)
              {
                  fl=true;
                  for(j=1;j<=v;j++)
                   if (n==h[j] && m==g[j]) {fl=false;break;}
                  if (fl)
                  {
                      v++;h[v]=n;g[v]=m;
                      ans++;
                  }
              }
          }
      }
      fprintf(out,"Case #%d: %lld\n", q, ans);
  }
  fclose(in);
  fclose(out);
return 0;
}
