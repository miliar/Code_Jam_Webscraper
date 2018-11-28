/*CODE_BY_MANAS_KIRTI
Algo:Ad-hoc
Date:13/04/2013*/
using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include<bitset>
#include <set>
# define LLU long long  int
# define LLD long long double
# define FOR(i,N) for(int i=0;i<(N);i++)
# define FOR1(i,a,N) for(int i=a;i<(N);i++)
# define pb push_back
# define in(x) scanf("%d",&x)
# define out(x) printf("%d\n",x)
# define clr(a) memset(a,0,sizeof(a))
# define fill(a,x) memset(a,x,sizeof(a))
# define mp make_pair
# define INF_MAX 2147483647
# define INF_MIN -2147483647
# define maxn 51
# define mod 1000000007
int main()
{
    string ip[4];
    int t,r,c;
    bool flag=false;
    in(t);
    int cas=1;
    while(t--)
    {
        flag=false;
        FOR(i,4)
        cin>>ip[i];
        int winner=0;
        r=c=-1;
        FOR(i,4)
        {
            winner=0;
            FOR(j,4)
            {
                if(ip[i][j]==ip[i][0] || ip[i][j]=='T')
                winner++;
            }
            if(winner==4 && ip[i][0]!='.')
            {
                flag=true;
                r=i;
                c=0;
                break;
            }
        }
        if(flag)
        {
            printf("Case #%d: %c won\n",cas++,ip[r][c]);
            continue;
        }
        FOR(i,4)
        {
            winner=0;
            FOR(j,4)
            {
                if(ip[j][i]==ip[0][i] || ip[j][i]=='T')
                winner++;
            }
            if(winner==4 && ip[0][i]!='.')
            {
                flag=true;
                r=0;
                c=i;
                break;
            }
        }
        if(flag)
        {
            printf("Case #%d: %c won\n",cas++,ip[r][c]);
            continue;
        }
        winner=0;
        FOR(i,4)
        if(ip[i][i]==ip[0][0] || ip[i][i]=='T')
        winner++;
        if(winner==4 &&  ip[0][0]!='.')
        {
            printf("Case #%d: %c won\n",cas++,ip[0][0]);
            continue;
        }
        winner=0;
        FOR(i,4)
        if(ip[i][3-i]==ip[0][3] || ip[i][3-i]=='T')
        winner++;
        if(winner==4 &&  ip[0][3]!='.')
        {
            printf("Case #%d: %c won\n",cas++,ip[0][3]);
            continue;
        }
        flag=false;
        FOR(i,4)
        FOR(j,4)
        if(ip[i][j]=='.')
        {
            flag=true;
            break;
        }
        if(flag)
        printf("Case #%d: Game has not completed\n",cas++);
        else
        printf("Case #%d: Draw\n",cas++);
    }
    return 0;
}
