#include<iostream>
#include<algorithm>
using namespace std;
struct node
{
  int st,ed,tag;
} a[210];
int cn,ci,tt,na,nb,hh,mm,i,j,n,k;
int f[210];
int ans[2];

bool cmp(const node &a,const node &b)
{
  if (a.st==b.st) return a.ed<b.ed;
  else return a.st<b.st;
}

int main()
{
  freopen("b_small.out","w",stdout);
  scanf("%d",&cn);
  for (ci=1;ci<=cn;ci++)
  {
    scanf("%d%d%d",&tt,&na,&nb);
    for (i=0;i<na+nb;i++)
    {
      scanf("%d:%d",&hh,&mm);
      a[i].st=hh*60+mm;
      scanf("%d:%d",&hh,&mm);
      a[i].ed=hh*60+mm;
      if (i<na) a[i].tag=0;
      else a[i].tag=1;
    }
    n=na+nb;
    memset(f,0,sizeof(f));
    sort(a,a+n,cmp);
    ans[0]=0;
    ans[1]=0;
    for (i=0;i<n;i++)
    {
      if (!f[i]) ans[a[i].tag]++;
      k=-1;
      for (j=i+1;j<n;j++)
        if (!f[j] && a[j].st>=a[i].ed+tt && a[j].tag!=a[i].tag)
        {
          if (k==-1 || a[j].ed<a[k].ed) k=j;
        }
      if (k!=-1) f[k]=1;
    }
    printf("Case #%d: %d %d\n",ci,ans[0],ans[1]);
  }
  return 0;
}