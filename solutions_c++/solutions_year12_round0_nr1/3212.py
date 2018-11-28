#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

char mp[30]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char s[300];

int main()
{
  //  freopen("in.in","r",stdin);
  //  freopen("out.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        while(1)
        {
            gets(s);
            if(strlen(s)>0) break;
        }
        int l=strlen(s);
        printf("Case #%d: ",cas);
        for(int i=0;i<l;i++)
            if(s[i]==' ') printf(" ");
            else printf("%c",mp[s[i]-'a']);
        printf("\n");
    }
}
