#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std; 
int mp[26]={121,104,101,115,111,99,118,120,100,117,105,103,108,98,107,114,122,116,110,119,106,112,102,109,97,113};
char s[3000];
int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("A.txt","w",stdout);
    int cs,i,j,k,n,m=0;
    scanf("%d",&cs);
    getchar();
    while (cs--)
    {
       gets(s);
       printf("Case #%d: ",++m);
       for (int i=0;s[i];i++)
       {
           if (s[i]<='z'&&s[i]>='a')
       printf("%c",mp[s[i]-'a']);
       else printf("%c",s[i]);
       }
       puts("");
    }
}

