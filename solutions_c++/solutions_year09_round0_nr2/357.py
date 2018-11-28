#include <iostream>

using namespace std;

const int dx[4] = {-1, 0, 0, 1};
const int dy[4] = {0, -1, 1, 0};
const int N = 110;

int a[N][N];
int m, n;
int lab[N][N];
char ans[N][N];
int g[N*N][5];
bool ind[N*N];

struct node
{
    int root, least;
    int id;
    bool operator < (const node &e) const
    {
        return least < e.least;
    }
}b[50];

inline int X(int k)
{
    return (k-1)/n + 1;
}

inline int Y(int k)
{
    return (k-1)%n + 1;
}

int BFS(int root, int cnt)
{
    lab[X(root)][Y(root)] = cnt;
    int q[10010], head, tail;
    int ans = root;
    int i, j, k;
    
    q[head=tail=1] = root;
    while(head <= tail)
    {
        i=q[head++];
        for(j=1;j<=g[i][0];j++)
        {
            ans = min(ans, g[i][j]);
            lab[X(g[i][j])][Y(g[i][j])] = cnt;
            q[++tail] = g[i][j];
        }
    }
    return ans;
}

int main()
{
    int i, j, k, ca;
    
    freopen("large.in", "r", stdin);
    freopen("out.txt", "w",stdout);
    scanf("%d",&ca);
    
    for(int cs=1;cs<=ca;cs++)
    {
        scanf("%d%d",&m,&n);
        for(i=1;i<=m;i++)
            for(j=1;j<=n;j++)
                scanf("%d",&a[i][j]);
        
        printf("Case #%d:\n",cs);
        
        memset(ind, false, sizeof(ind));
        for(i=1;i<=m*n;i++) g[i][0]=0;
        
        for(i=1;i<=m;i++)
            for(j=1;j<=n;j++)
            {
                int tmp = 1000000, t;
                for(k=0;k<4;k++){
                    int wx=i+dx[k], wy=j+dy[k];
                    if(wx<1||wx>m||wy<1||wy>n) continue;
                    if(a[wx][wy] < tmp){
                        tmp = a[wx][wy];
                        t = k;
                    }
                }
                if(tmp < a[i][j]){
                    int wx=i+dx[t], wy=j+dy[t];
                    t = (wx-1)*n+wy;
                    g[t][++g[t][0]] = (i-1)*n+j;
                    ind[(i-1)*n+j] = true;
                }
            }
        int cnt = 0;
        for(i=1;i<=m;i++)
            for(j=1;j<=n;j++){
                k=(i-1)*n+j;
                if(!ind[k]){
                    cnt++;
                    b[cnt].root = k;
                    b[cnt].id = cnt;
                    b[cnt].least = BFS(k, cnt);
                }
            }
        
        sort(b+1,b+cnt+1);
        for(k=0;k<cnt;k++)
            for(i=1;i<=m;i++)
                for(j=1;j<=n;j++)
                    if(lab[i][j]==b[k+1].id) ans[i][j] = k+'a';
        
        for(i=1;i<=m;i++)
            for(j=1;j<=n;j++)
                printf("%c%c",ans[i][j], j==n? '\n':' ');
    }
    scanf("%d",&n);
    return 0;
}
                
        
    
        
    
