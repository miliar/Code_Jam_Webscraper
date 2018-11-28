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

int nRound, nSeat, n, g[1111], m, vs[1111], a[2222], s[2222];

int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	
	int st;
	scanf("%d",&st);
	For(ts,1,st) {
		scanf("%d%d%d",&nRound,&nSeat,&n);
		
		Rep(i,n) scanf("%d",&g[i]);
		
		m = 0;
		Rep(i,n) vs[i]=-1;
		
		int cs = 0;
		while (vs[cs]<0) {
			vs[cs]=m;
			a[m]=cs;
			
			int total = 0;
			Rep(i,n) {
				if (total+g[cs]<=nSeat) {
					total+=g[cs];
					cs = (cs+1)%n;
				}
			}
			
			s[m++]=total;
		}
		
		int cir = m-vs[cs];
		long long scir = 0;
		For(i,vs[cs],m-1) scir+=s[i];
		
		long long sinit = 0;
		For(i,0,min(vs[cs]-1, nRound-1)) sinit+=s[i];
		
		if (vs[cs]>=nRound) {
			printf("Case #%d: %lld\n",ts, sinit);
			continue;
		}
		
		long long res = sinit;
		res+=scir*((nRound-vs[cs])/cir);
		
		int sl = (nRound-vs[cs])%cir;
		
		Rep(i,sl) res+=s[vs[cs]+i];
		
		printf("Case #%d: %lld\n",ts,res);
	}

	return 0;
}
