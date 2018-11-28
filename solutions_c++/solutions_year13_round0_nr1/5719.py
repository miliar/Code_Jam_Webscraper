#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
using namespace std;

struct node{
    int x,y;
};

vector <node> list;

char s[10][10];

inline char next(){
    char ch;
    do{
        ch=getchar();
    } while(ch!='.' && (ch<'A' || ch>'Z'));
    return ch;
}
bool check(char ch)
{
    int i,j;
    bool temp;
    for (i=1;i<=4;i++)
    {
        temp = true;
        for (j=0;j<4;j++)
            if (s[i][j]!=ch)
            {
                temp =false;
                break;
            }
        if (temp)
            return true;
    }
    for (j=0;j<4;j++)
    {
        temp = true;
        for (i=1;i<=4;i++)
            if (s[i][j]!=ch)
            {
                temp =false;
                break;
            }
        if (temp)
            return true;
    }
    if (s[1][0]==ch && s[2][1]==ch && s[3][2]==ch && s[4][3]==ch)
        return true;
    if (s[4][0]==ch && s[3][1]==ch && s[2][2]==ch && s[1][3]==ch)
        return true;
    return false;
}

int main()
{
    int i,j,k,CASE,t;
    bool win_X,win_O,point;
    scanf("%d",&CASE);
    for (t=1;t<=CASE;t++)
    {
        list.clear();
        point=false;
        for (i=1;i<=4;i++)
        {
            for (j=0;j<4;j++)
            {
                s[i][j]  = next();
                if (s[i][j]=='T')
                {
                    node node1;
                    node1.x=i;node1.y=j;
                    list.push_back(node1);
                }
                else if (s[i][j]=='.')
                    point = true;
            }


        }
        for (i=0;i<list.size();i++)
            s[list[i].x][list[i].y] = 'X';
        win_X = check('X');
        for (i=0;i<list.size();i++)
            s[list[i].x][list[i].y] = 'O';
        win_O = check('O');
        if (!win_X && !win_O && !point)
            printf("Case #%d: Draw\n",t);
        else if (!win_X && !win_O)
            printf("Case #%d: Game has not completed\n",t);
        else if (win_X && !win_O)
            printf("Case #%d: X won\n",t);
        else if (!win_X && win_O)
            printf("Case #%d: O won\n",t);
    }
    return 0;
}
