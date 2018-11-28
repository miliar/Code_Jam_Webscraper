#include<iostream>
using namespace std;
__int64 ans,tmp;
__int64 n,A,B,C,D,x,y,M;
__int64 cnt[5][5];
__int64 x1,x2,x3,y1,y2,y3,cn,ci;

int main()
{
  freopen("a_large.out","w",stdout);
  scanf("%I64d",&cn);
  ci=0;
  while (cn--)
  {
    ci++;
    scanf("%I64d %I64d %I64d %I64d %I64d %I64d %I64d %I64d",&n,&A,&B,&C,&D,&x,&y,&M);
    memset(cnt,0,sizeof(cnt));
    cnt[x%3][y%3]++;
    while (--n)
    {
      x=(A*x+B)%M;
      y=(C*y+D)%M;
      cnt[x%3][y%3]++;
    }
    ans=0;
    for (x1=0;x1<3;x1++)
    for (y1=0;y1<3;y1++)
    for (x2=0;x2<3;x2++)
    for (y2=0;y2<3;y2++)
    for (x3=0;x3<3;x3++)
    for (y3=0;y3<3;y3++)
      if ((x1+x2+x3)%3==0 && (y1+y2+y3)%3==0) 
      {
        tmp=cnt[x1][y1];
        if (x2==x1 && y2==y1)
        {
          tmp*=cnt[x2][y2]-1;
          if (x3==x1 && y3==y1) tmp*=cnt[x3][y3]-2;
          else tmp*=cnt[x3][y3];
        }
        else
        {
          tmp*=cnt[x2][y2];
          if (x3==x1 && y3==y1
            || x3==x2 && y3==y2) tmp*=cnt[x3][y3]-1;
          else tmp*=cnt[x3][y3];
        }
        ans+=tmp;
      }
    ans/=6;
    printf("Case #%I64d: %I64d\n",ci,ans);
    //if (ans%6!=0) printf("n\n");
  }
  return 0;
}