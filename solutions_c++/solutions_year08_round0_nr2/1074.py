#include<cstdio>
#include<cstring>
using namespace std;

const int MAXN  =   200+10;

int E[MAXN],next[MAXN*MAXN],y[MAXN*MAXN],edgesum;
int start_a[MAXN],start_b[MAXN],end_a[MAXN],end_b[MAXN];
int linky[MAXN*2];
bool vist[MAXN];
int T,NA,NB;

int gettime(){
    int a,b;
    scanf("%d:%d", &a, &b);
    return a*60+b;
}

void init(){
    scanf("%d%d%d", &T, &NA, &NB);
    for(int i=0; i<NA; ++i){
        start_a[i] = gettime();
        end_a[i] = gettime();
    }
    for(int i=0; i<NB; ++i){
        start_b[i] = gettime();
        end_b[i] = gettime();
    }
}

void addedge(int a,int b){
    ++edgesum;
    next[edgesum] = E[a];
    y[edgesum] = b;
    E[a] = edgesum;
}

bool find(int v){
    if(vist[v])return false;
    vist[v] = true;
    for(int i=E[v]; i!=-1; i=next[i]){
        int u = y[i];
        if(linky[u] == -1 || find(linky[u])){
            linky[u] = v;
            return true;
        }
    }
    return false;
}

void solve(){
    memset(E, -1, sizeof(E));
    edgesum = -1;
    for(int i=0; i<NA; ++i){
        for(int j=0; j<NB; ++j){
            if(end_a[i] + T <= start_b[j]){
                addedge(i, NA+NB+NA+j);
            }else if(end_b[j] + T <= start_a[i]){
                addedge(NA+j, NA+NB+i);
            }
        }
    }
    memset(linky, -1, sizeof(linky));
    for(int i=0; i<NA+NB; ++i){
        memset(vist, false, sizeof(vist));
        find(i);
    }
    int res_a=0,res_b=0;
    for(int i=0; i<NA; ++i)if(linky[NA+NB+i] == -1)++res_a;
    for(int i=0; i<NB; ++i)if(linky[NA+NB+NA+i] == -1)++res_b;
    printf("%d %d\n", res_a, res_b);
}

int main(){
    int N;
    scanf("%d", &N);
    for(int i=1; i<=N; ++i){
        init();
        printf("Case #%d: ", i);
        solve();
    }
}
