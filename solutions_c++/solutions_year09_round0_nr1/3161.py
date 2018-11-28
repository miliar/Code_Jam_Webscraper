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
char s[100],a[5000][5000];
int n;
bool check(char *a,char *s)
{
    int p=0,f=true;
    for(int q=0;q<n;q++)
    {
	  int fl=0;
	  if(s[p]=='(')
        fl=1,p++;
      while(s[p]!=a[q])
      {
		if(!fl||s[p]==')'||s[p]==0)
          return 0;
	    p++;
      }
	  p++;
	  while(fl)
		fl=s[p++]!=')';
	}
	return 1;
}
int main()
{
  int m,k;
  freopen(taskname"in","r",stdin);
  freopen(taskname"out","w",stdout);
  scanf("%d %d %d\n",&n,&m,&k);
  for(int i=0;i<m;i++)
    gets(a[i]);
  for(int i=0;i<k;i++)
  {
    int ans=0;
    gets(s);
    for(int j=0;j<m;j++)
    {
      if(check(a[j],s)) 
        ans++; 
    }
    printf("Case #%d: %d\n",i+1,ans);
  }
  return 0;
}