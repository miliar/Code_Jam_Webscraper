#pragma warning(disable:4786)
#include<iostream>
#include<map>
#include<string>
using namespace std;
int cn,ci,n,i;
map <string,int> a;
map <string,int>::iterator it;
char s[110];
int qn,j,k,f[1010],d[1010][110],ans,tmp;
string str;

int main()
{
  freopen("a_large.out","w",stdout);
  scanf("%d\n",&cn);
  for (ci=1;ci<=cn;ci++)
  {
    a.clear();
    scanf("%d\n",&n);
    for (i=1;i<=n;i++)
    {
      gets(s);
      str=s;
      a[str]=i;
    }
    scanf("%d\n",&qn);
    for (i=0;i<qn;i++)
    {
      gets(s);
      str=s;
      it=a.find(str);
      if (it==a.end()) f[i]=-1;
      else f[i]=it->second;
    }
    for (i=1;i<=n;i++)
      if (f[0]==i) d[0][i]=-1;
      else d[0][i]=0;
    for (i=1;i<qn;i++)
      for (j=1;j<=n;j++)
        if (f[i]==j) d[i][j]=-1;
        else
        {
          d[i][j]=-1;
          for (k=1;k<=n;k++)
            if (d[i-1][k]!=-1)
            {
              tmp=d[i-1][k];
              if (k!=j) tmp++;
              if (d[i][j]==-1 || tmp<d[i][j]) d[i][j]=tmp;
            }
        }
    ans=-1;
    for (i=1;i<=n;i++)
      if (d[qn-1][i]!=-1 && (ans==-1 || d[qn-1][i]<ans))
        ans=d[qn-1][i];
    printf("Case #%d: %d\n",ci,ans);
  }
  return 0;
}