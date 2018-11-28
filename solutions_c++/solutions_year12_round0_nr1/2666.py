#include<cstdio>
#include<iostream>
#include <cstring>
using namespace std;
const int Maxn=110;
char aa[26]={'y','h','e','s','o','c','v','x','d','u','i',
                'g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

void solve()
{
      int n;
         char x[2];
         scanf("%d",&n);
         gets(x);
         for(int cas=1;cas<=n;++cas)
         {
             char s[Maxn];
             gets(s);
             int i,len=strlen(s);
             char res[Maxn];
             for(i=0;i<len;++i)
             {
                 if(s[i]>='a'&&s[i]<='z')
                 res[i]=aa[s[i]-'a'];
                 else res[i]=' ';
             }
             res[i]='\0';
             printf("Case #%d: ",cas);
             puts(res);
         }
}
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    solve();
    return 0;

}
