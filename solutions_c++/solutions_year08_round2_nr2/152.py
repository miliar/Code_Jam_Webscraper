#include<iostream>
using namespace std;
int f[2000];
int cn,ci,A,B,i,j,x,y,z,k,flag,p,ans;

int fa(int x)
{
  if (f[x]<0) return x;
  f[x]=fa(f[x]);
  return f[x];
}

int gcd(int x,int y)
{
  if (y==0) return x;
  return gcd(y,x%y);
}

int main()
{
  freopen("B_small.out","w",stdout);
  scanf("%d",&cn);
  ci=0;
  while (cn--)
  {
    ci++;
    scanf("%d %d",&A,&B);
    for (i=A;i<=B;i++) f[i]=-1;
    scanf("%d",&p);
    for (i=A;i<=B;i++)
      for (j=A+1;j<=B;j++)
      {
        x=fa(i);
        y=fa(j);
        if (x!=y)
        {
          z=gcd(i,j);
          flag=0;
          for (k=2;k*k<=z;k++)
            if (z%k==0)
            {
              if (k>=p)
              {
                flag=1;
                break;
              }
              while (z%k==0) z/=k;
            }
          if (!flag)
          {
            if (z!=1 && z>=p) flag=1;
          }
          if (flag) 
          {
            f[x]=y;
          }
        }
      }
    ans=0;
    for (i=A;i<=B;i++)
      if (f[i]<0) ans++;
    printf("Case #%d: %d\n",ci,ans);
  }
  return 0;
}