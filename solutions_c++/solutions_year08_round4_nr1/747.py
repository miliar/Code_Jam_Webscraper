#include <iostream>
#include <fstream>

#pragma optimize("O2",on)
using namespace std;

const int SIZE=11000;
const int inf=1000000;
int G[SIZE],c[SIZE];
int f[SIZE][2];
int m,v;

void dfs(int pos) {
    if (pos>(m-1)/2) return;
    dfs(2*pos); dfs(2*pos+1);
    int A,B,C,D,add=2*inf;
    A=min(inf,f[2*pos][1]+f[2*pos+1][1]);
    B=min(min(inf,f[2*pos][0]+f[2*pos+1][1]),min(f[2*pos][0]+f[2*pos+1][0],f[2*pos][1]+f[2*pos+1][0]));
    C=min(min(inf,f[2*pos][1]+f[2*pos+1][1]),min(f[2*pos][0]+f[2*pos+1][1],f[2*pos][1]+f[2*pos+1][0]));
    D=min(inf,f[2*pos][0]+f[2*pos+1][0]);
    if (c[pos]==1) add=1;
    if (G[pos]==1){
        f[pos][1]=min(A,C+add);
        f[pos][0]=min(B,D+add);
    } else {
        f[pos][1]=min(C,A+add);
        f[pos][0]=min(D,B+add);
    }
};

int main() {
#ifndef ONLINE_JUDGE
	ifstream cin("A-large.in");
    ofstream cout("A-large.out");
#endif
    int T; cin>>T;
    for (int o=1; o<=T; o++) {
        cin>>m>>v;
        for (int i=1; i<=m; i++)
            f[i][0]=f[i][1]=inf;
        memset(c,0,sizeof c);
        for (int i=1; i<=(m-1)/2; i++)
            cin>>G[i]>>c[i];
        for (int i=(m-1)/2+1; i<=m; i++) {
            int x; cin>>x;
            f[i][x]=0; f[i][1-x]=inf;
        }
        dfs(1);
        if (f[1][v]!=inf)
            cout<<"Case #"<<o<<": "<<f[1][v]<<endl;
        else
            cout<<"Case #"<<o<<": "<<"IMPOSSIBLE"<<endl;
    }
	return 0;
}