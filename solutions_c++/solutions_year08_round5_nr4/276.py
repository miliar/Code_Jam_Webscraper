#include <cstdio>
#include <cstring>
using namespace std;
const int base=10007;

int f[200][200];
bool dan[200][200];
int n,m,x,cases;

int get_s(int x,int y) {
    if (x<=0 || y<=0) return 0; else return f[x][y];
}   

int main() {
    scanf("%d",&cases);
    for (int kase=1;kase<=cases;kase++) {
        scanf("%d%d%d",&n,&m,&x);
        memset(f,0,sizeof(f));
        f[1][1]=1;
        memset(dan,0,sizeof(dan));
        int k1,k2;
        for (int i=1;i<=x;i++) {
            scanf("%d%d",&k1,&k2);
            dan[k1][k2]=true;    
        }    
        for (int i=1;i<=n;i++)
           for (int j=1;j<=m;j++) {
               if (dan[i][j]) continue;
               f[i][j]=(f[i][j]+get_s(i-1,j-2))%base;
               f[i][j]=(f[i][j]+get_s(i-2,j-1))%base;
           }    
        printf("Case #%d: %d\n",kase,f[n][m]);
    }    
}    
