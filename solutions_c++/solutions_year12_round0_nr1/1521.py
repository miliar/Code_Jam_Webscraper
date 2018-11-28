#include <stdio.h>
#include <string.h>
char ts[4][110]={"a zoo","our language is impossible to understand","there are twenty six factorial possibilities",
"so it is okay if you want to just give up"};
char s[110];
int tp[110]={24,7,4,18,14,2,21,23,3,20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,16};
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int T;
    scanf("%d",&T);
    gets(s);
    for (int ii=1;ii<=T;ii++)
    {
        gets(s);
        int len=strlen(s);
        printf("Case #%d: ",ii);
        for (int i=0;i<len;i++)
            if (s[i]!=' ') printf("%c",'a'+tp[s[i]-'a']);
            else printf(" ");
        printf("\n");
    }
    return 0;
}
