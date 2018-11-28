#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

char list[]="yhesocvxduiglbkrztnwjpfmaq";
char s[256];
char o[256];
int tn;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d\n",&tn);
    for (int w=1;w<=tn;w++)
    {
        gets(s);
        memset(o,0,sizeof(o));
        for (int i=0;i<(int)strlen(s);i++)
        {
            if (s[i]==' ') o[i]=' ';
            else o[i]=list[s[i]-97];
        }
        printf("Case #%d: ",w);
        puts(o);
    }
    return 0;
}
