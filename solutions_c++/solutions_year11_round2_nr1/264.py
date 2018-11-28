#include <cstdio>
#define nmax 105
int a[nmax][nmax],nr[nmax],nro[nmax],win[nmax];
char s[nmax * 2];
double wp[nmax],wpo[nmax],wpoo[nmax];
FILE *in, *out;
int main(){
  int T,t,n,i,j;
  in=fopen("rpi.in","r");
  out=fopen("rpi.out","w");
  fscanf(in,"%d",&T);
  for (t=1;t<=T;t++)
  {
    fscanf(in,"%d",&n);
    for (i=1;i<=n;i++)
      nr[i]=nro[i]=wp[i]=wpo[i]=wpoo[i]=win[i]=0;
    for (i=1;i<=n;i++)
    {
      fscanf(in,"%s",s+1);
      for (j=1;j<=n;j++)
      {
        if (s[j]== '.')
        {
          a[i][j] = -1;
          continue;
        }
        a[i][j] = s[j] -'0';
        nr[i]++;
        if (a[i][j])
          win[i]++;
      }
    }
    for (i=1;i<=n;i++)
    {
      wp[i] = ((double)win[i])/nr[i];
    }
    
    for (i=1;i<=n;i++)
    {
      for (j=1;j<=n;j++)
        if (a[i][j]!=-1)
        {
          nro[i]++;
          if (a[i][j])
            wpo[i] += ((double)win[j]) / (nr[j]-1);
          else
            wpo[i] += ((double)win[j] - 1) / (nr[j]-1);
        }
      wpo[i]/= nro[i];
    }
    for (i=1;i<=n;i++)
    {
      for (j=1;j<=n;j++)
        if (a[i][j] != -1)
          wpoo[i]+=wpo[j];
      wpoo[i] /= nro[i];
    }
    fprintf(out,"Case #%d:\n",t);
    for (i=1;i<=n;i++)
      fprintf(out,"%.12lf\n", 0.25 * wp[i] + 0.50 * wpo[i] + 0.25 * wpoo[i]);
  }
  fclose(in);
  fclose(out);
  return 0;
}