#include <stdio.h>
char s[1000];
char a[200][200];
int i,j,n,t,ii,i1;
double wp[200],owp[200],oowp[200];
int main()
{
freopen("A-large.in","r",stdin);
freopen("A-large.out","w",stdout);
scanf("%d",&t);
gets(s);
for(ii=1;ii<=t;ii++)
   {
   printf("Case #%d:\n",ii);
   scanf("%d",&n);
   gets(s);
   for(i=0;i<n;i++)
      gets(a[i]);
   for(i=0;i<n;i++)
      {
      int wf = 0, rd = 0;
      for(j=0;j<n;j++)
         {
         if(a[i][j] != '.')
            rd++;
         if(a[i][j] == '1')
            wf++;
         }
      if(!rd) wp[i] = 0.;
      else wp[i] = wf * 1. / rd;
      }
   for(i=0;i<n;i++)
      {
      int rd = 0;
      owp[i] = 0.;
      for(j=0;j<n;j++)
         if(a[i][j] != '.')
            {
            int rdd = 0;
            double wpp = 0;
            for(i1=0;i1<n;i1++)
               if(a[j][i1] != '.' && i1 != i)
                  {
                  rdd++;
                  if(a[j][i1] == '1')
                     wpp += 1.;
                  }
            if(rdd)
               wpp /= rdd;
            owp[i] += wpp;
            rd++;
            }
      if(rd)
         owp[i] /= rd;
      }
   for(i=0;i<n;i++)
      {
      int rd = 0;
      oowp[i] = 0.;
      for(j=0;j<n;j++)
         if(a[i][j] != '.')
            {
            oowp[i] += owp[j];
            rd++;
            }
      if(rd)
         oowp[i] /= rd;
      }
   for(i=0;i<n;i++)
      printf("%.10lf\n",0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
   }
return 0;
}
