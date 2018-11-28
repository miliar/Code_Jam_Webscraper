#include <stdio.h>
#include <string.h>

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    char trs[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    char s[110];
    int n,i;
    while(scanf("%d",&n)!=EOF)
    {
        getchar();
        int t = 1;
        while(n--)
        {
            gets(s);
            int len = strlen(s);
            for(i=0;i<len;i++)
            {
                if(s[i]>='a'&&s[i]<='z')
                    s[i] = trs[s[i]-'a'];
            }
            printf("Case #%d: %s\n",t++,s);
        }

    }
    return 0;
}
