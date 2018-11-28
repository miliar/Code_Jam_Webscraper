#include <stdio.h>
#include <string.h>

char str[10005];
int map[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int T,i,j,n,cnt=1;
    char ch;
    scanf("%d",&T);
    ch=getchar();
    while(T--)
    {
        gets(str);
        n=strlen(str);
        for (i=0;i<n;i++)
        {
            if (str[i]==' ') continue;
            str[i]=map[str[i]-'a'];
        }
        printf("Case #%d: %s\n",cnt++,str);
    }
    return 0;
}
