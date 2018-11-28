#include <cstdio>
#define nmax 250
FILE *in,*out;
long long a[nmax], b[nmax], d;
int n;
const double inf = 1e20;
const double eps = 1e6;
inline double maxim(double x,double y)
{
  return x>y?x:y;
}
int ver(long long rez)
{
  int i;
  double timp, minv , dist_inceput;
  timp = rez / eps;
  
  minv = -inf;
  
  for (i=1;i<=n;i++)
  {
    dist_inceput = maxim ( minv + d, a[i] - timp);
    if ( b[i] > 1)
      minv  = dist_inceput + (b[i]-1) * d;
    else
      minv = dist_inceput;
    if ( minv - a[i] > timp )
      return 0;
  }
  return 1;
}

int main()
{
  int T,t;
  long long i,rez;
  in=fopen("revenge.in","r");;
  out=fopen("revenge.out","w");

  fscanf(in,"%d",&T);
  
  for (t=1;t<=T;t++)
  {
    fscanf(in,"%d%lld",&n,&d);
    for (i=1;i<=n;i++)
    {
      fscanf(in,"%lld%lld",&a[i],&b[i]);
    }
    rez=0;
    for (i=((long long )1)<<61;i;i>>=1)
    {
      rez+=i;
      if (ver(rez))
        rez-=i;
    }
    fprintf(out,"Case #%d: %lf\n",t,(rez+1)/eps);
  }
}