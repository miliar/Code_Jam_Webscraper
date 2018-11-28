#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;

bool c[200][200],d[200][200];
int n;

bool check()
{
    for (int i=0;i<130;i++)
        for (int j=0;j<130;j++)
            if (c[i][j]) return true;
    return false;
}


int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    int T;
    scanf("%d\n",&T);
    for (int casenum=1;casenum<=T;casenum++)
    {
        memset(c,false,sizeof(c));
        scanf("%d\n",&n);
        for (int i=0;i<n;i++)
        {
            int x1,x2,y1,y2;
            scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
            for (int x=x1;x<=x2;x++)
                 for (int y=y1;y<=y2;y++)
                    c[x][y]=true;
        }
        int ans=0;
        while (check())
        {
            memset(d,false,sizeof(d));
            for (int i=1;i<130;i++)
                for (int j=1;j<130;j++)
                {
                    if (c[i][j] && (c[i-1][j] || c[i][j-1])) d[i][j]=true;
                    if (c[i-1][j] && c[i][j-1])d[i][j]=true;
                }
            for (int i=1;i<130;i++)
                for (int j=1;j<130;j++) c[i][j]=d[i][j];
            ans++;
        }
        printf("Case #%d: %d\n",casenum,ans);
    }
}
