#include <cstdio>
#include <vector>
using namespace std;

vector <int> okstate,num;
int opt[15][1500],state[15],tot,n,m;
char map[15][15];

int main(){
    scanf("%d",&tot);
    for (int cases=0;cases<tot;++cases){
        scanf("%d%d",&n,&m);
        for (int i=1;i<=n;++i) scanf("%s",map[i]);
        for (int i=1;i<=n;++i){
            state[i]=0;
            for (int j=0;j<m;++j){
                state[i]*=2;
                if (map[i][j]=='x') ++state[i];
            }
        }
        memset(opt,0,sizeof(opt));
        okstate.clear();
        num.clear();
        for (int i=0;i<(1<<m);++i){
            if (i&(i<<1)) continue;
            if (i&(i>>1)) continue;
            okstate.push_back(i);
            int cur=0;
            for (int j=0;j<m;++j) if ((i>>j)&1) ++cur;
            num.push_back(cur);
        }
        int ans=0;
        for (int i=1;i<=n;++i)
            for (int j=0;j<okstate.size();++j)
                for (int k=0;k<okstate.size();++k){
                    int oldstate=okstate[j];
                    int newstate=okstate[k];
                    if (newstate&(oldstate<<1)) continue;
                    if (newstate&(oldstate>>1)) continue;
                    if (newstate&state[i]) continue;
                    if (opt[i-1][oldstate]+num[k]>opt[i][newstate]){
                        opt[i][newstate]=opt[i-1][oldstate]+num[k];
                        if (opt[i][newstate]>ans) ans=opt[i][newstate];
                    }
                }
        printf("Case #%d: %d\n",cases+1,ans);
    }
    return 0;
}
