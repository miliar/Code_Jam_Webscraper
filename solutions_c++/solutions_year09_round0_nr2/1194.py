#include <iostream>
#include <algorithm>
#include <map>
#include <queue>

#define ii pair<long,long>
#define MP make_pair

using namespace std; 

long m,n,h[111][111],di[4]={-1,0,0,1},dj[4]={0,-1,1,0};
char a[111][111];
map< ii,ii > M;
queue< ii > q;

void inp() {
    cin>> m >> n;
    
    for(long j=0; j<=n+1; j++) {
        h[0][j]=1000111;
        h[m+1][j]=1000111;
    }
    for(long i=0; i<=m+1; i++) {
        h[i][0]=1000111;
        h[i][n+1]=1000111;
    }
    
    for(long i=1; i<=m; i++)
    for(long j=1; j<=n; j++)
        cin>> h[i][j];
        
}

void init() {
    M.clear();
    for(long i=1; i<=m; i++)
    for(long j=1; j<=n; j++) {
        M[MP(i,j)]=MP(0,0);
        for(long dir=0; dir<4; dir++) {
            long u=i+di[dir], v=j+dj[dir];
            if (h[u][v]<h[i][j])
                if (h[M[MP(i,j)].first][M[MP(i,j)].second]>h[u][v])
                    M[MP(i,j)]=MP(u,v);
        }
    } //Khoi tao M
}

void solve() {
    memset(a,0,sizeof a);
    char now='a';
    for(long i=1; i<=m; i++)
    for(long j=1; j<=n; j++) 
    if ((long)a[i][j]==0) {
        ii u; u.first=i; u.second=j;
        while (M[u].first!=0) 
            u=M[u];
            
        while (!q.empty()) q.pop();
        q.push(u);
        a[u.first][u.second]=now;
        while (!q.empty()) {
            u=q.front(); q.pop();
            for(long di=-1; di<=1; di+=1)
            for(long dj=-1; dj<=1; dj+=1) 
            if (di*di+dj*dj==1) {
                ii v; v.first=u.first+di; v.second=u.second+dj;
                if (M.find(v)!=M.end() && M[v]==u && a[v.first][v.second]==0) { 
                    a[v.first][v.second]=now;
                    q.push(v); 
                }
            } //for di dj
        } //while (!q.empty()
        now++;
    } //for i j
}

void ans() {
    for(long i=1; i<=m; i++) {
        for(long j=1; j<=n; j++) cout<<a[i][j]<<" ";
        cout<<endl;
    }
}

int main() {
//    freopen("b-small-attempt0.in","r",stdin);
    freopen("b-large.in","r",stdin);
    freopen("b.out","w",stdout);

    long test;    
    cin>>test;
    while (test--) {
        inp();
        init();
        solve();
        cout<<"Case #"<<100-test<<":\n";
        ans();
    }
    return 0;
}
