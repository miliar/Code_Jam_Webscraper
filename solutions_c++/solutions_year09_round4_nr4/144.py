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

int kc2(int x, int y, int xx, int yy) {
	return (x-xx)*(x-xx)+(y-yy)*(y-yy);
}

bool inside(int x, int y, int r, int xx, int yy, int rr) {  //r inside rr
	return (rr>=r && (kc2(x,y,xx,yy)<=(rr-r)*(rr-r)));
}

double bao(int x, int y, int r, int xx, int yy, int rr) {
	return (sqrt(kc2(x,y,xx,yy)) + r + rr)/2;
}

int n, x[44],y[44],r[44];

int main() {
	freopen("D-small-attempt1.in","r",stdin);
	freopen("D-small-attempt1.out","w",stdout);
	
	int st;
	scanf("%d",&st);
	For(ts,1,st) {
		scanf("%d",&n);
		For(i,1,n) scanf("%d%d%d",&x[i],&y[i],&r[i]);
		
		double res = 1e+12;
		if (n<3) {
			res = r[1];
			For(i,2,n) res = max(res, (double)r[i]);
		} else {
				res <?= max((double)r[1],	bao(x[2],y[2],r[2],x[3],y[3],r[3]));
				res <?= max((double)r[2],	bao(x[1],y[1],r[1],x[3],y[3],r[3]));
				res <?= max((double)r[3],	bao(x[2],y[2],r[2],x[1],y[1],r[1]));								
		}
		
		printf("Case #%d: %.6f\n",ts,res);
	}

	return 0;
}
