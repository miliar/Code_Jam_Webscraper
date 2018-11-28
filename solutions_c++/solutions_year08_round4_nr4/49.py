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

char s[55000];
int K, begin, inf, ns;
int F[1<<16][16];
int A[16][16], R[16][16];

void process() {
	memset( F, 0x1f, sizeof(F));
	inf = F[0][0];
	F[1<<begin][begin] = ns / K;
	Rep(bit,(1<<K)) {
		int cb = 0;
		Rep(i,K) if((bit&(1<<i))!=0) ++cb;
		if(cb<=1) continue;		
		Rep(last,K) if((bit&(1<<last))!=0) {
			Rep(ol,K) if((bit&(1<<ol))!=0 && ol!=last) {
				int ob = bit ^ (1<<last);
				if(F[ob][ol]!=inf) {
					int reduce = 0;
					if(cb==K) reduce = R[begin][last];
					F[bit][last] <?= F[ob][ol] + A[ol][last] - reduce;
				}
			}
		}
	}
}

void init() {
	Clear(A);
	Clear(R);
	Rep(i,K) Rep(j,K) if(i!=j) {
		Rep(t,ns/K) {
			int base = t * K;
			if(s[base+i]!=s[base+j]) ++A[i][j];
		}
	}
	Rep(begin,K) Rep(end,K) if(begin!=end) {
		Rep(t,ns/K-1) {
			int base = t * K;
			if(s[base+end]==s[base+K+begin]) ++R[begin][end];
		}
	}
}

int main() {
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	int numtest;
	scanf("%d", &numtest);
	For(test,1,numtest) {
		scanf("%d", &K);
		gets(s);
		gets(s);
		ns = strlen(s);
		init();
		int res = 1000000000;
		for(begin=0;begin<K;++begin) {
			process();
			Rep(last,K) if(last!=begin) res <?= F[(1<<K)-1][last];
		}
		printf("Case #%d: %d\n", test, res);
	}
	return 0;
}
