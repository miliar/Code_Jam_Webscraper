#include <iostream>
using namespace std;
int t,z,q,j,n;
char f[100][100];
int main()
{
 freopen("input.txt","r",stdin);
 freopen("output.txt","w",stdout);
 scanf("%d",&t);
 for (int i=1;i<=t;++i)
 {
  printf("Case #%d:\n",i);
  cin>>n;
  for (j=0;j<n;++j) 
   for (z=0;z<n;++z) cin>>f[j][z];
  double wp,owp[100],rpi[100];
  for (j=0;j<n;++j)
  {
   int k=0,won=0;
   for (z=0;z<n;++z)
   {
    if (f[j][z]!='.') ++k;
    if (f[j][z]=='1') ++won;
   } 
   wp=double(won)/k;

   int nmb=0; double av=0;
   for (z=0;z<n;++z)
    if (f[j][z]!='.')
    {
     ++nmb;
     int k=0,won=0;
     for (q=0;q<n;++q)
     {
      if (f[z][q]!='.' && q!=j) ++k;
      if (f[z][q]=='1' && q!=j) ++won;
     } 
     av+=double(won)/k;
    }
   owp[j]=av/nmb;
   rpi[j]=0.25*wp+0.5*owp[j];
  }
  for (j=0;j<n;++j)
  {
   int k=0; double av=0;
   for (z=0;z<n;++z)
    if (f[j][z]!='.') { av+=owp[z]; ++k; }
   rpi[j]+=0.25*av/k;
   printf("%.15lf\n",rpi[j]);
  }
 }
}