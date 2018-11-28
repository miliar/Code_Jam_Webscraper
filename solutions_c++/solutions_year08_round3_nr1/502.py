#include<stdio.h>
#include<algorithm>
using namespace std;

__int64 a[1005];
__int64 n,p,k,l,r,c,m;
FILE *fp1;
FILE *fp2;

int main()
{
  fp1=fopen("A-large.in","r");
  fp2=fopen("AAA1.txt","w");
  fscanf(fp1,"%I64d",&n);
  for(int q=1;q<=n;q++)
  {
    fscanf(fp1,"%I64d%I64d%I64d",&p,&k,&l);
    for(int i=0;i<l;i++) fscanf(fp1,"%I64d",&a[i]);
    sort(a,a+l);
    r=c=m=0;
    for(int i=l-1;i>=0;i--)
      if(m<k)
      {
        r+=a[i]*(c+1);
        m++;
        if(m==k)
        {
          c++;
          m=0;        
        }        
      }
    fprintf(fp2,"Case #%d: %I64d\n",q,r);        
  }
  fclose(fp1);
  fclose(fp2);
  return 0;
}
