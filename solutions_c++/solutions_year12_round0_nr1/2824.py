#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
char map[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main()
{
   freopen("in.txt","r",stdin);
   freopen("out.txt","w",stdout);
   int n,cas;
   char str[105];
   scanf("%d",&n);
   getchar();
   for(cas = 1;cas <= n;++cas) {
    gets(str);
    for(int i = 0;str[i] != '\0';++i) {
      if(str[i] != ' ')
        str[i] = map[str[i] - 'a'];
    }
    printf("Case #%d: %s\n",cas,str);
   }
}
