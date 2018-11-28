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

int x2[51][51][2600], y2[51][51][2600], x3[51][51][2600], y3[51][51][2600];
int m,n, a;

void tinh(int ts) {
    	For(i,1,m) For(j,1,n) if (x2[i][j][a]!=0 || y2[i][j][a]!=0 || x3[i][j][a]!=0 || y3[i][j][a]!=0) {
            cout<<"Case #"<<ts<<": "<<0<<' '<<0<<' '<<x2[i][j][a]<<' '<<y2[i][j][a]<<' '<<x3[i][j][a]<<' '<<y3[i][j][a]<<endl;
			return;
		}
		cout<<"Case #"<<ts<<": IMPOSSIBLE"<<endl;
}

int main() {
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	
	
	Clear(x2);
	Clear(y2);
	Clear(x3);
	Clear(y3);
	int i1 = 0, j1 = 0;
	Rep(i2,51) Rep(j2,51) Rep(i3,51) Rep(j3,51) {
		int dt = (i2-i1)*(j2+j1);
		dt+=(i3-i2)*(j3+j2);
		dt+=(i1-i3)*(j1+j3);
		dt = abs(dt);
		int mm = max(i2,i3);
		int nn = max(j2,j3);
		x2[mm][nn][dt]=i2;
		y2[mm][nn][dt]=j2;
		x3[mm][nn][dt]=i3;
		y3[mm][nn][dt]=j3;
	}
	int st;
	cin>>st;
	For(ts,1,st) {
		cin>>m>>n>>a;
		
		if (a>m*n) {
			cout<<"Case #"<<ts<<": IMPOSSIBLE"<<endl;
			continue;
		}
		tinh(ts);
	}

	return 0;
}
