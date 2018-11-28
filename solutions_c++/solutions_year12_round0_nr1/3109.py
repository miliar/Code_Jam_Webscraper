#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <memory>
using namespace std;
int p[26]={24,7,4,18,14,2,21,23,3,20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,16},n;
char s[222222],ss[222222];
int main()
{
    freopen("speak.in","r",stdin);
    freopen("speak.out","w",stdout);
    scanf("%d\n",&n);
    int sss=0;
    while(n--)
    {
    gets(s);
    memset(ss,0,sizeof(ss));
    for(int i=0;i<strlen(s);i++)
        if(s[i]==' ')ss[i]=' ';
        else ss[i]=p[s[i]-'a']+'a';
        cout<<"Case #"<<++sss<<": ";
    puts(ss);
    }
}
