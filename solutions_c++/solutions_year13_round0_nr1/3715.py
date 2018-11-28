#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
using namespace std;
int d[2][4][2] = {{{0,0},{1,1},{2,2},{3,3}},
                  {{3,0},{2,1},{1,2},{0,3}}};
int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    int T;
    scanf("%d",&T);
    char mp[5][5];
    char s[10];
    int cas = 1;
    while(T--)
    {
        printf("Case #%d: ",cas++);
        int cnt = 0;
        for(int i=0;i<4;i++)
        {
            cin >> s;
            //cout << s<<endl;
            for(int j=0;j<4;j++)
            {
                mp[i][j] = s[j];
                if(mp[i][j] == 'X' || mp[i][j] == 'O' || mp[i][j] == 'T')cnt++;
            }
        }
        int found = 0;
        for(int i=0;i<4;i++)
        {
            int cntt=0,cnto=0,cntx=0;
            for(int j=0;j<4;j++)
            {
                if(mp[i][j] == 'X')cntx++;
                else if(mp[i][j] == 'O')cnto++;
                else if(mp[i][j] == 'T')cntt++;
            }
            if(cnto == 4 || (cnto ==3 && cntt == 1)){printf("O won\n");found = 1;break;}
            else if(cntx == 4 || (cntx ==3 && cntt == 1)){printf("X won\n");found = 1;break;}
        }
        if(found)continue;
         for(int i=0;i<4;i++)
        {
            int cntt=0,cnto=0,cntx=0;
            for(int j=0;j<4;j++)
            {
                if(mp[j][i] == 'X')cntx++;
                else if(mp[j][i] == 'O')cnto++;
                else if(mp[j][i] == 'T')cntt++;
            }
            if(cnto == 4 || (cnto ==3 && cntt == 1)){printf("O won\n");found = 1;break;}
            else if(cntx == 4 || (cntx ==3 && cntt == 1)){printf("X won\n");found = 1;break;}
        }
        if(found)continue;
        for(int i=0;i<2;i++)
        {
            int cntt=0,cnto=0,cntx=0;
            for(int j=0;j<4;j++)
            {
                if(mp[d[i][j][0]][d[i][j][1]] == 'X')cntx++;
                else if(mp[d[i][j][0]][d[i][j][1]] == 'O')cnto++;
                else if(mp[d[i][j][0]][d[i][j][1]] == 'T')cntt++;
            }
            if(cnto == 4 || (cnto ==3 && cntt == 1)){printf("O won\n");found = 1;break;}
            else if(cntx == 4 || (cntx ==3 && cntt == 1)){printf("X won\n");found = 1;break;}
        }

        if(!found)
        {
            if(cnt == 16)printf("Draw\n");
            else printf("Game has not completed\n");
        }

    }
    return 0;
}
