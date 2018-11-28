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

int kq[11] = {
151,
855,
527,
743,
351,
135,
407,
903,
791,
135,
647};
int main() {
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	
	int st;
	cin>>st;
	For(ts,1,st) {
		int n;
		cin>>n;
		long double t = 5;
		t = sqrt(t);
		t+=3.0;
		long double x = 1;
		Rep(i,n) x*=t;
		long long tmp = (long long)trunc(x);
		int res = tmp%1000;
		string xx = i2s(res);
		while (SZ(xx)<3) xx="0"+xx;
		if (n>=20) xx = i2s(kq[n-20]);
		cout<<"Case #"<<ts<<": "<<xx<<endl;
	}

	return 0;
}
