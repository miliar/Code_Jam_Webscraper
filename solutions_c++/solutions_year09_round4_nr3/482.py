#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <map>
#include <cmath>
using namespace std;

int n,k;
int A[200][200];
int F[200][200];

int Comp(int x, int y)
  {
  for(int i=0;i<k;++i)
    {
    if (A[x][i]==A[y][i]) return 0;
    if (i>0)
      {
      if ((A[x][i]<A[y][i] && A[x][0]>A[y][0]) || (A[x][i]>A[y][i] && A[x][0]<A[y][0]))
        return 0;
      }
    }
  return 1;
  }

int B[1<<16+10];

int Rec(int t)
  {
  if (t==0) return 0;
  if (B[t]!=-1) return B[t];

  int ret=-1;

  int i=t;
  while(i>0)
    {
    bool flag=true;
    for(int j=0;j<n && flag;++j) if (i&(1<<j))
      for(int l=j+1;l<n;++l) if (i&(1<<l))
        if (F[j][l]==0) {flag=false;break;}

    if (flag)
      {
      int tmp=Rec(t-i)+1;
      if (ret==-1 || tmp<ret) ret=tmp;
      }

    i = (i - 1) & t;
    }

  return B[t]=ret;
  }

int main()
  {
  int T;

  scanf("%d ",&T);
  for(int t=0;t<T;++t)
    {
    scanf("%d %d ",&n,&k);
    for(int i=0;i<n;++i)
      for(int j=0;j<k;++j)
        {
        int t;
        scanf("%d ",&t);
        A[i][j]=t;
        }

    for(int i=0;i<n-1;++i)
      for(int j=i+1;j<n;++j)
        F[i][j]=F[j][i]=Comp(i,j);

    for(int i=0;i<1<<16+10;++i) B[i]=-1;
    int ret=Rec((1<<n)-1);
    printf("Case #%d: %d\n",t+1,ret);
    }

  return 0;
  }