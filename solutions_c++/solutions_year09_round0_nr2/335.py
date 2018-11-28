#include<iostream>
using namespace std;

const int maxn = 101;
const int dx[4] = { -1 , 0 , 0 , 1 };
const int dy[4] = { 0 , -1 , 1 , 0 };

int map[maxn][maxn];
int fa[maxn*maxn];
int bo[maxn*maxn];
int n,m;

void init()
{
     scanf("%d%d",&n,&m);
     for (int i=0; i<n; i++ )
         for (int j=0; j<m; j++ ) scanf("%d",&map[i][j]);
}

int father(int x )
{
    if (fa[x]!=x) fa[x]=father(fa[x]);
    return fa[x];
}

void merge(int x,int y )
{
     fa[father(x)]=father(y);
}

void work()
{
     for (int i=0; i<n*m; i++ ) fa[i]=i;
     for (int i=0; i<n; i++ )
         for (int j=0; j<m; j++ )
         {
             int x=-1,y,t1,t2;
             for (int k=0; k<4; k++ )
             {
                 t1=i+dx[k];
                 t2=j+dy[k];
                 if (t1<0 || t1==n || t2<0 || t2==m) continue;
                 if (x==-1 || map[t1][t2]<map[x][y]) { x=t1; y=t2; }
             }
             if (x>=0 && map[x][y]<map[i][j]) merge(i*m+j,x*m+y);
         }
     
     memset(bo,0,sizeof(bo));
     int label=97;
     for (int i=0; i<n; i++ )
         for (int j=0; j<m; j++ )
         {
             int k=father(i*m+j);
             if (!bo[k]) bo[k]=label++;
             printf("%c",bo[k]);
             if (j<m-1) printf(" "); else printf("\n");
         }
}

int main()
{
    //freopen("b-3.in","r",stdin);
    //freopen("b-3.out","w",stdout);
    int test;
    scanf("%d",&test);
    for (int zy=0; zy<test; zy++ )
    {
        init();
        printf("Case #%d:\n",zy+1);
        work();
    }
    //fclose(stdin);
    //fclose(stdout);
}

