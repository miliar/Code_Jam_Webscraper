#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
char trans[27]="yhesocvxduiglbkrztnwjpfmaq";
char s[101];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    gets(s);
    for (int cas=1; cas<=t; cas++)
    {
        printf("Case #%d: ",cas);
        gets(s);
        int n=strlen(s);
        for (int i=0; i<n; i++)
            if (s[i]>='a' && s[i]<='z')
                putchar(trans[s[i]-'a']);
            else
                putchar(s[i]);
        puts("");
    }
    return 0;
}
