#include <cstdio>
#include <cstring>
#define REP(i,n) for(int i=0,_n=(n);i<_n;i++)
#define FOR(i,a,b) for(int i=(a),_n=(b);i<=_n;i++)
int cut[104],best[104][104];

int calc(int L,int R)
{
    if (L+1 == R) return 0;
    if (best[L][R]==-1)
    {
        int res = 2000000000;
        for(int i=L+1;i<R;i++) 
					res <?= calc(L,i) + calc(i,R) + cut[R] - cut[L]-2;
        best[L][R] = res;
    }
    return best[L][R];
}
int main()
{
    int L,n,t;
		scanf("%d",&t);
		REP(__,t)
    {
        scanf("%d %d",&L,&n);
        for(int i=1;i<=n;i++) scanf("%d",cut+i);
        cut[0] = 0;
        cut[n+1] = L+1;
        memset(best,-1,sizeof(best));
        printf("Case #%d: %d\n",__+1,calc(0,n+1));
        fprintf(stderr,"Case #%d: %d\n",__+1,calc(0,n+1));
    }
    return 0;
}
