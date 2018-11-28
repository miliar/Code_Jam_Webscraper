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

set<int> s;
bool happy(int a, int b) {
	s.clear();
	if (a==1) return true;
	while (true) {
		int ss = 0, aa = a;
		while (aa>0) {
			int kt = aa%b;
			ss+=(kt*kt);
			aa/=b;
		}
		
		if (ss==1) return true;
		if (s.find(ss)!=s.end()) break;
		a = ss;
		s.insert(a);
	}
	return false;
}

int res[600000], n;

int main() {
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);

	int M = 569669;
	memset(res,0,sizeof(res));	
	For(x,2,M) {
		int t = 0;		
		For(b,2,10) if (happy(x,b)) {
			t|=(1<<(b-2));
		}
		
		if (res[t]==0) res[t]=x;
	}

	int st;
	scanf("%d",&st);
	char line[100];
	gets(line);
	For(ts,1,st) {
		gets(line);
		istringstream fi((string)line);
		int x = 0;
		int b;
		while (fi>>b) {
			x|=(1<<(b-2));
		}
		
		int ret = M+1;
		Rep(t,1<<9) if (res[t]>0 && t>=x && x==(t&x)){
			ret<?=res[t];
		}
		
		printf("Case #%d: %d\n",ts, ret);
	}

	return 0;
}
