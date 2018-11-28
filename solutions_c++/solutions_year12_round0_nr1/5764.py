#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
char ans[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main()
{
    int test,j;
    int i;
    char string[1000];
    scanf("%d%*c",&test);

    for(i=1;i<=test;i++)
    {
        gets(string);

       // printf("Case #%d: ",i);
        cout<<"Case #"<<i<<": ";
        for(j=0;j<strlen(string);j++)
        {
            if(string[j]==' ')
            {
                printf(" ");
            }
            else
            {
                printf("%c",ans[string[j]-'a']);
            }
        }
        cout<<"\n";
    }
    return 0;
}
