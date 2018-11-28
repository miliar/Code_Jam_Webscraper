#include<cstdio>
#include<iostream>

using namespace std;

typedef long long ll;

int T,i,I=0;
ll L;
int n,b[200],now,l,r,x,nx,ncost;
bool bt[200000];
int Q[10000000];
int opt[200000];

int main(){
    cin >> T;
    while (T--){
        cin >> L >> n;
        for (i=0;i<n;++i) cin >> b[i];
        sort(b,b+n);
        cout << "Case #" << ++I <<": ";
        now=b[n-1];
        for (i=0;i<now;++i) opt[i]=-1,bt[i]=0;
        opt[0]=0;
        l=0;r=0;
        Q[r++]=0;
        while (l<r){
            x=Q[l++];
            bt[x]=0;
            for (i=0;i<n;++i){
                nx=x+b[i];
                ncost=opt[x]+1;
                if (nx>=now) nx-=now,ncost--;
                if (opt[nx]==-1 || opt[nx]>ncost){
                    opt[nx]=ncost;
                    if (!bt[nx]){
                        bt[nx]=1;
                        Q[r++]=nx;
                    }
                }
            }
        }
        if (opt[L%now]==-1) cout << "IMPOSSIBLE" << endl;
        else cout << L/now+opt[L%now] << endl;
    }
}
