#include<stdio.h>
#include<string>
#include<string.h>
#include<iostream>
using namespace std;
int main (void)
{
    int n;
    int i,j,k;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    char map[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    char inp[1000];
    int tcase,act;
    cin>>tcase;
    gets(inp);
    for(act=0;act<tcase;act++)
    {
        gets(inp);
        for(i=0;i<strlen(inp);i++)
            if(inp[i]>='a' and inp[i]<='z')
                inp[i]=map[inp[i]-'a'];
        printf("Case #%d: %s\n",act+1,inp);
    }
    return 0;
}
