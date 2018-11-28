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

#define M 111
#define N 25

int a[M][N];
bool ok[M][M];
queue<int> q;
int pre[M], x[M], y[M], m, n;

int findPath() {
	while (!q.empty()) q.pop();
	memset(pre,-1,sizeof(pre));
	for (int i = 0; i<m; i++) if (x[i]<0) q.push(i);
	
	while (!q.empty()) {
	    int i = q.front(); q.pop();
	    for (int j = 0; j<m; j++) if (ok[i][j] && pre[j]<0) {
	        pre[j]=i;
	        if (y[j]<0) {
	           return j;
	        }

	        q.push(y[j]);
	    }
	}

    return -1;
}

void tang(int j) {
     int i = pre[j];
     int k = x[i];
     y[j]=i;
     x[i]=j;
     if (k>=0) tang(k);
}

int CapGhep() {
     for (int i = 0; i<m; i++) x[i] = -1;
     for (int j = 0; j<m; j++) y[j] = -1;

     int sl=0;
	 while (true) {
			int i = findPath();
			if (i<0) break;
			sl++;
			tang(i);
		}

     return sl;
}

int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	
	int st;
	scanf("%d",&st);
	For(ts,1,st) {
		scanf("%d%d",&m,&n);
		Rep(i,m) Rep(j,n) scanf("%d",&a[i][j]);

		Rep(i,m) Rep(j,m) {
			ok[i][j] = true;
			Rep(k,n) if (a[i][k]>=a[j][k]) ok[i][j] = false;
		}
		
		int res = m-CapGhep();
				
		printf("Case #%d: %d\n",ts,res);
	}

	return 0;
}
