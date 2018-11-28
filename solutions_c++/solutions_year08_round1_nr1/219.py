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

int n;
ll x[1000], y[1000];
bool xx[1000], yy[1000];

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int st;
	cin>>st;
	For(ts,1,st) {
		cin>>n;
		Rep(i,n) cin>>x[i];
		Rep(i,n) cin>>y[i];
		
		sort(x,x+n);
		sort(y,y+n);

		ll res = 0;
		memset(xx,false,sizeof(xx));
		memset(yy,false,sizeof(yy));
		
		Ford(i,0,n-1) if (x[i]<0 && !xx[i]) {
			bool ok = false;
			Ford(j,n-1,0) if (y[j]>0 && !yy[j]) {
				ok = true;
				res+=x[i]*y[j];
				xx[i]=true;
				yy[j]=true;
				break;
			}
			if (!ok) break;
		}
		Ford(j,0,n-1) if (y[j]<0 && !yy[j]) {
			bool ok = false;
			Ford(i,n-1,0) if (x[i]>0 && !xx[i]) {
				ok = true;
				res+=x[i]*y[j];
				xx[i]=true;
				yy[j]=true;
				break;
			}
			if (!ok) break;
		}
		
		Rep(i,n) if (!xx[i]) {
			Ford(j,n-1,0) if (!yy[j]) {
				res+=x[i]*y[j];
				xx[i]=true;
				yy[j]=true;
				break;
			}
		}
		
		cout<<"Case #"<<ts<<": "<<res<<endl;
	}

	return 0;
}
