#include<iostream>
using namespace std;
int ci,ans,cn,n,i,j,tmp,len,k;
int a[10];
char s[10000],t[10000];

int main()
{
  freopen("d_small.out","w",stdout);
  scanf("%d",&cn);
  while (cn--)
  {
    ci++;
    scanf("%d %s",&n,&s);
    len=strlen(s);
    for (i=0;i<n;i++) a[i]=i;
    ans=1000000;
    while (1)
    {
      memset(t,0,sizeof(t));
      for (i=0;i<len;i++)
      {
        j=i/n*n;
        t[i]=s[a[i%n]+j];
      }
      tmp=0;
      for (i=1;i<len;i++)
        if (t[i]!=t[i-1]) tmp++;
      if (tmp<ans) ans=tmp;
      i=n-2;
      while (i>=0 && a[i]>a[i+1]) i--;
      if (i<0) break;
      k=i+1;
      for (j=k+1;j<n;j++)
        if (a[j]>a[i] && a[j]<a[k]) k=j;
      tmp=a[i];
      a[i]=a[k];
      a[k]=tmp;
      for (i++;i<n;i++)
        for (j=i+1;j<n;j++)
          if (a[i]>a[j])
          {
            tmp=a[i];
            a[i]=a[j];
            a[j]=tmp;
          }
    }
    printf("Case #%d: %d\n",ci,ans+1);
  }
  return 0;
}