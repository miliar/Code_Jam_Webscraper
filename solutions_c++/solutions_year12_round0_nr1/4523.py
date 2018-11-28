#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
char tt[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main()
{
      freopen("a.in","r",stdin);
      freopen("a.out","w",stdout);
      int T;
      char s[105];
      scanf("%d\n",&T);
      for(int cas=1;cas<=T;cas++)
      {
			 		  printf("Case #%d: ",cas);
					  gets(s);
						for(int i=0;s[i]!='\0';i++)
						if(s[i]==' ')printf(" ");
						else printf("%c",tt[s[i]-'a']);
						puts("");		
							 
      }


      return 0;
}
