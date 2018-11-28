/* @author Sidharth Gupta */

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <cassert>

#define MOD 1000000007
#define MIN(a,b) ((a)>(b)?(b):(a))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ABS(a) MAX(a,-(a))
#define SET(a,b) memset(a, b, sizeof(a))
#define EVEN(a) ((a&1)==0)
#define SQR(a) ((a)*(a))
#define EPS 0.0001

typedef long long int lli;
typedef unsigned long long int llui;
typedef unsigned int uint;

using namespace std;

char grid[10][10];

int check()
{
    int i,j;
    int x,o,t;

    //row check
    for(i=0;i<4;++i)
    {
        x = o = t = 0;
        for(j=0;j<4;++j)
        {
            if(grid[i][j] == 'X')
                ++x;
            else if(grid[i][j] == 'O')
                ++o;
            else if(grid[i][j] == 'T')
                ++t;
        }

        if(x==4)
            return 1;
        else if(o==4)
            return 2;
        else if(x==3 && t==1)
            return 1;
        else if(o==3 && t==1)
            return 2;
    }

    //column check
    for(i=0;i<4;++i)
    {
        x = o = t = 0;
        for(j=0;j<4;++j)
        {
            if(grid[j][i]=='X')
                ++x;
            else if(grid[j][i]=='O')
                ++o;
            else if(grid[j][i] == 'T')
                ++t;
        }

        //printf("x %d o %d t %d\n", x, o, t);

        if(x==4)
            return 1;
        else if(o==4)
            return 2;
        else if(x==3 && t==1)
            return 1;
        else if(o==3 && t==1)
            return 2;
    }

    //printf("here\n");

    //diagonal check
    x = o =  t = 0;
    for(i=0;i<4;++i)
    {
        if(grid[i][i] == 'X')
            ++x;
        else if(grid[i][i] == 'O')
            ++o;
        else if(grid[i][i] == 'T')
            ++t;
    }
    if(x==4)
        return 1;
    else if(o==4)
        return 2;
    else if(x==3 && t==1)
        return 1;
    else if(o==3 && t==1)
        return 2;

    x = o =  t = 0;
    for(i=0;i<4;++i)
    {
        if(grid[i][3-i] == 'X')
            ++x;
        else if(grid[i][3-i] == 'O')
            ++o;
        else if(grid[i][3-i] == 'T')
            ++t;
    }
    if(x==4)
        return 1;
    else if(o==4)
        return 2;
    else if(x==3 && t==1)
        return 1;
    else if(o==3 && t==1)
        return 2;


    //game not over
    for(i=0;i<4;++i)
    {
        for(j=0;j<4;++j)
        {
            if(grid[i][j] == '.')
                return 4;
        }
    }

    //the game is a draw if we reach here.
    return 3;
}

int main()
{
    int t, i, status, tc;

    scanf("%d",&tc);

    for(t = 1; t <= tc; ++t)
    {
        for(i=0;i<4;++i)
            scanf("%s",grid[i]);

        status = check();

        printf("Case #%d: ", t);
        if(status == 1)
            printf("X won\n");
        else if(status == 2)
            printf("O won\n");
        else if(status == 3)
            printf("Draw\n");
        else
            printf("Game has not completed\n");
    }

    return 0;
}
