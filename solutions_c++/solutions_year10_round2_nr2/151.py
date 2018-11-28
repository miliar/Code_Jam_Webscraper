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

#define vc 1000001

int n, m, len, t, x[100], v[100], s[100];
bool ok[100];

int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	int st;
	scanf("%d",&st);
	For(ts,1,st) {
		scanf("%d%d%d%d",&n,&m,&len,&t);
		
		For(i,1,n) scanf("%d",&x[i]);
		For(i,1,n) scanf("%d",&v[i]);
		
		memset(ok,false,sizeof(ok));
		
		For(i,1,n) if (((long long) v[i])*t+x[i]>=len) ok[i]=true;
		
		For(i,1,n) {
			if (!ok[i]) {
				s[i] = vc;
				continue;
			}
			s[i] = 0;
			For(j,i+1,n) if (v[i]>v[j] && !ok[j]) {
				double tt = ((x[j]-x[i])*1.0)/(v[i]-v[j]);
				double vt = x[i]+tt*v[i];
				
				long long vv = v[i]-v[j];
				vv*=(len-x[i]);
				
				long long xx = x[j]-x[i];
				xx*=v[i];
				
				
				//cout<<i<<' '<<j<<' '<<vt<<' '<<tt<<endl;
				
				//if (vt<len) s[i]++;
				if (xx<vv) s[i]++;
			}
		}
		
		sort(s+1,s+n+1);
		if (s[m]>=vc) {
			printf("Case #%d: IMPOSSIBLE\n", ts);
			continue;
		}
		
		int res = 0;
		For(i,1,m) res+=s[i];
		
		printf("Case #%d: %d\n",ts, res);
	}

	return 0;
}
