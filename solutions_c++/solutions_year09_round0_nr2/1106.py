#include <iostream>
#include <vector>
#define MAXN 110
using namespace std;
const int td[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
const int rev[4]={3,2,1,0};
vector <int> ke[MAXN][MAXN];
int a[MAXN][MAXN], kq[MAXN][MAXN];
int ntest, m, n, id;

void dfs(int i, int j)
{
     kq[i][j]=id;
     int lim=ke[i][j].size();
     for (int k=0; k<lim; k++)
     {
         int i1=i+td[ke[i][j][k]][0], j1=j+td[ke[i][j][k]][1];
         if (kq[i1][j1]==-1)
            dfs(i1,j1);
     }
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.ou","w",stdout);
    
    scanf("%d",&ntest);
    for (int test=1; test<=ntest; test++)
    {
        scanf("%d%d",&m,&n);
        for (int i=1; i<=m; i++)
            for (int j=1; j<=n; j++)
            {
                scanf("%d",&a[i][j]);
                ke[i][j].clear();
            }
        for (int i=1; i<=m; i++)
            for (int j=1; j<=n; j++)
            {
                int nho=1000000000 ,best;
                for (int k=0; k<4; k++)
                {
                    int i1=i+td[k][0], j1=j+td[k][1];
                    if (i1<1 || i1>m || j1<1 || j1>n) continue;
                    if (a[i1][j1]<nho)
                    {
                       nho=a[i1][j1];
                       best=k;
                    }
                }
                if (nho<a[i][j])
                {
                   ke[i][j].push_back(best);
                   ke[i+td[best][0]][j+td[best][1]].push_back(rev[best]);
                }
            }
        memset(kq,-1,sizeof(kq));
        id=-1;
        for (int i=1; i<=m; i++)
            for (int j=1; j<=n; j++)
                if (kq[i][j]==-1)
                {
                   id++;
                   dfs(i,j);
                }
        printf("Case #%d:\n",test);
        for (int i=1; i<=m; i++)
        {
            for (int j=1; j<n; j++)
                printf("%c ",char(kq[i][j]+'a'));
            printf("%c\n",char(kq[i][n]+'a'));
        }       
    }
    
    return 0;
}
