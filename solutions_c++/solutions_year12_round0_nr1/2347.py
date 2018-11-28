#include <cstdio>
#include <cstring>

#define REP(i,n) for(__typeof(n) i=0;i!=(n);++i)

char translation[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

char str[147],res[147];

int main()
{
        int N;
        scanf("%d\n",&N);
        REP(i,N)
        {
                gets(str);
                int size=strlen(str);
                REP(j,size)
                {
                        if (str[j]==' ') res[j]=' ';
                        else res[j]=translation[str[j]-'a'];
                }
                res[size]='\0';
                printf("Case #%d: %s\n",i+1,res);
        }
        return 0;
}
