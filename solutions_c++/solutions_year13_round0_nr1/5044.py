#include <iostream>
#include <cstdio>

using namespace std;

#define cont continue
char c[10][10];

void f_read()
{

    int i;
    for (i=0;i<4;++i)
        cin>>c[i];
}

bool f(char s1,char s2)
{
    if (s1==s2 || s1=='T') return true;
    else return false;
}

bool win(char s)
{
    int i;
    for (i=0;i<4;++i)
        if  (f(c[0][i],s) && f(c[1][i],s) && f(c[2][i],s) && f(c[3][i],s)) return true;
    for (i=0;i<4;++i)
        if  (f(c[i][0],s) && f(c[i][1],s) && f(c[i][2],s) && f(c[i][3],s)) return true;

    if (f(c[0][0],s) && f(c[1][1],s) && f(c[2][2],s) && f(c[3][3],s)) return true;
    if (f(c[0][3],s) && f(c[1][2],s) && f(c[2][1],s) && f(c[3][0],s)) return true;
    return false;
}

bool P()
{
    for (int i=0;i<4;++i)
        for (int j=0;j<4;++j)
            if (c[i][j]=='.') return true;
    return false;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for (int i=0;i<t;++i)
    {
        f_read();
        printf("Case #%d: ",i+1);
        if (win('X')) {cout<<"X won"<<endl;cont;}
        if (win('O')) {cout<<"O won"<<endl;cont;}
        if (P()) {cout<<"Game has not completed"<<endl;cont;}
        cout<<"Draw"<<endl;
    }
}
