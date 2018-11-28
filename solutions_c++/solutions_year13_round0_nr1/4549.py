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

string s[4];

bool checkrow(int r, char c) {
	Rep(i,4) if (s[r][i] != c && s[r][i] != 'T') return false;
	return true;
}

bool checkcolumn(int c, char cc) {
	Rep(i,4) if (s[i][c] != cc && s[i][c] != 'T') return false;
	return true;
}

bool checkdiagonal(char c) {
	bool ok = true;
	Rep(i,4) if (s[i][i] != c && s[i][i] != 'T') ok = false;
	if (ok) return true;
	Rep(i,4) if (s[i][3-i] != c && s[i][3-i] != 'T') return false;
	return true;
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int st;
	cin>>st;
	
	For(ts,1,st) {

		Rep(i,4) cin>>s[i];
		
		int cnt = 0;
		Rep(i,4) Rep(j,4) if (s[i][j]=='.') cnt++;
		
		bool Xwin = false;
		Rep(r,4) if (checkrow(r, 'X')) Xwin = true;
		Rep(c,4) if (checkcolumn(c, 'X')) Xwin = true;
		if (checkdiagonal('X')) Xwin = true;
		
		bool Owin = false;
		Rep(r,4) if (checkrow(r, 'O')) Owin = true;
		Rep(c,4) if (checkcolumn(c, 'O')) Owin = true;
		if (checkdiagonal('O')) Owin = true;		
		
		if (Xwin) {
			cout<<"Case #"<<ts<<": X won"<<endl;
			continue;
		}
		if (Owin) {
			cout<<"Case #"<<ts<<": O won"<<endl;
			continue;
		}
		
		if (cnt == 0) {
			cout<<"Case #"<<ts<<": Draw"<<endl;
			continue;
		}
		
		cout<<"Case #"<<ts<<": Game has not completed"<<endl;
	}

	return 0;
}
