#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <string>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cctype>

using namespace std;
typedef long long int64;
const int inf = 0x3f3f3f3f;
typedef double real;
const real eps = 1e-6;
typedef pair<int,int> pip;
#define Eo(x) { cerr << #x << " = " << (x) << endl; }

const int maxn = 410;
vector<int> g[maxn];
int gg[maxn];
int d[2][maxn];
int q[maxn];
char was[maxn],w2[maxn];

void mark(int v, int dist[maxn]){
    memset(dist,0x3f,sizeof(int)*maxn);
    int ba = 0;
    int fr = 0;
    q[fr++] = v;
    dist[v] = 0;
    for (;ba<fr;){
        int v = q[ba++];
        for (int i = 0; i < g[v].size(); i++){
            int p = g[v][i];
            if (dist[p]>dist[v]+1){
                dist[p]=dist[v]+1;
                q[fr++]=p;
            }
        }
    }
}

int calc(int n){
    memset(w2,0,sizeof(char)*n);
    for (int i = 0; i < n; i++) if (was[i]){
        for (int j = 0; j < g[i].size(); j++){
            int p = g[i][j];
            w2[p]=1;
        }
    }
    int r = 0;
    for (int i = 0; i < n; i++)  if (w2[i]){
        if (!was[i]){
            r++;
        }
    }
    return r;
}

int mx;
void go(int v, int n){
    if (v==1){
        mx = max(mx,calc(n));
        return;
    }
    was[v]=1;
    for (int i = 0; i < g[v].size(); i++){
        int p = g[v][i];
        if (!gg[p])continue;
        if (d[0][p]!=d[0][v]+1)continue;
        go(p,n);
    }
    was[v]=0;
}

int main(){
    int T; cin >> T;
    for (int _ = 0; _ < T; _++){
        printf("Case #%d: ",_+1);
        int n,m ;cin >> n >> m;
        for (int i = 0; i < m; i++){
            int x,y; scanf("%d,%d",&x,&y);
            g[x].push_back(y);
            g[y].push_back(x);
        //    Eo(x);Eo(y);
        }
        mark(0,d[0]);
        mark(1,d[1]);
        int z = d[0][1];
        memset(gg,0,sizeof(gg));
        memset(was,0,sizeof(was));
//        Eo(d[0][1]);Eo(d[1][0]);
        for (int i = 0; i < n; i++) if (d[0][i]+d[1][i]==z){
 //           Eo(i);
            gg[i] = 1;
        }
        mx = -1;
        go(0,n);
        pip zz(d[0][1]-1,mx);
        printf("%d %d\n",zz.first,zz.second);
        for (int i = 0; i < n; i++) g[i].clear();
    }
	return 0;
}

