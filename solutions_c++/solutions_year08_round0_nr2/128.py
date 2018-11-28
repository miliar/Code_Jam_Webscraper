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

int m,n,mn,sa[111],ta[111],sb[111],tb[111],res[2], t;
bool vs[222];
pair< pair<int,int>, int> a[222];

int convert(string a) {
	int h = s2i(a.substr(0,2));
	int m = s2i(a.substr(3,2));
	
	return h*60+m;
}

int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	int st;
	cin>>st;
	For(ts,1,st) {
		cin>>t;
		cin>>m>>n;
		For(i,1,m) {
			string x,y;
			cin>>x>>y;
			sa[i]=convert(x);
			ta[i]=convert(y);
		}
		For(i,1,n) {
			string x,y;
			cin>>x>>y;
			sb[i]=convert(x);
			tb[i]=convert(y);
		}
		
		mn = 0;
		For(i,1,m) a[mn++]=make_pair(make_pair(sa[i],ta[i]), 0);
		For(i,1,n) a[mn++]=make_pair(make_pair(sb[i],tb[i]), 1);
		sort(a,a+mn);
		
		res[0]=res[1]=0;
		memset(vs,false,sizeof(vs));
		
		Rep(i,mn) if (!vs[i]) {
			res[a[i].second]++;
			vs[i]=true;
			int tg = a[i].first.second;
			int loai = a[i].second;
			
			For(j,i+1,mn-1) if (!vs[j] && a[j].first.first>=tg+t && a[j].second!=loai) {
				loai = a[j].second;
				vs[j]=true;
				tg = a[j].first.second;
			}
		}
		
		cout<<"Case #"<<ts<<": "<<res[0]<<" "<<res[1]<<endl;
	}

	return 0;
}
