#include<algorithm>
#include<cstdio>
#include<iostream>
#include<string>
#include<vector>
#include<string.h>
#include<set>
#include<map>
#define taskname ""
#define sqr(a) (a)*(a)
#define forn(i,n) for(int i=0;i<(int)n;i++)
using namespace std;
char s[1000];
int check(char *a)
{
  int mx=0,n=strlen(a);
  for(int i=1;i<n;i++)
    if(a[i]=='1')
      mx=i;
  return mx;
}
int x[1000];
int main()
{
  int n,t;
  freopen(taskname"in","r",stdin);
  freopen(taskname"out","w",stdout);
  scanf("%d ",&t);
  forn(i,t)
  {
    int ans=0;
    scanf("%d ",&n);
    forn(j,n)
    {
      gets(s);
      x[j]=check(s);
    }
    forn(j,n)
    {
      if(x[j]>j)
      { 
        int mi=0;
        for(int k=j;k<n;k++)
          if(x[k]<=j)
          {
            mi=k;
            break;
          }
        for(int k=mi;k>j;k--)
        {  
          swap(x[k],x[k-1]);
          ans++;
        }
      }  
    }
    printf("Case #%d: %d\n",i+1,ans);
  }
  return 0;
}