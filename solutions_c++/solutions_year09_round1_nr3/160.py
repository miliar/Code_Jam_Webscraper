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

int n, c;
double s[11111][44];
ll t[44][44];

int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	
	memset(t,0,sizeof(t));
	t[0][0]=1;
	For(i,1,40) {
		t[i][0]=1;
		For(j,1,i) t[i][j]=t[i-1][j]+t[i-1][j-1];
	}
	
	int st;
	scanf("%d",&st);
	For(ts,1,st) {
		scanf("%d%d",&c,&n);

		memset(s,0,sizeof(s));
		s[0][0]=1;		
		double res = 0;
		For(i,0,10000) {
			For(j,0,c-1) if (s[i][j]>=1e-9) {
				For(k,0,c-j) if (j>=n-k) {
					double tmp = t[c-j][k];
					tmp/=t[c][n];
					tmp*=t[j][n-k];
					
					s[i+1][j+k]+=s[i][j]*tmp;
				}
			}
			res+=s[i][c]*i;
		}
		
		printf("Case #%d: %.7f\n",ts,res);		
	}

	return 0;
}
