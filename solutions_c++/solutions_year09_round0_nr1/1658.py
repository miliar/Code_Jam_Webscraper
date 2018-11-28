#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <string.h>
#include <string>

#define PI 3.14159265358979
#define PB(x) push_back(x)
using namespace std;
typedef long long LL;

const int N = 1100;

vector<int> vx[N];
vector<int> vx2[N];
vector<int> ans[N];

int colour[N];
int counts;
int queue[N];//拓扑序
bool v[N];
int n,m;

    void dfs(int j)
    {
        int i,k;
        for (i=0;i<(int)vx[j].size();i++)
        {
            k = vx[j][i];
            if (v[k]) continue;
            v[k] = 1;
            dfs(k);
        }
        queue[counts++] = j;
    }

    void ndfs(int j,int c)
    {
        int i,k;
        colour[j] = c;
        ans[c].PB(j);
        for ( i =0 ;i<(int)vx2[j].size();i++ )
        {
            k = vx2[j][i];
            if (v[k]) continue;
            v[k] = 1;
            ndfs(k,c);
        }
    }

    void kosaraju()
    {
        int i,j;
        counts = 0;
        memset(v,0,sizeof(v));
        for (i=0;i<n;i++)
        if (!v[i])
        {
            v[i] = 1;
            dfs(i);
        }

//        for (i=n-1;i>=0;i--) printf("%d ",queue[i]);printf("\n");//debug

        memset(v,0,sizeof(v));
        j = 0;
        int k;
        for ( i=n-1;i>=0;i-- )
        {
            k = queue[i];
            if (!v[ k ])
            {
                v[ k ] = 1;
                ndfs(k,j);
                j++;
            }
        }
        counts = j;
    }

    void inputing()
    {
        int i;
        scanf("%d%d",&n,&m);
        for (i=0;i<=n;i++)
        {
            vx[i].clear();
            vx2[i].clear();
        }
        for (i=0;i<m;i++)
        {
            int a,b;
            scanf("%d%d",&a,&b);
            a--,b--;
            vx[a].PB(b);
            vx2[b].PB(a);
        }
    }

    void outputing()
    {
//        int i,j;
        if (counts ==1)
        printf("Yes\n");
        else printf("No\n");
//        for (i=0;i<counts;i++)
//        {
//            printf("set %d: \n",i);
//            for (j=0;j<(int)ans[i].size();j++)
//            printf("  %d",ans[i][j]);
//            printf("\n");
//        }

    }

int main()
{
//    freopen("inputing","r",stdin);
    int cas;
    scanf("%d",&cas);
    while (cas--)
    {
        inputing();
        kosaraju();
        outputing();
    }
    //freopen("outputing","w",stdout);

    return 0;
}


