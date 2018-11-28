#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

char board[10][10];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1; cas<=T; cas++)
    {
        bool flag=false;
        bool xf=false,of=false;
        for(int i=0; i<4; i++)
        {
            scanf("%s",board[i]);
            for(int j=0; j<4; j++)
            {
                if(board[i][j]=='.')
                {
                    flag=true;
                }
            }
        }
        int c[15];
        for(int i=0; i<4; i++)
        {
            memset(c,0,sizeof(c));
            for(int j=0; j<4; j++)
            {
                switch(board[i][j])
                {
                case 'X':c[0]++; break;
                case 'O':c[1]++; break;
                case 'T':c[2]++; break;
                case '.':break;
                }
                switch(board[j][i])
                {
                case 'X':c[3]++; break;
                case 'O':c[4]++; break;
                case 'T':c[5]++; break;
                case '.':break;
                }
            }
            if(c[0]==4||c[0]==3&&c[2]==1||c[3]==4||c[3]==3&&c[5]==1)
            {
                xf=true;
            }
            if(c[1]==4||c[1]==3&&c[2]==1||c[4]==4||c[4]==3&&c[5]==1)
            {
                of=true;
            }
        }
        for(int i=0; i<4; i++)
        {
            switch(board[i][i])
            {
            case 'X':c[6]++; break;
            case 'O':c[7]++; break;
            case 'T':c[8]++; break;
            case '.':break;
            }
            switch(board[i][3-i])
            {
            case 'X':c[9]++; break;
            case 'O':c[10]++; break;
            case 'T':c[11]++; break;
            case '.':break;
            }
        }
        if(c[6]==4||c[6]==3&&c[8]==1||c[9]==4||c[9]==3&&c[11]==1)
        {
            xf=true;
        }
        if(c[7]==4||c[7]==3&&c[8]==1||c[10]==4||c[10]==3&&c[11]==1)
        {
            of=true;
        }
        if(xf&&!of)
        {
            printf("Case #%d: X won\n",cas);
        }
        else if(!xf&&of)
        {
            printf("Case #%d: O won\n",cas);
        }
        else if((xf&&of)||(!xf&&!of&&!flag))
        {
            printf("Case #%d: Draw\n",cas);
        }
        else
        {
            printf("Case #%d: Game has not completed\n",cas);
        }
    }
    return 0;
}
