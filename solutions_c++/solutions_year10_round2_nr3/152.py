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

int n, c[555][555], s[555][555];
#define mod 100003

int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	
	memset(c,0,sizeof(c));
	
	c[0][0]=1;
	For(i,1,500) {
		c[i][0]=1;
		For(j,1,i) c[i][j]=(c[i-1][j-1]+c[i-1][j])%mod;
	}
	
	int st;
	scanf("%d",&st);
	For(ts,1,st) {
		scanf("%d",&n);
		
		memset(s,0,sizeof(s));
		
		For(i,2,n) s[1][i]=1; 
		
		For(i,1,n-1) For(j,i+1,n) if (s[i][j]>0) {
			For(k,j+1,n) if (k-j-1>=j-i-1) {
				long long tmp = s[i][j];
				tmp*=c[k-j-1][j-i-1];
				
				s[j][k]=(tmp+s[j][k])%mod;
			}
		}
		
		int res = 0;
		For(i,1,n-1) res+=s[i][n];
		
		res%=mod;
		printf("Case #%d: %d\n",ts,res);
	}
	

	return 0;
}
