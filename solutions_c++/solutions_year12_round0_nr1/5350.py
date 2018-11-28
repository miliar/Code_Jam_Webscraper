#include<stdio.h>
#include<string.h>
#include<limits.h>
#include<stdlib.h>
#include<iostream>
#include<deque>
#include<vector>
#include<list>
#include<stack>
#include<algorithm>
#include<math.h>
#include<map>

#define MOD 1000000007
using namespace std;
char pre[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main()
{
  int t,i,j,l;
  char s[111];
  scanf("%d",&t);
  getchar();
  for(i=1;i<=t;i++)
  {
    scanf("%[^\n]",s);
    getchar();
    l=strlen(s);
    for(j=0;j<l;j++)
    {
      if(s[j]==' ') continue;
      else s[j]=pre[s[j]-'a'];
    }
    printf("Case #%d: %s\n",i,s);
  }
  return 0;
}
