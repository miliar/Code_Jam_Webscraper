#include<cstdio>
#include<cstring>
#include<cmath>
#include<ctime>
#include<cstdlib>
#include<queue>
#include<stack>
#include<vector>
#include<set>
#include<algorithm>
#include<iostream>
#include<deque>

#define inf 1000000000

using namespace std;

int n;
char tab[4][5];

bool won(char a)
{
    int x, y, t=false;
    for(int i=0; i<4; i++)
        for(int j=0; j<4; j++)
            if(tab[i][j]=='T')
            {
                x=i;
                y=j;
            }
    tab[x][y]=a;
    for(int i=0; i<4; i++)
    {
        int c=0;
        for(int j=0; j<4; j++)
            if(tab[i][j]==a)
                c++;
        if(c==4)
            t=true;
    }
    for(int i=0; i<4; i++)
    {
        int c=0;
        for(int j=0; j<4; j++)
            if(tab[j][i]==a)
                c++;
        if(c==4)
            t=true;
    }
    int c=0;
    for(int i=0; i<4; i++)
        if(tab[i][i]==a)
            c++;
    if(c==4)
        t=true;
    c=0;
    for(int i=0; i<4; i++)
        if(tab[3-i][i]==a)
            c++;
    if(c==4)
        t=true;


    tab[x][y]='T';
    return t;
}

int main()
{
scanf("%d", &n);
for(int i=1; i<=n; i++)
{
    for(int j=0; j<4; j++)
        scanf("%s", tab[j]);
    int amount = 0;
    for(int j=0; j<4; j++)
        for(int k=0; k<4; k++)
            if(tab[j][k]!='.')
                amount++;
    if(won('X'))
        printf("Case #%d: %c won\n", i, 'X');
    else if(won('O'))
        printf("Case #%d: %c won\n", i, 'O');
    else if(amount<16)
        printf("Case #%d: Game has not completed\n", i);
    else
        printf("Case #%d: Draw\n", i);
    
}
return 0;
}
