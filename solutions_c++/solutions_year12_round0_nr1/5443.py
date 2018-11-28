#include <iostream>
#include <cstdio>

using namespace std;

char mymap[27] = "yhesocvxduiglbkrztnwjpfmaq";

int main()
{
//    freopen("in.txt","r",stdin);
//    freopen("out.txt","w",stdout);
    int cases,c = 0;
    scanf("%d",&cases);
    getchar();
    while(cases--)
    {
        printf("Case #%d: ",++c);
        char ch;
        while((ch = getchar()) && ch != '\n')
        {
            char tran;
            if(ch == ' ')   tran = ' ';
            else            tran = mymap[ch-'a'];
            putchar(tran);
        }
        puts("");
    }
    return 0;
}
