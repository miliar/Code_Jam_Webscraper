#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 

using namespace std;

char s[1000];
char mp[26]={'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};

int main()
{
  int i,j,l,t,len;
  scanf("%d",&t);
  gets(s);
  for (l=0;l<t;l++)
  {
    gets(s);
    len=strlen(s);
    for (i=0;i<len;i++)
      if (s[i]!=' ')
        for (j=0;j<26;j++)
          if (mp[j]==s[i])
          {
            s[i]='a'+j;
            break;
          }
    printf("Case #%d: %s\n",l+1,s);
  }
}
