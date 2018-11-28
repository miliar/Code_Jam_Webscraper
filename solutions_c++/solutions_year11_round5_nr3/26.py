#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<map>
#define PB push_back
#define MP make_pair
#define SZ(v) ((int)(v).size())
#define CLR(x) memset((x), 0, sizeof(x))
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FEACH(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define F first
#define S second
//using namespace std;
typedef long long LL;
inline LL Min(LL a,LL b){
    return a<b?a:b;
}
inline LL Max(LL a,LL b){
    return a>b?a:b;
}
inline LL Abs(LL a){
    return a>0?a:-a;
}

inline int md(int aa,int nn){
    return (aa+nn)%nn;
}
struct Edge{
    int s,t;
}edg[1000010];
bool cmp(Edge a,Edge b){
    return a.s<b.s;
}
int casN,n,m,edn[20010],v,e,vis[20010],ans,com[20010][2];
char inp[110][110];
inline int tr(int ii,int jj){
    return md(ii,n)*m+md(jj,m);
}
inline void dfs(int ii){
    for(int i=edn[ii];i<edn[ii+1];i++){
        if(!vis[edg[i].t]){
            vis[edg[i].t]=ans;
            dfs(edg[i].t);
        }
    }
}
int main(){
    scanf("%d",&casN);
    for(int III=0;III<casN;III++){
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++){
            scanf("%s",inp[i]);
        }
        v=n*m*2;
        e=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(inp[i][j]=='|'){
                    edg[e].s=tr(i,j);
                    edg[e++].t=tr(i-1,j)+n*m;
                    edg[e].s=tr(i,j);
                    edg[e++].t=tr(i+1,j)+n*m;
                }else if(inp[i][j]=='\\'){
                    edg[e].s=tr(i,j);
                    edg[e++].t=tr(i-1,j-1)+n*m;
                    edg[e].s=tr(i,j);
                    edg[e++].t=tr(i+1,j+1)+n*m;
                }else if(inp[i][j]=='/'){
                    edg[e].s=tr(i,j);
                    edg[e++].t=tr(i-1,j+1)+n*m;
                    edg[e].s=tr(i,j);
                    edg[e++].t=tr(i+1,j-1)+n*m;
                }else if(inp[i][j]=='-'){
                    edg[e].s=tr(i,j);
                    edg[e++].t=tr(i,j-1)+n*m;
                    edg[e].s=tr(i,j);
                    edg[e++].t=tr(i,j+1)+n*m;
                }
            }
        }
        memset(edn,0,sizeof(edn));
        for(int i=0;i<e;i++){
            edg[e+i].s=edg[i].t;
            edg[e+i].t=edg[i].s;
            edn[edg[i].s+1]++;
            edn[edg[i].t+1]++;
        }
        for(int i=1;i<=v;i++)edn[i]+=edn[i-1];
        e*=2;
        ans=0;
        std::sort(edg,edg+e,cmp);
        memset(vis,0,sizeof(vis));
        for(int i=0;i<v;i++){
            if(!vis[i]){
                ans++;
                vis[i]=ans;
                dfs(i);
            }
        }
        int out=1;
        for(int i=0;i<ans;i++)out=(out*2)%1000003;
        memset(com,0,sizeof(com));
        for(int i=0;i<v/2;i++){
            com[vis[i]][0]++;
        }
        for(int i=v/2;i<v;i++){
            com[vis[i]][1]++;
        }
        for(int i=1;i<=ans;i++){
            if(com[i][0]!=com[i][1])out=0;
        }
        printf("Case #%d: %d\n",III+1,out);
    }
    scanf(" ");
    return 0;
}

