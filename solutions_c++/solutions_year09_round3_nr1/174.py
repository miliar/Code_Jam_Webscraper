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
int x[60],k;
int f(char a)
{
  if(a<='9')
    return a-'0';
  return a-'a'+10;
}
char s[100];
int main()
{
  int t;
  freopen(taskname"in","r",stdin);
  freopen(taskname"out","w",stdout);
  scanf("%d ",&t);
  forn(q,t)
  {
	memset(s,0,sizeof(s));
    gets(s);
	k=2;
    int n=strlen(s);
    memset(x,-1,sizeof(x));
    x[f(s[0])]=1;
    int j=0;
    while(j<n&&s[j]==s[0])
      j++;
    if(j!=n)
		x[f(s[j])]=0;
    for(int i=j+1;i<n;i++)
      if(x[f(s[i])]==-1)
        x[f(s[i])]=k,k++;
    long long ans=0,p=1;
    for(int i=n-1;i>=0;i--)
    {
      ans+=p*x[f(s[i])];
      p*=k;
    }
    printf("Case #%d: %I64d\n",q+1,ans);
	//cerr<<s<<endl;
  }
  return 0;
}