#include <cstdio>

const char code[] = "yhesocvxduiglbkrztnwjpfmaq";

int main()
{
    int t,ncase = 0;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    char from[200],to[200];
    scanf("%d",&t);
    getchar();
    while(t--){
        gets(from);
        int i;
        for(i = 0; from[i]; i++)
            if(from[i] != ' ')
                to[i] = code[from[i]-'a'];
            else
                to[i] = from[i];
        to[i] = 0;
        printf("Case #%d: %s\n",++ncase,to);
    }
    return 0;
}
