#include <cstdio>
#include <cstring>

using namespace std;

int map[501][501];
char tmp;
int T,n,m,d;

int min(int a,int b){return a<b?a:b;}

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d",&T);
    for (int Case=1;Case<=T;Case++){
        scanf("%d%d%d\n",&n,&m,&d);
        for (int i=1;i<=n;i++){
            for (int j=1;j<=m;j++){
                scanf("%c",&tmp);
                map[i][j]=tmp-'0';
            }
            scanf("\n");
        }
        int max=0;
        for (int i=1;i<=n;i++)
            for (int j=1;j<=m;j++)
                for (int r=3;r<=min(n,m);r++) if (i+r-1<=n && j+r-1<=m){
                    double midx=(i+i+r-1)/2.0,midy=(j+j+r-1)/2.0,nowx=0,nowy=0;
                    for (int i1=i;i1<=i+r-1;i1++)
                        for (int j1=j;j1<=j+r-1;j1++) if (!(i1==i && j1==j) && !(i1==i && j1==j+r-1) && !(i1==i+r-1 && j1==j) && !(i1==i+r-1 && j1==j+r-1)){
                            nowx+=(i1*1.0-midx)*map[i1][j1];
                            nowy+=(j1*1.0-midy)*map[i1][j1];
                            //if (i==1 && j==1 && r==10) printf("%lf %lf %lf %lf\n",midx,midy,nowx,nowy);
                        }
                    if (!nowx && !nowy) if (r>max) max=r;       
        }
        if (max==0) printf("Case #%d: IMPOSSIBLE\n",Case);else printf("Case #%d: %d\n",Case,max);        
    }
}
