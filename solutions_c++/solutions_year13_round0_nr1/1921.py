#include <iostream>
#include <cstdio>
using namespace std;

char map[6][6];

bool win(char ch)
{
    bool res=0;
    int i;
    for(i=1;i<=4;i++)
    {
        if((map[i][1]==ch||map[i][1]=='T') 
            && (map[i][2]==ch||map[i][2]=='T')
            && (map[i][3]==ch||map[i][3]=='T')
            && (map[i][4]==ch||map[i][4]=='T'))
        {
            res=1;
            break;
        }
        if((map[1][i]==ch||map[1][i]=='T') 
            && (map[2][i]==ch||map[2][i]=='T')
            && (map[3][i]==ch||map[3][i]=='T')
            && (map[4][i]==ch||map[4][i]=='T'))
        {
            res=1;
            break;
        }
        if((map[1][1]==ch||map[1][1]=='T')
            && (map[2][2]==ch||map[2][2]=='T')
            && (map[3][3]==ch||map[3][3]=='T')
            && (map[4][4]==ch||map[4][4]=='T'))
        {
            res=1;
            break;
        }
        if((map[1][4]==ch||map[1][4]=='T')
            && (map[2][3]==ch||map[2][3]=='T')
            && (map[3][2]==ch||map[3][2]=='T')
            && (map[4][1]==ch||map[4][1]=='T'))
        {
            res=1;
            break;
        }
    }
    return res;
}
            
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int i,j,cas,o;
    bool notcom;
    scanf("%d",&cas);
    for(o=1;o<=cas;o++)
    {
        printf("Case #%d: ",o);
        notcom=0;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
            {
                cin>>map[i][j];
                if(map[i][j]=='.')
                    notcom=1;
            }
        if(win('X')) printf("X won\n");
        else if(win('O')) printf("O won\n");
        else if(notcom==1) printf("Game has not completed\n");
        else printf("Draw\n");
    }
    return 0;        
}
