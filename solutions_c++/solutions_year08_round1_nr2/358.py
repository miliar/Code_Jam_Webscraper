#include <cstdio>
#include <cstring>


const int oo=2000000000;
const int Mal=1,UnMal=2;
int custom[128][16];
int m,n;

bool ok(int k,int*bit)
{
    for(int i=1;i<=n;++i)
        if(custom[k][i])
            if(custom[k][i]==UnMal&&bit[i-1]==0||custom[k][i]==Mal&&bit[i-1]==1)
                return true;      // printf("**\n");
    return false;
}

int cal(int* bit)
{
    int i;
    
    for(i=1;i<=m;++i)
        if(!ok(i,bit))
            return oo;

    int cnt=0;
    for(i=0;i<n;++i)
        if(bit[i])
            ++cnt;
    return cnt;
}

int main()
{
    int re,cas,i,j,state,taste,limit,t,best;
    int bit[16],res[16];
    
    freopen("B-small.in","r",stdin);
    freopen("B-small.out","w",stdout);

    for(scanf("%d",&re),cas=1;re--;++cas){
        scanf("%d%d",&n,&m);
        memset(custom,0,sizeof custom);
        for(i=0;i<m;++i){
            scanf("%d",&t);
            for(j=0;j<t;++j){
                scanf("%d%d",&taste,&state);
                if(state==0)
                    custom[i+1][taste]=UnMal;
                else
                    custom[i+1][taste]=Mal;
            }
        }
        limit=(1<<n);
        best=oo;
        for(i=0;i<limit;++i){
            for(j=0;j<n;++j)
                bit[j]=( (i>>j)&1 );
            if(cal(bit)<best){
                best=cal(bit);
                for(j=0;j<n;++j)
                    res[j]=bit[j];
            }
        }
        if(best==oo)
            printf("Case #%d: IMPOSSIBLE\n",cas);
        else{
            printf("Case #%d:",cas);
            for(i=0;i<n;++i)
                printf(" %d",res[i]);
            printf("\n");
        }
    }
}
