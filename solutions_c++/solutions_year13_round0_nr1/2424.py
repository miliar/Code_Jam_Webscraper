#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<stack>
#include<queue>
#include<vector>
#include<map>
#include<ctime>
#include<set>
#include<string>
using namespace std;
const int MAX=200005;
const int inf=1<<30;
#define ll long long
#define PB push_back
#define PII pair<int,int>
#define MP(x,y) make_pair(x,y)
char s[5][5];
int check(char goal)
{
    int t,b;
    int mi = 100;
    for(int i = 0; i < 4;i++)
    {
        t = b = 0;
        for(int j = 0; j < 4; j++)
            if(s[i][j]== goal || s[i][j]=='T')
                t++;
            else if (s[i][j]=='.')
                b++;
        if(t == 4)
            return -1;
        if(t+b==4)
            mi = min(mi, b);
    }
    for (int i = 0; i < 4; i++)
    {
        t = b = 0;
        for (int j = 0; j < 4; j++)
            if(s[j][i] == goal || s[j][i]== 'T')
                t++;
            else if(s[j][i]=='.')
                b++;
        if(t==4)
            return -1;
        if(t+b==4)
            mi = min(mi, b);
    }
    t=b=0;
    for (int i = 0; i < 4; i++)
        if(s[i][i] == goal || s[i][i] == 'T')
            t++;
        else if (s[i][i]=='.')
            b++;
    if (t == 4)
        return -1;
    if(t+b==4)
        mi =min(mi,b);
    t = b = 0;
    for (int i = 0; i < 4; i++)
        if(s[i][4-i-1] == goal || s[i][4-i-1] == 'T')
            t++;
        else if(s[i][4-i-1]=='.')
            b++;
    if (t==4)
        return -1;
    if (t+b==4)
        mi = min(mi, b);
    return mi;

}
int main()
{
    int i,j,k,T;
    freopen("A-small.in","r",stdin);
    freopen("1.txt","w",stdout);
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        int cnt_x=0,cnt_o=0;
        for(i=0;i<4;i++)
        {
            scanf("%s",s[i]);
            for(j=0;j<4;j++)
            {
                if(s[i][j]=='x')
                    cnt_x++;
                if(s[i][j]=='o')
                    cnt_o++;
            }
        }
        int tot = cnt_x + cnt_o;
        int blank = 16 - tot - 1;
        printf("Case #%d: ",cas);
        int res1 = check('X');
        int res2 = check('O');
        if (res1 == -1)
        {
            printf("X won\n");
        }
        else if (res2 == -1)
        {
            printf("O won\n");
        }
        else
        {
            char first = 'X';
            if (tot %2 == 1)
                first = 'O';
            if (first == 'X')
            {
                cnt_x = (blank+1)/2;
                cnt_o = blank/2;
            }
            else
            {
                cnt_o = (blank+1)/2;
                cnt_x = blank/2;
            }
            //cout<<"res1="<<res1<<" res2="<<res2<<endl;
            if ( res1 <= cnt_x || res2 <= cnt_o)
            {
                printf("Game has not completed\n");
            }
            else
            {
                printf("Draw\n");
            }
        }

    }
    return 0;
}
/*
6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O
*/
