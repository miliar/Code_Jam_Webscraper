#include<stdio.h>
#include<algorithm>
using namespace std;
#define MAXN 1000
__int64 a[MAXN];
__int64 b[MAXN];
int T,n;
__int64 r;
FILE *fp1;
FILE *fp2;

int main()
{
  fp1=fopen("A-large.in","r");
  fp2=fopen("AAA2.txt","w");
  fscanf(fp1,"%d",&T);
  for(int k=0;k<T;k++)
  {
    fscanf(fp1,"%d",&n);
    for(int i=0;i<n;i++) fscanf(fp1,"%I64d",&a[i]);     
    for(int i=0;i<n;i++) fscanf(fp1,"%I64d",&b[i]);
    sort(a,a+n);
    sort(b,b+n);
    r=0;
    for(int i=0;i<n;i++) r+=a[i]*b[n-1-i];
    fprintf(fp2,"Case #%d: %I64d\n",k+1,r);
  }
  fclose(fp1);
  fclose(fp2);
  return 0;
}
