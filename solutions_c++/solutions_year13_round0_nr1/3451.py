#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
char map[10][10];
int main()
{
//    freopen("input.in","r",stdin);
//    freopen("output.out","w",stdout);
    int t,Case=0;
    scanf("%d",&t);
    while(t--)
    {
        for(int i=0;i<4;++i)
            scanf("%s",map[i]);
        int flag=0;
        for(int i=0;i<4;++i)
            for(int j=0;j<4;++j)
            if(map[i][j]=='.')flag=1;
        int wx=0,wo=0;
        for(int i=0;i<4;++i)
        {
            int xx=0,oo=0,tt=0;
            for(int j=0;j<4;++j)
                if(map[i][j]=='X')++xx;
                else if(map[i][j]=='O')++oo;
                else if(map[i][j]=='T')++tt;
            if(xx==4||(xx==3&&tt==1))wx=1;
            if(oo==4||(oo==3&&tt==1))wo=1;
        }
        for(int i=0;i<4;++i)
        {
            int xx=0,oo=0,tt=0;
            for(int j=0;j<4;++j)
                if(map[j][i]=='X')++xx;
                else if(map[j][i]=='O')++oo;
                else if(map[j][i]=='T')++tt;
            if(xx==4||(xx==3&&tt==1))wx=1;
            if(oo==4||(oo==3&&tt==1))wo=1;
        }
        int xx=0,oo=0,tt=0;
        for(int i=0;i<4;++i)
            if(map[i][i]=='X')++xx;
            else if(map[i][i]=='O')++oo;
            else if(map[i][i]=='T')++tt;
        if(xx==4||(xx==3&&tt==1))wx=1;
        if(oo==4||(oo==3&&tt==1))wo=1;
        xx=0,oo=0,tt=0;
        for(int i=0;i<4;++i)
            if(map[i][3-i]=='X')++xx;
            else if(map[i][3-i]=='O')++oo;
            else if(map[i][3-i]=='T')++tt;
        if(xx==4||(xx==3&&tt==1))wx=1;
        if(oo==4||(oo==3&&tt==1))wo=1;
        printf("Case #%d: ",++Case);
        if(wx==1&&wo==0)printf("X won\n");
        else if(wx==0&&wo==1)printf("O won\n");
        else if(flag)printf("Game has not completed\n");
        else printf("Draw\n");
    }
    return 0;
}
