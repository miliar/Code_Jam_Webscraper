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

int n, m, sl[111], a[111][333], b[111][333];

int main() {
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	
	int st;
	cin>>st;
	For(ts,1,st) {
		cin>>n;
		cin>>m;
		Rep(i,m) {
			cin>>sl[i];
			Rep(j,sl[i]) {
				cin>>a[i][j]>>b[i][j];
				a[i][j]--;
			}
		}
		
		int res = n+1;
		int kq = -1;
		Rep(t,1<<n) {
			int malt = 0;
			Rep(i,n) if ((t>>i)&1) malt++;
			bool ok = true;
			Rep(i,m) {
				bool ok1 = false;
				Rep(j,sl[i]) if (((t>>a[i][j])&1)==b[i][j]) {
					ok1 = true;
					break;
				}
				if (!ok1) {
					ok = false;
					break;
				}
			}
			if (ok) if (res>malt) {
				res=malt;
				kq = t;
			}
		}
		if (res>n) {
			cout<<"Case #"<<ts<<": IMPOSSIBLE"<<endl;
		} else {
            cout<<"Case #"<<ts<<":";
            Rep(i,n) if ((kq>>i)&1) cout<<' '<<1;
            else cout<<' '<<0;
            cout<<endl;
		}
	}

	return 0;
}
