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

bool canBestWithoutDiff2(int total, int threshold) {
	int base = total / 3;
	if (total % 3 > 0) return base + 1 >= threshold;
	return base >= threshold;
}

bool canBestWithDiff2(int total, int threshold) {
	int base = total / 3;
	if (total % 3 == 2) return base + 2 >= threshold;
	if (total % 3 == 1) return base + 1 >= threshold;
	if (total > 0) return base + 1>= threshold;
	return base >= threshold;
}

int n, nSurprise, nBest, a[111], s[111][12];

int main() {
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
	
	int st;
	cin>>st;
	For(ts, 1, st) {
		cin>>n>>nSurprise>>nBest;
		For(i,1,n) cin>>a[i];
		
		memset(s,0,sizeof(s));
		
		For(i,1,n) {
			//cout<<canBestWithoutDiff2(a[i], nBest)<<' '<<canBestWithDiff2(a[i], nBest)<<endl;
			For(j,0,nSurprise) {
				s[i][j] = s[i-1][j];
				if (canBestWithoutDiff2(a[i], nBest)) s[i][j] = max(s[i][j], s[i-1][j] + 1);
				if (j > 0 && canBestWithDiff2(a[i], nBest)) s[i][j] = max(s[i][j], s[i-1][j-1] + 1);
			}
		}
		
		cout<<"Case #"<<ts<<": "<<s[n][nSurprise]<<endl;
	}

	return 0;
}
