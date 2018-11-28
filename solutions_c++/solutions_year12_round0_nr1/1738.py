#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

char dict[300];
char s[200];
char sol[200];
int tests;
int len;
int main()
{
    strcpy(s,"ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y e q z");
    strcpy(sol,"our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a o z q");    len = strlen(s);
    for(int i = 0; i < len; i++)
        dict[s[i]] = sol[i];
    freopen("input.txt","r",stdin);    
    freopen("output.txt","w",stdout);    
    scanf("%d\n",&tests);
    for(int t = 0; t < tests; t++)
    {
		strcpy(s,"");
        scanf("%[^\n]\n",s);
        len = strlen(s);
        for(int i = 0; i < len; i++)
            s[i] = dict[s[i]];
        printf("Case #%d: %s\n", (t+1), s);
    }
    return(0);
}

