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

int n, a[1111], c1[1111], c2[1111], s[1111][11], p[1111];
#define vc 1000000001

int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	int st;
	scanf("%d",&st);
	
	For(ts,1,st) {
		scanf("%d",&n);
		
		Rep(i,1<<n) {
			scanf("%d",&a[i]);
			a[i] = n-a[i];
		}
		
		Rep(i,(1<<n)-1) scanf("%d",&p[i]);
		
		int m = (1<<n)-1;
		
		int nn = (1<<n)/2;
		int vt1 = 0;
		int vt2 = nn;
		Rep(i,n-1) {
			nn/=2;
			Rep(j,nn) {
				c1[vt2]=vt1;
				c2[vt2]=vt1+1;
				vt2++;
				vt1+=2;
			}
		}
		
		Rep(i,m) Rep(j,n+1) s[i][j]=vc;
		
		
		Rep(i,(1<<n)/2) {
			int x = i*2;
			int y = i*2+1;
			
			s[i][max(a[x], a[y])] = 0;
			if (max(a[x], a[y]) > 0) s[i][max(a[x], a[y])-1] = min(s[i][max(a[x], a[y])-1], p[i]);
		}
		
		For(i, (1<<n)/2, m-1) {
			int x = c1[i], y = c2[i];
			
			For(j, 0, n) if (s[x][j]<vc) For(k, 0, n) if (s[y][k]<vc) {
				int jk = max(j,k);
				
				s[i][jk]=min(s[i][jk], s[x][j]+s[y][k]);
				s[i][max(jk-1, 0)] = min(s[i][max(jk-1, 0)], s[x][j]+s[y][k]+p[i]);
			}
		}
		
		
		printf("Case #%d: %d\n",ts, s[m-1][0]);
	}

	return 0;
}
