#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <iterator>
#include <utility>
using namespace std;

template <class T> T gcd(T a, T b) { return b==0 ? a : gcd(b,a%b) ; }
template <class T> T maxm(T a, T b) { return a > b ? a : b ; }
template <class T> T minm(T a, T b) { return a < b ? a : b ; }
template <class T> T abs(T a) { return a > 0 ? a : (-1)*a ; }
template <class T> T sq(T a) { return a * a ; }

#define clr(a) memset(a,0,sizeof(a))
#define set(a) memset(a,-1,sizeof(a))
#define R(a) freopen(a,"r",stdin)
#define W(t) while(t--)
#define forr(x, b, e)    for (int x = (b); x <= (e); x++)
#define S(n) scanf("%d",&n)

char grid[10][10];

bool check(char ch)
{
    int i,j,count=0;
    for(i=0;i<4;i++)
    {
        count=0;
        for(j=0;j<4;j++)
        {
            if(grid[i][j]==ch || grid[i][j]=='T')
                count++;
        }
        if(count==4)
        {
            return true;
        }
    }

    for(j=0;j<4;j++)
    {
        count=0;
        for(i=0;i<4;i++)
        {
            if(grid[i][j]==ch || grid[i][j]=='T')
                count++;
        }
        if(count==4)
        {
            return true;
        }
    }

    count=0;
    for(i=0;i<4;i++)
    {
        if(grid[i][i]=='T' || grid[i][i]==ch)
            count++;
    }
    if(count==4)
        return true;

    count=0;
    for(i=0;i<4;i++)
    {
        if(grid[i][3-i]=='T' || grid[i][3-i]==ch)
            count++;
    }
    if(count==4)
        return true;

    return false;

}

int main()
{
    int t,i,j,flag,cnt=0;
    bool ans;
    char ch;
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    S(t);
    W(t)
    {
        flag=0;
        for(i=0;i<4;i++)
        {
            getchar();
            for(j=0;j<4;j++)
            {
                scanf("%c",&grid[i][j]);
                if(grid[i][j]=='.')
                    flag=1;
            }
        }
        getchar();

        /*
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cout<<grid[i][j];
            }
            cout<<endl;
        }
        */

        ch='X';
        ans=check(ch);
        //cout<<ans<<endl;
        if(ans)
        {
            printf("Case #%d: %c won\n",++cnt,ch);
            continue;
        }

        ch='O';
        ans=check(ch);
        //cout<<ans<<endl;
        if(ans)
        {
            printf("Case #%d: %c won\n",++cnt,ch);
            continue;
        }

        if(flag==1)
        {
            printf("Case #%d: Game has not completed\n",++cnt);
        }
        else
        {
            printf("Case #%d: Draw\n",++cnt);
        }
    }
    return 0;
}
