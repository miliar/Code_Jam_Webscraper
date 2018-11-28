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

int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	
	int st;
	scanf("%d",&st);
	For(ts,1,st) {
		int n;
		int a[1100];
		scanf("%d",&n);
		Rep(i,n) scanf("%d",&a[i]);
		
		int xxx = 0;
		Rep(i,n) xxx^=a[i];
		if (xxx!=0) {
			printf("Case #%d: NO\n",ts);
			continue;
		} 
		
		int res = 0, minv = 1111111;
		
		Rep(i,n) {
			res+=a[i];
			minv=min(minv, a[i]);
		}
		
		res-=minv;
		
		printf("Case #%d: %d\n",ts,res);
	}

	return 0;
}
