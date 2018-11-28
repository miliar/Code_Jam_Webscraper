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
char s[100];
int main()
{
  int n;
  freopen(taskname"in","r",stdin);
  freopen(taskname"out","w",stdout);
  scanf("%d ",&n);
  for(int i=0;i<n;i++)
  {
	  memset(s,0,sizeof(s));
    s[0]='0';
    //cerr<<n;
    scanf(" %s ",s+1);
    //puts(s);
    next_permutation(s,s+strlen(s));
    printf("Case #%d: ",i+1); 
    if(s[0]=='0')
      puts(s+1);
    else
      puts(s);
  }
  return 0;
}