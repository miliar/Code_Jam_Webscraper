#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <utility>
#include <string>
#include <map>
#include <set>
#define maxn 511

#define INP "C.in"
#define OUP "C.out"

using namespace std;

int n;
int sum;
int a[maxn + 1];
bool done[2111111]={};
int mark[maxn + 1];

bool dfs1(int depth,int sum)
{
    if (sum==0){
        for (int i=1;i<=n;i++)
            if (mark[i]==2)
                printf("%d ",a[i]);
        printf("\n");
        return true;
    }
    if (depth>n)
        return false;
    if (a[depth]<=sum && (!mark[depth])){
        mark[depth] = 2;
        if (dfs1(depth + 1,sum - a[depth]))
            return true;
        mark[depth] = 0;
        if (dfs1(depth + 1,sum))
            return true;
    }
    return false;
}

bool dfs(int depth,int x)
{
    if (x*2>sum)
        return 0;
    if (x!=0){
        if (mark[11] && mark[12] && mark[14] && x==12270)
            printf("haha\n");
        if (dfs1(1,x)){
            for (int i=1;i<=n;i++)
                if (mark[i]==1)
                    printf("%d ",a[i]);
            printf("\n");
            return true;
        }
    }
    if (depth>n)
        return 0;
    mark[depth] = 1;
    if (dfs(depth + 1,x + a[depth]))
        return true;
    mark[depth] = 0;
    if (dfs(depth + 1,x))
        return true;
    return false;
}

int main()
{
    freopen(INP,"r",stdin);
    freopen(OUP,"w",stdout);
    int tc;
    scanf("%d",&tc);
    for (int tt=1;tt<=tc;tt++){
        scanf("%d",&n);
        sum = 0;
        for (int i=1;i<=n;i++)
            scanf("%d",&a[i]),sum += a[i];
        printf("Case #%d:\n",tt);
        memset(mark,0,sizeof(mark));
        memset(done,0,sizeof(done));
        if (!dfs(1,0))
            printf("Impossible\n");
    }
    return 0;
}
