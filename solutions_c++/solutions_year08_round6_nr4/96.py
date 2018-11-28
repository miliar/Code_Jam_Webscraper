/*
Nguyen Tran Nam Khanh
microsoft
*/
#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
#include <functional>
#include <cstring>
#include <cmath>
#include <cstdio>

using namespace std;

#define Clear(t) memset((t),0,sizeof(t))
#define For(i,a,b) for (int i=(int)(a),_t = (int)(b);i<=_t;i++)
#define Ford(i,a,b) for (int i=(int)(a), _t = (int)(b);i>=_t;i--)
#define Rep(i,n) for (int i=0, _t = (int)(n);i<_t;i++)
#define tr(it, c) for(typeof(c.begin()) it = c.begin(); it != c.end(); it++)
#define SZ(t) ((int)((t).size()))
#define All(v) (v).begin(),(v).end()
#define Sort(v) sort(All(v))
#define pb push_back

typedef vector<int> VI;
typedef long long ll;
typedef vector<ll> VL;
typedef vector<string> VS;

string i2s(int x) { ostringstream o; o<<x; return o.str(); }
int s2i(string s) { int x; istringstream i(s); i>>x; return x; }

int n, m, a[10];
bool vs[10][10], vs1[10][10];

int main() {
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	
	int st;
	scanf("%d",&st);
	For(ts,1,st) {
        scanf("%d",&n);
        memset(vs,false,sizeof(vs));
        
        For(i,1,n-1) {
            int u,v;
            cin>>u>>v;
            vs[u][v]=true;
            vs[v][u]=true;
        }
        
        For(i,1,n) a[i]=i;
        
        cin>>m;
        memset(vs1,false,sizeof(vs1));
        For(i,1,m-1) {
            int u, v;
            cin>>u>>v;
            vs1[u][v]=vs1[v][u]=true;
        }
        
        bool can = false;
        do {
            bool ok = true;
            For(i,1,m) For(j,1,m) if (vs1[i][j] != vs[a[i]][a[j]]) {
                ok = false;
                break;
            }
            if (ok) {
                can = true;
                break;
            }
        } while (next_permutation(a+1,a+n+1));
        
        if (can) {
            printf("Case #%d: YES\n",ts);
        } else             printf("Case #%d: NO\n",ts);
    }

	return 0;
}
