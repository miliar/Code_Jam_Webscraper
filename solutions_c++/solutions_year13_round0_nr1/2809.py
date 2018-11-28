#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char s[5][6];

int judge()
{
    int i,j,o,x,t;
    for(i=0;i<4;i++)
    {
        o = x = t = 0;
        for(j=0;j<4;j++)
        if(s[i][j]=='O')
        o++;
        else if(s[i][j]=='T')
        t++;
        else if(s[i][j]=='X')
        x++;
        if(t<=1 && (x+t==4 || o+t==4))
        return x>o?1:2;
    }
    for(i=0;i<4;i++)
    {
        o = x = t = 0;
        for(j=0;j<4;j++)
        if(s[j][i]=='O')
        o++;
        else if(s[j][i]=='T')
        t++;
        else if(s[j][i]=='X')
        x++;
        if(t<=1 && (x+t==4 || o+t==4))
        return x>o?1:2;
    }
    o = x = t = 0;
    for(j=0;j<4;j++)
    if(s[j][j]=='O')
    o++;
    else if(s[j][j]=='T')
    t++;
    else if(s[j][j]=='X')
    x++;
//    cout << x << " " << o << " " << t << endl;
    if(t<=1 && (x+t==4 || o+t==4))
    return x>o?1:2;
    o = x = t = 0;
    for(j=0;j<4;j++)
    if(s[3-j][j]=='O')
    o++;
    else if(s[3-j][j]=='T')
    t++;
    else if(s[3-j][j]=='X')
    x++;
//    cout << x << " " << o << " " << t << endl;
    if(t<=1 && (x+t==4 || o+t==4))
    return x>o?1:2;
    return 0;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int pos,t,cas = 1,i,j;
    scanf("%d",&t);
    while(t--)
    {
        pos = 0;
        scanf("%s%s%s%s",s[0],s[1],s[2],s[3]);
        for(i=0;i<4;i++)
        for(j=0;j<4;j++)
        if(s[i][j]=='.')
        pos++;
        printf("Case #%d: ",cas++);
        int ans = judge();
        if(!ans)
        {
            if(pos == 0)
            cout << "Draw" << endl;
            else
            cout << "Game has not completed" << endl;
        }
        else
        printf("%c won\n",ans==1?'X':'O');
    }
    return 0;
}
