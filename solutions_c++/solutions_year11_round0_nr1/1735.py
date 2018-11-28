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

int n, p[111], c[111];

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int st;
	cin>>st;
	
	For(ts,1,st) {
		memset(c,0,sizeof(c));
		cin>>n;
		For(i,1,n) {
			string cc;
			cin>>cc;
			cin>>p[i];
			if (cc=="O") c[i]=0;
			else c[i]=1;
		}
		
		int res = 0;
		int pa = 1, pb = 1;
		For(i,1,n) if (c[i]==0){
			int nb = -1;
			For(j,i+1,n) if (c[j]==1) {
				nb = p[j];
				break;
			}
			
			int dis = abs(p[i]-pa)+1;
			res+=dis;
			pa = p[i];
			
			if (dis>=abs(nb-pb)) pb = nb;
			else {
				if (nb>pb) pb+=dis;
				else pb-=dis;
			}
		} else {
			int na = -1;
			For(j,i+1,n) if (c[j]==0) {
				na = p[j];
				break;
			}
			
			int dis = abs(p[i]-pb)+1;
			res+=dis;
			pb = p[i];
			
			if (dis>=abs(na-pa)) pa = na;
			else {
				if (na>pa) pa+=dis;
				else pa-=dis;
			}			
		}
		
		cout<<"Case #"<<ts<<": "<<res<<endl;
	}

	return 0;
}
