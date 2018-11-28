#include <cstdio>
using namespace std;

int R,C;
char mat[51][51];
int main ()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int z=1;z<=T;++z)
    {
    scanf("%d %d",&R,&C);
    for (int i=0;i<R;++i) scanf("%s",mat[i]);
    bool ok=1;
    for (int i=0;i<R;++i) for (int j=0;j<C;++j) if (mat[i][j]=='#')
    {
        if (i==R-1 || j==C-1 || mat[i][j+1]!='#' || mat[i+1][j]!='#' || mat[i+1][j+1]!='#') { ok=0,i=R; break; }
        mat[i][j]=mat[i+1][j+1]='/';
        mat[i+1][j]=mat[i][j+1]='\\';
    }
    printf("Case #%d:\n",z);
    if (!ok) printf("Impossible\n");
    else{ for (int i=0;i<R;++i) printf("%s\n",mat[i]); }
    }
    return 0;
}
