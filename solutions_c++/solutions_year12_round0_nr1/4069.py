#include<iostream>
#include<cstdio>
using namespace std;
char map[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char str[105];
int main()
{
    freopen("A-small-attempt4.in","r",stdin);
    freopen("t.txt","w",stdout);
    int n;
    scanf("%d",&n);
    getchar();
    for(int i=0;i<n;i++)
    {
        gets(str);
        printf("Case #%d: ",i+1);
        for(int j=0;str[j]!='\0';j++)
        {
            if(str[j]!=' ')
                printf("%c",map[str[j]-'a']);
            else printf(" ");
        }
        printf("\n");
    }
    return 0;
}
