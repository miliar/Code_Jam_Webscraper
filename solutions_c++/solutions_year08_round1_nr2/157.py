#include <iostream>
#include <cstdio>
#include <set>
using namespace std;
#define  For(i,a,b) for(int i=a; i<=b; i++)
#define Ford(i,a,b) for(int i=a; i>=b; i--)
#define fillchar(a) memset(a, 0, sizeof(a))
#define maxn 2002
#define maxm 3003

int a[maxm][maxn],  q[maxm], tt[maxn], dem[maxm];
int n,m;

int xuly(){
    int lst=0;
    For(i,1,m) if (!dem[i]) q[++lst]=i;
    int fst=1, u;
    while (fst<=lst){
        u=q[fst++];
        For(i,1,n) if (a[u][i]==2) {
            if (tt[i]) break;
            tt[i]=1;
            For(v,1,m) if (a[v][i]==1) {
                dem[v]--;
                if (dem[v]==0) q[++lst]=v;
            }
        }
    }
    For(u,1,m) {
        int tm=0;
        For(i,1,n) if (a[u][i]==tt[i]+1) {tm++;break;}
        if (!tm) return 1;
    }
    return 0;
}

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out","w", stdout);
    int ntest, k, h, t;
    cin>>ntest;
    For(test,1,ntest){
        fillchar(dem);
        fillchar(tt);
        fillchar(a);
        cin>>n;
        cin>>m;
        For(i,1,m){
            cin>>t;
            For(j,1,t){
                cin>>k>>h;
                a[i][k]=h+1;
                dem[i]+=(1-h);
            }
        }
        cout<<"Case #"<<test<<":";
        if (xuly()) cout<<" IMPOSSIBLE"<<endl; 
        else {
            For(i,1,n) cout<<" "<<tt[i];
            cout<<endl;
        }
    }    
    return 0;
}
