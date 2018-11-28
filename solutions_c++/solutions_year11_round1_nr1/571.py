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

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int st;
	scanf("%d",&st);
	For(ts,1,st) {
		int pd, pg;
		ll n;
		cin>>n>>pd>>pg;
		
		if (pd<100 && pg==100) {
			printf("Case #%d: Broken\n",ts);
			continue;
		}
		
		if (pd>0 && pg==0) {
			printf("Case #%d: Broken\n",ts);
			continue;
		}		
		
		int d = 0;
		For(i,1,(int)min(n,(ll)100)) {
			if ((i*pd)%100==0) {
				d = i;
				break;
			}
		}
		
		if (d==0) printf("Case #%d: Broken\n",ts);
		else printf("Case #%d: Possible\n",ts);
	}
	
	return 0;
}
