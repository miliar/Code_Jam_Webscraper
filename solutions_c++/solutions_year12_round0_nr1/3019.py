#include<stdio.h>
#include<string.h>
#define max 1000
using namespace std;
int main()
{
    int i,j,len,n;
    char ch[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    char str[max];
    freopen("A-small-attempt1.in","r",stdin);
    freopen("output.txt","w",stdout);
    while(scanf("%d",&n)==1)
    {
        getchar();
        for(i=1;i<=n;i++)
        {
            gets(str);
            len=strlen(str);
            printf("Case #%d: ",i);
            for(j=0;j<len;j++)
            {
                if(str[j]==32)
                {
                    printf("%c",32);
                }
                else if(str[j]>='a'&&str[j]<='z')
                {
                    printf("%c",ch[str[j]-'a']);
                }
            }
            printf("\n");
        }
        fclose(stdout);
        fclose(stdin);
    }
    return 0;
}
