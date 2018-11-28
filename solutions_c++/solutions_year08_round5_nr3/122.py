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

int m, n;
int s[12][1111], sb[1111];
string a[12];


bool ok(int x) {
	Rep(i,n-1) if (((x>>i)&1) && ((x>>(i+1))&1)) return false;
	return true;
}

bool ok2(int x, int y) {
	Rep(i,n-1) {
        if (((x>>i)&1) && ((y>>(i+1))&1)) return false;
        if (((y>>i)&1) && ((x>>(i+1))&1)) return false;
	}
	return true;
}

bool ok3(int h, int x) {
	Rep(i,n) if (a[h][i]=='x' && ((x>>i)&1)) return false;
	return true;
}

int sobit(int x) {
	int ret = 0;
	Rep(i,n) if ((x>>i)&1) ret++;
	return ret;
}


int main() {
	freopen("C-small-attempt2.in","r",stdin);
	freopen("C-small-attempt2.out","w",stdout);
	
	int st;
	cin>>st;
	For(ts,1,st) {
		cin>>m>>n;
		memset(sb,0,sizeof(sb));
		Rep(i,1<<n) sb[i]=sobit(i);
		Rep(i,m) cin>>a[i];
		Rep(i,m) Rep(j,1<<n) s[i][j]=-10000;
		Rep(i,1<<n) if (ok(i) && ok3(0,i)) s[0][i]=sb[i];
		For(i,1,m-1) Rep(x,1<<n) if (ok(x) && ok3(i,x)) {
			Rep(y,1<<n) if (s[i-1][y]>=0 && ok2(x,y)) s[i][x]=max(s[i][x], s[i-1][y]+sb[x]);
		}
		int res = 0;
		Rep(i,1<<n) res = max(res, s[m-1][i]);
		cout<<"Case #"<<ts<<": "<<res<<endl;
	}

	return 0;
}
