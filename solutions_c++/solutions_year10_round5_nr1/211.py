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

int a[20], d, np, p[511111], n;
bool nt[1111111];

int main() {
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	
	memset(nt,true,sizeof(nt));
	nt[1]=false;
	For(i,2,1000) if (nt[i]) {
		int j = i+i;
		while (j<=1000000) {
			nt[j]=false;
			j+=i;
		}
	}
	
	int np = 0;
	For(i,2,1000000) if (nt[i]) p[np++]=i;
	
	int st; 
	scanf("%d",&st);
	For(ts,1,st) {
		scanf("%d%d",&d,&n);
		
		For(i,1,n) scanf("%d",&a[i]);
		
		if (n==1) {
			printf("Case #%d: I don't know.\n",ts);
			continue;
		}
		
		int md = 1;
		Rep(i,d) md*=10;
		
		int ma = 0;
		For(i,1,n) ma = max(ma, a[i]);
		
		int nres = 0;
		int res = -1;
		//int ares = -1, bres = -1, pres = -1;
		Rep(i,np) if (p[i]>ma && p[i]<=md) {
			Rep(x,p[i]) {
				ll tmp = x;
				tmp*=a[1];
				tmp%=p[i];
				int y = a[2]-tmp;
				if (y<0) y+=p[i];
				
				int ok = true;
				For(j,2,n-1) {
					tmp = x;
					tmp=(tmp*a[j]+y)%p[i];
					if (tmp!=a[j+1]) {
						ok = false;
						break;
					}
				}
				if(ok) {
					nres=1;
					tmp = x;
					int tres = (tmp*a[n]+y)%p[i];
					
					if (res<0) res = tres;
					else if (res!=tres) {
						nres=2;
						break;
					}
				}
			}
			if (nres>1) break;
		}
		
		if (nres>1) printf("Case #%d: I don't know.\n",ts);
		else printf("Case #%d: %d\n",ts,res);
	}

	return 0;
}
