#include <cstdio>
#include <cstring>
#define N 2048
#define eps (1e-7)
#define CNT 1e7
#define K(a,b) ((y[b]-y[a])/(b-a))
int n,b[N];
double y[N];

double check(int a,int b) {
  //printf("chk(%d,%d)\n",a,b);
  int c; double Kac,Bac;
  for (c=a+1;c<b;c++)
    if ((Kac=K(a,c))>=K(a,b)) {
      Bac=y[a]-Kac*a;
      y[c]=Kac*c+Bac;
      //y[b]=Kac*b+Bac+1;
      y[b]+=1;
      //printf("y[%d]=%.2lf\n",b,y[b]);
      return y[b];
    }
  for (c=b+1;c<=n;c++)
    if ((Kac=K(a,c))>K(a,b)) {
      Bac=y[a]-Kac*a;
      y[c]=Kac*c+Bac;
      //y[b]=Kac*b+Bac+1;
      y[b]+=1;
      //printf("y[%d]=%.2lf\n",b,y[b]);
      return y[b];
    }
  return -1;
}

int goon() {
  int i;
  //for (i=1;i<=n;i++)
  //  printf("%.2lf ",y[i]);
  //  putchar(10);
  for (i=1;i<n;i++)
    if (check(i,b[i])>0)
      return 1;
  return 0;
}

int main() {
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int T,t,i,j,cnt;
  scanf("%d",&T);
  for (t=1;t<=T;t++) {
    memset(y,cnt=0,sizeof(y));
    scanf("%d",&n);
    for (i=1;i<n;i++)
      scanf("%d",b+i);
    while (cnt<CNT&&goon()) cnt++;
    printf("Case #%d: ",t);
    if (cnt<CNT) {
      for (i=1;i<=n;i++)
        printf("%.0lf ",y[i]);
        putchar(10);
    } else printf("Impossible\n");
  }
  return 0;
}
