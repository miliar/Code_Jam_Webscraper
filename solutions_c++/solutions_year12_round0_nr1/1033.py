#include <iostream>
#include <string.h>
#include <cstring>
#include <stdio.h>
using namespace std;

char chs[26]={'y','h','e','s','o','c','v','x','d','u','i',
                'g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int n=0;
    char s[110];
    char out[110];
    cin>>n;
    getchar();
    for(int i=1;i<=n;i++)
    {
        gets(s);
        int index=-1;
        //printf("%s\n",s);
        while(s[++index])
        {
            if(s[index]==' ')
            {
                out[index]=' ';
            }
            else out[index]=chs[s[index]-'a'];
        }
        out[index]='\0';
        printf("Case #%d: %s\n",i,out);
    }
    return 0;
}
