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

int L, m, n, t[20];
char a[5555][20], s[1000];

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	scanf("%d%d%d",&L,&m,&n);
	
	Rep(i,m) scanf("%s",&a[i]);
	
	For(ts,1,n) {
		scanf("%s",&s);
		int l = strlen(s);
		int vt = 0;
		Rep(i,L) {
			t[i]=0;
			if (s[vt]=='(') {
				vt++;
				while (s[vt]!=')') {
					int c = s[vt]-'a';
					t[i]|=(1<<c);
					vt++;
				}
				vt++;
			} else {
				int c = s[vt]-'a';
				t[i]|=(1<<c);
				vt++;
			}
		}
		
		int res = 0;
		
		Rep(i,m) {
			bool ok = true;
			Rep(j,L) {
				int c = a[i][j]-'a';
				if (((t[j]>>c)&1)==0) {
					ok = false;
					break;
				}
			}
			if (ok) res++;
		}
		
		printf("Case #%d: %d\n",ts,res);
	}

	return 0;
}
