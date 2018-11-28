#include <iostream>
#include <stdio.h>
using namespace std;
char m[]="yhesocvxduiglbkrztnwjpfmaq";
int n;
char s[1111];
int main()
{
//freopen("out.txt","w",stdout);
    scanf("%d",&n);
    getchar();
    for(int i=1;i<=n;i++)
    {
        gets(s);
        printf("Case #%d: ",i);
        for(int j=0;s[j];j++) if(s[j]>='a'&& s[j]<='z')putchar(m[s[j]-'a']);
        else putchar(s[j]);
        putchar('\n');
    }

}
