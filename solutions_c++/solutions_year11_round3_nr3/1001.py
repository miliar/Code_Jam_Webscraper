#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
//#define ONLINE_JUDGE
#define PB push_back
#define MP make_pair
#define CLR(x,y) memset((x),y,sizeof(x))
#define rep(i,n) for(int i=0; i<(n); i++)
#define forr(i,a,b) for(int i=(a);i<=(b);i++)
typedef long long i64;
const int N = 10001;
int prime[10001],pn;
bool mark[10002];

i64 GCD(i64 x,i64 y) {
    if(y==0) return x;
    else return GCD(y,x%y);   
}

void init() {
    CLR(mark,0);
    pn=0;
    for(int i=2; i<=N; i++) {
        if(!mark[i]) prime[pn++]=i;
        for(int j=0; j<pn&&prime[j]*i<=N; j++) {
            mark[prime[j]*i]=1;
            if(i%prime[j]==0) break;   
        }   
    }
}

int main() {
    #ifndef ONLINE_JUDGE
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small.out", "w", stdout);
    #endif

    init();
    
    int tt, cas = 1;
    scanf("%d", &tt);
    for(cas=1; cas<=tt; cas++) {
        //To-Do
        int n,L,H,x;
        scanf("%d%d%d",&n,&L,&H);
        vector<int> vv, pp,all;
        rep(i,n) {
            scanf("%d",&x);
            if(x==1) continue;
            if(!mark[x]) pp.PB(x);
            else vv.PB(x);
            all.PB(x);
        }       
        printf("Case #%d: ",cas); 
        if(L<=1&&1<=H) {
            printf("%d\n",1);
            continue;
        }
        
        i64 lcm=1LL;
        bool trunc=false;
        rep(i,pp.size()) {
            lcm=(i64)lcm*pp[i]/GCD(lcm,pp[i]);
            if(lcm>H) {
                trunc=true;
                break;   
            }
        }
        if(trunc) {
            printf("NO\n");
            continue;   
        }
        int tmp=lcm;
        while(lcm<L) lcm+=tmp;
        if(lcm>H) {
            printf("NO\n");
            continue;
        }
        bool fin=false;
        while(!fin) {
            fin=true;
            rep(i,vv.size()) {
                if(lcm%vv[i]!=0&&vv[i]%lcm!=0) {
                    fin=false;
                    break;
                }
            }   
            if(fin) break;
            lcm+=tmp;
            if(lcm>H) break;
        }
        if(fin) printf("%d\n",lcm);
        else printf("NO\n");
    }
    //system("pause");
    return 0;
}
