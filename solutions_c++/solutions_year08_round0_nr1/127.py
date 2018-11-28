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
#define vc 100000

typedef vector<int> VI;
typedef long long ll;
typedef vector<ll> VL;
typedef vector<string> VS;

string i2s(int x) { ostringstream o; o<<x; return o.str(); }
int s2i(string s) { int x; istringstream i(s); i>>x; return x; }

int n, m, qe[1111], s[1111][111];
string en[111];

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int st;
	cin>>st;
	For(ts,1,st) {
		cin>>n;
		string tmp;
		getline(cin,tmp);
		For(i,1,n) {
			getline(cin, en[i]);
		}
		cin>>m;
		getline(cin,tmp);
		For(i,1,m) {
			getline(cin,tmp);
			For(j,1,n) if (en[j]==tmp) {
				qe[i]=j;
				break;
			}
		}
		For(i,1,m) For(j,1,n) s[i][j]=vc;
		For(j,1,n) if (j!=qe[1]) s[1][j]=0;
		
		For(i,2,m) For(j,1,n) if (j!=qe[i]) {
			For(k,1,n) if (k!=j) s[i][j]=min(s[i][j], s[i-1][k]+1);
			else s[i][j]=min(s[i][j], s[i-1][k]);
		}
		
		int res = vc;
		For(j,1,n) res = min(res, s[m][j]);
		cout<<"Case #"<<ts<<": "<<res<<endl;
	}

	return 0;
}
