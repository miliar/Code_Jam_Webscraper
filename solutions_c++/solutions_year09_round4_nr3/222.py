#include <iostream>
using namespace std;

int n,m,p[100][100],match[100];
bool g[100][100],c[100];

bool find(int x)
{
    for (int y=0;y<n;y++)
        if (!c[y]&&g[x][y])
        {
            c[y]=1;
            if (match[y]==-1||find(match[y]))
            {
                match[y]=x;
                return 1;    
            }   
        }    
    return 0;
}

int count()
{
    int ret=0;
    memset(match,-1,sizeof(match));
    for (int i=0;i<n;i++)
    {
        memset(c,0,sizeof(c));
        if (find(i)) 
            ret++;
    }
    return ret;
}

main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);   
    int t;
    cin>>t;
    for (int task=1;task<=t;task++)
    {
        cin>>n>>m;
        for (int i=0;i<n;i++)
            for (int j=0;j<m;j++)
                cin>>p[i][j];
        memset(g,0,sizeof(g));
        for (int i=0;i<n;i++)
            for (int j=0;j<n;j++)
            {
                g[i][j]=1;
                for (int k=0;k<m;k++)   
                    if (p[i][k]<=p[j][k])
                    {
                        g[i][j]=0;
                        break;   
                    }
            }   
        printf("Case #%d: %d\n",task,n-count());
    }
}
