#include<cstdio>
#include<cstring>
using namespace std;
//         abcdefghijklmnopqrstuvwxyz 
char ch[]="yhesocvxduiglbkrztnwjpfmaq";
char s[200];
int main()
{
    int n;
    //freopen("A-small-attempt2.in","r",stdin);
    //freopen("A-small-attempt2.out","w",stdout);
    scanf("%d\n",&n);
    for(int i=1;i<=n;++i)
    {
            gets(s);
            for(int j=0;j<strlen(s);++j)
               if(s[j]!=' ')
                  s[j]=ch[s[j]-'a'];
            printf("Case #%d: %s\n",i,s);
    }
    return 0;
}
               
