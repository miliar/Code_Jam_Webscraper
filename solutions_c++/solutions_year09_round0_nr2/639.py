#include <iostream>
#include <vector>
#include <string>
using namespace std;
//detectar sinks, començar des de ells i anar posant repres des d'on "puc venir"
//al final, començo per dalt a leskerra posant "abcdef.."
//per cada casella, miro si used[repre[i][j]], per fer lletra++

//North, West, East, South.
int dx[4]={-1,0,0,1};
int dy[4]={0,-1,1,0};
int n, m;
int BASE=101;
const int INF = 1000000000;
int used[101*101+5];

int memo[200][200];
int T[200][200];
int repre(int a, int b) {
    int &ans=memo[a][b];
    if (ans>=0) return ans;
    bool sink=1;
    int mn=INF,god=0;
    for (int d=0;d<4;++d) if (a+dx[d]>=0 and a+dx[d]<n and b+dy[d]>=0 and b+dy[d]<m) {
        if (T[a+dx[d]][b+dy[d]]<T[a][b]) sink=0;
        if (T[a+dx[d]][b+dy[d]]<mn) {
            mn=T[a+dx[d]][b+dy[d]];
            god=d;
        }
    }
    if (sink) return ans=BASE*a+b;
    return ans=repre(a+dx[god],b+dy[god]);
}

int main() {
    int t; cin >> t;
    for (int z=1;z<=t;++z) {
        cin >> n >> m;
        for (int i=0;i<n;++i) for (int j=0;j<m;++j) memo[i][j]=-1;
        for (int i=0;i<n;++i) for (int j=0;j<m;++j) cin >> T[i][j];
        repre(0,0);
        for (int i=0;i<n;++i) for (int j=0;j<m;++j) repre(i,j);
        int let=0;
        cout << "Case #"<<z<< ":" << endl;
        for (int i=0;i<101*101+5;++i) used[i]=-1;
        for (int i=0;i<n;++i) {
            for (int j=0;j<m;++j) {
                if (used[memo[i][j]]<0) {
                    used[memo[i][j]]=let;
                    ++let;
                }
                if (j>0) cout << " ";
                cout << char('a'+used[memo[i][j]]);
            }
            cout << endl;
        }
    }
}
