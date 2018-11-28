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
#define mp make_pair

typedef vector<int> VI;
typedef long long ll;
typedef vector<ll> VL;
typedef vector<string> VS;

string i2s(int x) { ostringstream o; o<<x; return o.str(); }
int s2i(string s) { int x; istringstream i(s); i>>x; return x; }

bool a[222][222], b[222][222], n;

int main() {
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	
	int st;
	scanf("%d",&st);
	
	For(ts,1,st) {
		scanf("%d",&n);
		
		int minx = 200, miny = 200, maxx = 0, maxy = 0;
		memset(a,false,sizeof(a));
		Rep(i,n) {
			int x1, x2, y1, y2;
			scanf("%d%d%d%d",&x1, &y1, &x2, &y2);
			For(x,x1,x2) For(y,y1,y2) a[x][y]=true;
			
			minx = min(minx, x1);
			maxx = max(maxx, x2);
			miny = min(miny, y1);
			maxy = max(maxy, y2);
		}
		
		int res = 0;
		while (true) {
			res++;
			
			bool stop = true;
			memset(b,false,sizeof(b));
			For(x,1,200) For(y,1,200) if (a[x][y]) {
				if (a[x-1][y] || a[x][y-1]) b[x][y]=true;
			} else {
				if (a[x-1][y] && a[x][y-1]) b[x][y]=true;
			}
			
			memset(a,false,sizeof(a));
			For(x,1,200) For(y,1,200) if (b[x][y]) {
				a[x][y]=true;
				stop = false;
				if (x==200 || y==200) cout<<"here"<<endl;
			}
			
			if (stop) break;
		}
		
		printf("Case #%d: %d\n",ts, res);
	}

	return 0;
}
