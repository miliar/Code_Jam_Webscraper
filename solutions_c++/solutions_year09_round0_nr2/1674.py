#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;

typedef struct{
        int x,y;
        int high;
        }point;

point a[10010];
int n,m;
int h[110][110];
int sum;
char ans[110][110];
const int di[4][2]={{-1,0},{0,-1},{0,1},{1,0}};

void dfs(int x, int y)
{
    int i,j,k,l;
    bool flag = false;
    int min = 1000000;
    for(i=0;i<4;i++)
    {
        int dx = x+di[i][0], dy = y + di[i][1];
        if(h[dx][dy] < min && dx <=n && dx >=1 && dy <=m && dy>=1 && h[dx][dy] < h[x][y])
        {
            k = dx, l = dy;
            min = h[dx][dy];
            flag = true;
        }
    }
    if(flag)
    {
        dfs(k,l);
        ans[x][y] = ans[k][l];
    }
    else
    {
        if(ans[x][y]==0)
        {
            ans[x][y] = (++sum)+'a'-1;
            return;
        }
    }
    return;
}


int main(int argc, char *argv[])
{
    int t,o;
    //freopen("E:/in.txt","r",stdin);
//freopen("E:/out.txt","w",stdout);
    scanf("%d",&t);

    for(o=1;o<=t;o++)
    {
        int i,j,k,l;
        scanf("%d%d",&n,&m);
        for(i=1;i<=n;i++)
            for(j=1;j<=m;j++)
            {
                scanf("%d",&h[i][j]);
                k = m*(i-1)+j;
                a[k].x = i, a[k].y = j, a[k].high = h[i][j];
            }
        //sort(a+1,a+1+n*m,cmp);        
        memset(ans,0,sizeof(ans));
        sum = 0;
        //for(i=1;i<=n*m;i++) cout<<(a[i].x-1)*m+a[i].y<<' ';cout<<endl;
        for(i=1;i<=n*m;i++)
        {
           if(ans[a[i].x][a[i].y] == 0)
           {             
               dfs(a[i].x,a[i].y);
           }
        }
        
        cout<<"Case #"<<o<<":\n";
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
            {
                cout<<ans[i][j];
                if(j < m) cout<<' ';
            }
            cout<<endl;
        }
    }
    return EXIT_SUCCESS;
}
