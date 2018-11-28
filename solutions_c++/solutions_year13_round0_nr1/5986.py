#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

char s[11][11];

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int ca,t=0;
    for(scanf("%d",&ca);ca--;)
    {
        printf("Case #%d: ",++t);
        for(int i=0;i<4;i++)
            scanf("%s",s[i]);
        bool ret=0;
        for(int i=0;i<4;i++)
        {
            bool f=1;
            if(s[i][0]=='.') continue;
            int id=0;
            if(s[i][0]=='T') id=1;
            for(int j=id;j<4;j++)
                if(s[i][j]!=s[i][0] && s[i][j]!='T') f=0;
            int cnt=0;
            for(int j=0;j<4;j++)
                cnt+=s[i][j]=='T';
            if(cnt>1) f=0;
            if(f==0) continue;
            ret=1;
            if(s[i][0]=='O')
            {
                printf("O won\n");
                break;
            }
            if(s[i][0]=='X')
            {
                puts("X won");
                break;
            }
            if(s[i][1]=='O')
            {
                printf("O won\n");
                break;
            }
            if(s[i][1]=='X')
            {
                puts("X won");
                break;
            }
        }
        if(ret) continue;
        for(int i=0;i<4;i++)
        {
            bool f=1;
            if(s[0][i]=='.') continue;
            int id=0;
            if(s[0][i]=='T') id=1;
            for(int j=id;j<4;j++)
                if(s[j][i]!=s[0][i] && s[j][i]!='T') f=0;
            int cnt=0;
            for(int j=0;j<4;j++)
                cnt+=s[j][i]=='T';
            if(cnt>1) f=0;
            if(f==0) continue;
            ret=1;
            if(s[0][i]=='O')
            {
                printf("O won\n");
                break;
            }
            if(s[0][i]=='X')
            {
                puts("X won");
                break;
            }
            if(s[1][i]=='O')
            {
                printf("O won\n");
                break;
            }
            if(s[1][i]=='X')
            {
                puts("X won");
                break;
            }
        }
        if(ret) continue;
        int id=0,f=1,cnt=0;
        if(s[0][0]=='T') id=1;
        for(int i=0;i<4;i++)
            if(s[i][i]!=s[0][0] && s[i][i]!='T') f=0;
        for(int i=0;i<4;i++)
            if(s[i][i]=='T') cnt++;
        if(cnt>1) f=0;
        if(f)
        {
            if(s[id][id]=='O')
            {
                puts("O won");
                continue;
            }
            if(s[id][id]=='X')
            {
                puts("X won");
                continue;
            }
        }
        f=1;
        cnt=0;
        id=0;
        if(s[0][3]=='T') id=1;
        for(int i=0;i<4;i++)
            if(s[i][3-i]!=s[0][3] && s[i][3-i]!='T') f=0;
        for(int i=0;i<4;i++)
            if(s[i][3-i]=='T') cnt++;
        if(cnt>1) f=0;
        if(f)
        {
            if(s[id][3-id]=='O')
            {
                puts("O won");
                continue;
            }
            if(s[id][3-id]=='X')
            {
                puts("X won");
                continue;
            }
        }
        cnt=0;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cnt+=s[i][j]=='.';
        if(cnt) printf("Game has not completed\n");
        else puts("Draw");
    }
    return 0;
}
