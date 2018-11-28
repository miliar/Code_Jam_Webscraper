#include <iostream>
#include <cstdio>
#include <iomanip>
#include <algorithm>
using namespace std;

char buf[502][502];
long long dx[501][501], dy[501][501];
long long vx[501][501], vy[501][501];
long long ms[501][501];
long long m[501][501];

void solve(){
     int r, c, d;
     cin>>r>>c>>d;
     for (int i=1; i<=r; ++i)
         cin>>&buf[i][1];
     for (int i=1; i<=r; ++i)
         for (int j=1; j<=c; ++j){
             vx[i][j]=i*(d+(int)(buf[i][j]-'0'));
             vy[i][j]=j*(d+(int)(buf[i][j]-'0'));
             ms[i][j]=d+(int)(buf[i][j]-'0');
             dx[i][j]=dx[i-1][j]+dx[i][j-1]-dx[i-1][j-1]+vx[i][j];
             dy[i][j]=dy[i-1][j]+dy[i][j-1]-dy[i-1][j-1]+vy[i][j];
             m[i][j]=m[i-1][j]+m[i][j-1]-m[i-1][j-1]+ms[i][j];
         }
     for (int k=min(r, c); k>2; --k){
         for (int i=1; i+k-1<=r; ++i)
             for (int j=1; j+k-1<=c; ++j){
                 long long sumx=dx[i+k-1][j+k-1]-dx[i-1][j+k-1]-dx[i+k-1][j-1]
                 +dx[i-1][j-1]-vx[i][j]-vx[i+k-1][j]-vx[i][j+k-1]-vx[i+k-1][j+k-1];
                 long long sumy=dy[i+k-1][j+k-1]-dy[i-1][j+k-1]-dy[i+k-1][j-1]
                 +dy[i-1][j-1]-vy[i][j]-vy[i+k-1][j]-vy[i][j+k-1]-vy[i+k-1][j+k-1];
                 long long mo=m[i+k-1][j+k-1]-m[i-1][j+k-1]-m[i+k-1][j-1]
                 +m[i-1][j-1]-ms[i][j]-ms[i+k-1][j]-ms[i][j+k-1]-ms[i+k-1][j+k-1];
                 if (2*sumx==mo*(long long)(2*i+k-1) && 2*sumy==mo*(long long)(2*j+k-1)){
                    cout<<k;
                    return;
                 }
             }
     }
     cout<<"IMPOSSIBLE";
}

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int t;
    cin>>t;
    for (int i=0; i<t; ++i){
        cout<<"Case #"<<i+1<<": ";
        solve();
        cout<<endl;
    }
}
