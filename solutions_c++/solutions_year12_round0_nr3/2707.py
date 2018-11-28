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
typedef map<string, int> MSI;

string i2s(int x) { ostringstream o; o<<x; return o.str(); }
int s2i(string s) { int x; istringstream i(s); i>>x; return x; }

MSI cnt;

string ss[2000010];

string smallestRotation(int a) {
	string s = i2s(a);
	string res = s;
	int len = SZ(s);
	Rep(i,len) {
		char c = s[0];
		s = s.substr(1, len - 1);
		s+=c;
		
		if (s < res) res = s;
	}
	return res;
}

int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	
	For(i,1,2000000) ss[i] = smallestRotation(i);
	
	int st;
	cin>>st;
	For(ts, 1, st) {
		cnt.clear();
		
		int a, b;
		cin>>a>>b;
		For(x,a,b) {
			string s = ss[x];
			
			if (cnt.find(s)!=cnt.end()) {
				int tmp = cnt[s] + 1;
				cnt[s] = tmp;
			} else cnt[s] = 1;
		}
		
		ll res = 0;
		for (MSI::iterator it = cnt.begin(); it != cnt.end(); it++) {
			ll cnt = (*it).second;
			res+=((cnt-1)*cnt/2);
		}
		
		cout<<"Case #"<<ts<<": "<<res<<endl;
	}

	return 0;
}
