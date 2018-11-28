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
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int st;
	scanf("%d",&st);
	For(ts,1,st) {
		int n;
		int a[44];
		scanf("%d",&n);
		Rep(i,n) {
			char tmp[44];
			scanf("%s",&tmp);
			a[i]=-1;
			Rep(j,n) if (tmp[j]=='1') a[i]=j;
		}
		
		int res = 0;
		Rep(i,n) if (a[i]>i) {
			int vt = i;
			For(j,i+1,n-1) if (a[j]<=i) {
				vt = j;
				break;
			}
			Ford(j,vt,i+1) {
				swap(a[j],a[j-1]);
				res++;
			}
		}
		
		printf("Case #%d: %d\n",ts,res);
	}

	return 0;
}
