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
#define vc 1000000

typedef vector<int> VI;
typedef long long ll;
typedef vector<ll> VL;
typedef vector<string> VS;

string i2s(int x) { ostringstream o; o<<x; return o.str(); }
int s2i(string s) { int x; istringstream i(s); i>>x; return x; }

int m, v, g[11111], c[11111], s0[11111], s1[11111];

void qhd(int i) {
	if (i*2>m) {
		if (g[i]==0) {
			s0[i]=0;
			s1[i]=vc;
		} else {
			s1[i]=0;
			s0[i]=vc;
		}
		return;
	}

	int i1 = i*2;
	int i2 = i1+1;
	qhd(i1);
	qhd(i2);
	if (g[i]==0) { //OR
	    s0[i]=vc;
	    s1[i]=vc;
		s0[i]=min(s0[i], s0[i1]+s0[i2]);
		s1[i]=min(s1[i], s0[i1]+s1[i2]);
		s1[i]=min(s1[i], s1[i1]+s0[i2]);
		s1[i]=min(s1[i], s1[i1]+s1[i2]);
		
		if (c[i]==1) {
			s1[i]=min(s1[i], s1[i1]+s1[i2]+1);
			s0[i]=min(s0[i], s0[i1]+s1[i2]+1);
			s0[i]=min(s0[i], s1[i1]+s0[i2]+1);
			s0[i]=min(s0[i], s0[i1]+s0[i2]+1);
		}
	} else { //AND
	    s0[i]=vc;
	    s1[i]=vc;
		s1[i]=min(s1[i], s1[i1]+s1[i2]);
		s0[i]=min(s0[i], s0[i1]+s1[i2]);
		s0[i]=min(s0[i], s1[i1]+s0[i2]);
		s0[i]=min(s0[i], s0[i1]+s0[i2]);
		
		if (c[i]==1) {
			s0[i]=min(s0[i], s0[i1]+s0[i2]+1);
			s1[i]=min(s1[i], s0[i1]+s1[i2]+1);
			s1[i]=min(s1[i], s1[i1]+s0[i2]+1);
			s1[i]=min(s1[i], s1[i1]+s1[i2]+1);
		}
	}
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int st;
	cin>>st;
	For(ts,1,st) {
		cin>>m>>v;
		Clear(g);
		Clear(c);
		int in = (m-1)/2;
		For(i,1,in) cin>>g[i]>>c[i];
		For(i,in+1,m) cin>>g[i];
		
		qhd(1);
		//For(i,1,m) cout<<i<<' '<<s0[i]<<' '<<s1[i]<<endl;
		int res = 0;
		if (v==1) res = s1[1];
		else res = s0[1];
		string ret;
		if (res>100000) ret = "IMPOSSIBLE";
		else ret = i2s(res);
		cout<<"Case #"<<ts<<": "<<ret<<endl;
	}

	return 0;
}
