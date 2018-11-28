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

long long f[3000][11];
int limit[3000];
int a[3000];
int n,p;

void dfs(int now,int l,int r)
{
    if (r-l==1)
    {
        f[now][p-min(limit[l],limit[r])]=0;
        f[now][p-min(limit[l],limit[r])-1]=a[now];
    }
    else
    {
        dfs(now*2,l,(l+r)/2);
        dfs(now*2+1,(l+r)/2+1,r);
        for (int i=0;i<=p;i++)
            for (int j=0;j<=p;j++)
            {
                f[now][max(i,j)]=min(f[now][max(i,j)],f[now*2][i]+f[now*2+1][j]);
                f[now][max(max(i,j)-1,0)]=min(f[now][max(max(i,j)-1,0)],f[now*2][i]+f[now*2+1][j]+a[now]);
            }
    }
}

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int casenum=1;casenum<=T;casenum++)
    {
        scanf("%d",&p); 
        n=1 << p;
        for (int i=0;i<=n;i++)
            for (int j=0;j<=p;j++) f[i][j]=100000000000LL;
        for (int i=n;i>=1;i--) scanf("%d",&limit[i]);
        for (int i=n-1;i>=1;i--) scanf("%d",&a[i]);
        dfs(1,1,n);
        printf("Case #%d: %d\n",casenum,f[1][0]);
    }
}
