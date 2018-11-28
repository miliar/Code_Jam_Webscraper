#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<iostream>
#include<cstdlib>
#include<queue>
#include<sstream>
#include<queue>
#include<ctype.h>
#include<cstring>


using namespace std;

#define re return
#define co continue
#define pb push_back
#define br break
#define sz size


#define pf printf
#define sf scanf

char grid[7][7];

bool Duality(char player, int i, int j)
{
    if ( grid[i][j] == player || grid[i][j] == 'T')
        return true;
    return false;
}

bool Won(char player)
{
    // test two diagonals.
    int i,j;
    j = 0;
    for(i=0;i<4;i++)
    {
        if ( !Duality(player, i, j) )
            br;
        j++;
    }
    if ( i==4)
        return true;
    j = 3;
    for(i=0;i<4;i++)
    {
        if ( !Duality(player, i, j))
            br;
        j--;
    }
    if( i==4)
        return true;
    // sweep rows
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
            if ( !Duality(player, i, j) )
                br;
        if ( j==4)
            return true;
    }
    //sweep columns
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
            if ( !Duality(player, j, i) )
                br;
        if ( j==4)
            return true;
    }
    return false;

}

bool AllCovered()
{
    int i,j;
    for(i=0;i<4;i++)
        for(j=0;j<4;j++)
        if ( grid[i][j] == '.')
            return false;
    return true;
}

int main()
{

    //freopen("sample.txt","r",stdin);
    freopen("A-large.in","r",stdin);

    freopen("A.ans","w",stdout);

    int t;
    sf("%d",&t);
    int kase=1;
    while  ( t--)
    {
        int i;
        for(i=0;i<4;i++)
            scanf("%s",grid[i]);
        pf("Case #%d: ",kase++);
        // test for player 1
        if ( Won('X') )
            cout<<" X won"<<endl;
        else if ( Won('O'))
            cout<<" O won"<<endl;
        else if ( AllCovered() )
            cout<< " Draw"<<endl;
        else
            cout<< " Game has not completed"<<endl;


    }
    return 0;
}
