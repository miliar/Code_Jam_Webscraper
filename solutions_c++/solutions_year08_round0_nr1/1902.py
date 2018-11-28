#include <cmath>
#include <string>
#define maxint 1000000000
using namespace std;

char name[105][105],list[1010][105],str[105];
int opt[1010][105],num[1010],tot,ans,n,m;

int main(){
    //freopen("a.in","r",stdin);
    //freopen("a.out","w",stdout);
    scanf("%d",&tot);
    for (int cases=0;cases<tot;++cases){
        scanf("%d",&n);
        gets(str);
        for (int i=0;i<n;++i) gets(name[i]);
        scanf("%d",&m);
        gets(str);
        for (int i=0;i<m;++i){
            gets(list[i]);
            for (int j=0;j<n;++j)
                if (strcmp(name[j],list[i])==0){
                    num[i]=j;
                    break;
                }
        }
        if (m==0){
            printf("Case #%d: 0\n",cases+1);
            continue;
        }
        for (int i=0;i<m;++i)
            for (int j=0;j<n;++j)
                opt[i][j]=maxint;
        for (int i=0;i<n;++i) if (strcmp(name[i],list[0])) opt[0][i]=0;
        for (int i=0;i+1<m;++i)
            for (int j=0;j<n;++j){
                for (int k=0;k<n;++k){
                    if (num[i+1]==k) continue;
                    if (j==k) continue;
                    if (opt[i][j]+1<opt[i+1][k]) opt[i+1][k]=opt[i][j]+1;
                }
                if ((num[i+1]!=j)&&(opt[i][j]<opt[i+1][j])) opt[i+1][j]=opt[i][j];
            }
        int ans=maxint;
        for (int i=0;i<n;++i) if (opt[m-1][i]<ans) ans=opt[m-1][i];
        printf("Case #%d: %d\n",cases+1,ans);
    }
}
