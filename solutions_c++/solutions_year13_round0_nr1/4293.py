#include <iostream>
#include <cstdio>
using namespace std;
string s[4];
char check(string s)
{
    int x,o,t;
    x=0;
    o=0;
    t=0;
    for (int i=0; i<4; i++)
    {
        if (s[i]=='X') x++;
        if (s[i]=='O') o++;
        if (s[i]=='T') t++;
    }
    if (x+t==4) return 'x';
    if (o+t==4) return 'o';
    return 't';
}
string ans()
{
    int i,j;
    for (i=0; i<4; i++)
    {
        char p;
        p=check(s[i]);
        if (p=='x') return "X won\n";
        if (p=='o') return "O won\n";
    }

    for (j=0; j<4; j++)
    {
        string temp="";
        for (i=0; i<4; i++)
            temp+=s[i][j];
        char p;
        p=check(temp);
        if (p=='x') return "X won\n";
        if (p=='o') return "O won\n";
    }
    string temp="";
    for (i=0; i<4; i++)
        temp+=s[i][i];
    char p;
    p=check(temp);
    if (p=='x') return "X won\n";
    if (p=='o') return "O won\n";
    temp="";
    for (i=0; i<4; i++)
        temp+=s[i][3-i];
    p;
    p=check(temp);
    if (p=='x') return "X won\n";
    if (p=='o') return "O won\n";
    for (i=0; i<4; i++)
        for (j=0; j<4; j++)
            if (s[i][j]=='.') return "Game has not completed\n";
    return "Draw\n";

}
int main()
{
    freopen("/home/garfield/下载/A-large.in","r",stdin);
    freopen("/home/garfield/下载/ans2.txt","w",stdout);
    int tt;
    cin>>tt;
    for (int pp=1; pp<=tt; pp++)
    {
        printf("Case #%d: ",pp);
        int i;
        for (i=0; i<4; i++)
            cin>>s[i];
        cout<<ans()<<endl;
    }
}
