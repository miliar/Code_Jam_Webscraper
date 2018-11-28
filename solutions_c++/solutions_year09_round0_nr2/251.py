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

#define N 111

int dx[4] = {-1,0,0,1};
int dy[4] = {0,-1,1,0};
int tt[4] = {3,2,1,0};

int a[N][N], m, n, vs[N][N], t[N][N];

void dfs(int x, int y, int tp) {
	vs[x][y]=tp;
	Rep(k,4) if ((t[x][y]>>k)&1) {
		int i = x+dx[k], j = y+dy[k];
		if (vs[i][j]<0) dfs(i,j,tp);
	}
}

int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	int st;
	scanf("%d",&st);
	For(ts,1,st) {
		scanf("%d%d",&m,&n);
		For(i,1,m) For(j,1,n) scanf("%d",&a[i][j]);
		
		memset(t,0,sizeof(t));
		
		For(i,0,m+1) a[i][0]=a[i][n+1]=10000000;
		For(j,0,n+1) a[0][j]=a[m+1][j]=10000000;
		
		For(i,1,m) For(j,1,n) {
			int cur = 10000000;
			int vt = -1;
			Rep(k,4) {
				int x = i+dx[k], y = j+dy[k];
				
				if (a[x][y]<cur) {
					cur = a[x][y];
					vt = k;
				}
			}
			
			if (cur<a[i][j]) {
				int x = i+dx[vt], y = j+dy[vt];
				//cout<<i<<' '<<j<<' '<<x<<' '<<y<<endl;
				t[i][j]|=(1<<vt);
				t[x][y]|=(1<<tt[vt]);
			}
		}
		
		memset(vs,-1,sizeof(vs));
		
		int stp = 0;
		For(i,1,m) For(j,1,n) if (vs[i][j]<0) {
			dfs(i,j,stp);
			stp++;
		}
		
		printf("Case #%d:\n",ts);
		For(i,1,m) {
			For(j,1,n-1) printf("%c ",'a'+vs[i][j]);
			printf("%c\n",'a'+vs[i][n]);
		}
	}

	return 0;
}
