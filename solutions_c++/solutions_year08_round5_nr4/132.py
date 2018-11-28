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

int s[111][111];
bool a[111][111];
int m, n, sl;

int main() {
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	
	int st;
	cin>>st;
	For(ts,1,st) {
		cin>>m>>n>>sl;
		memset(a,false,sizeof(a));
		while (sl--) {
			int x, y;
			cin>>x>>y;
			a[x][y]=true;
		}
		memset(s,0,sizeof(s));
		s[1][1]=true;
		For(i,1,m) For(j,1,n) if (s[i][j]>0) {
			if (!a[i+1][j+2]) s[i+1][j+2]=(s[i+1][j+2]+s[i][j])%10007;
			if (!a[i+2][j+1]) s[i+2][j+1]=(s[i+2][j+1]+s[i][j])%10007;
		}
		cout<<"Case #"<<ts<<": "<<s[m][n]<<endl;
	}

	return 0;
}
