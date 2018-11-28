#include <stdio.h>
#define eps 1e-7
double fabs(double a)
{
return a>0?a:-a;
}
int t,i,n,m,d,j,i1,j1,ii,jj,K,N,M,sig,ia,ja;
double mci,mcj,jami1,jami2;
char st[10000];
char s[1000][1000];
int mas[1000][1000];
double jm1[1009][1009][5];
double jm2[1009][1009][5];
int main()
{
freopen("B-large.in","r",stdin);
freopen("B-large.out","w",stdout);
scanf("%d",&t);
gets(st);
for(int it=1;it<=t;it++)
   {
   printf("Case #%d: ",it);
   scanf("%d %d %d",&n,&m,&d);
   gets(st);
   for(i=0;i<n;i++)
      {
      gets(s[i]);
      for(j=0;s[i][j];j++)
         mas[i][j] = d + (int)(s[i][j] - '0');
      }
   K = 0;
   for(sig = 3; sig <= n; sig++)
      for(i=0;i<n;i++)
         for(j=0;j<m;j++)
               {
               i1 = i + sig - 1;
               j1 = j + (i1 - i);
               if(i1 >= n || j1 >= m) break;
               N = (i1 - i + 1);
               mci = i + N / 2.;
               mcj = j + N / 2.;
               ia = (i<<1) + N;
               ja = (j<<1) + N;
               if(sig <= 4)
                  {
                  jami1 = 0;
                  jami2 = 0;
                  }
               else
                  {
                  jami1 = jm1[ia][ja][(sig-2)%3];
                  jami2 = jm2[ia][ja][(sig-2)%3];
                  }
               if(sig != 3)
                  {
                  ii = i+1; jj = j+1;
                  jami1 += (ii + 0.5 - mci) * mas[ii][jj];
                  jami2 += (jj + 0.5 - mcj) * mas[ii][jj];
                  ii = i+1; jj = j1-1;
                  jami1 += (ii + 0.5 - mci) * mas[ii][jj];
                  jami2 += (jj + 0.5 - mcj) * mas[ii][jj];
                  ii = i1-1; jj = j+1;
                  jami1 += (ii + 0.5 - mci) * mas[ii][jj];
                  jami2 += (jj + 0.5 - mcj) * mas[ii][jj];
                  ii = i1-1; jj = j1-1;
                  jami1 += (ii + 0.5 - mci) * mas[ii][jj];
                  jami2 += (jj + 0.5 - mcj) * mas[ii][jj];
                  }
               for(ii=i+1;ii<i1;ii++)
                  {
                  jami1 += (ii + 0.5 - mci) * (mas[ii][j] + mas[ii][j1]);
                  jami2 += (j + 0.5 - mcj) * mas[ii][j];
                  jami2 += (j1 + 0.5 - mcj) * mas[ii][j1];
                  }
               for(jj=j+1;jj<j1;jj++)
                  {
                  jami1 += (i + 0.5 - mci) * mas[i][jj];
                  jami1 += (i1 + 0.5 - mci) * mas[i1][jj];
                  jami2 += (jj + 0.5 - mcj) * (mas[i][jj] + mas[i1][jj]);
                  }
               jm1[ia][ja][sig%3] = jami1;
               jm2[ia][ja][sig%3] = jami2;
               if(N > K && fabs(jami1) < eps && fabs(jami2) < eps)
                   K = N;
               }
   if(K < 3) printf("IMPOSSIBLE\n");
   else printf("%d\n",K);
   }
return 0;
}
