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

int m,n;
set<string> s;

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int st;
	scanf("%d",&st);
	For(ts,1,st) {
		scanf("%d%d",&n,&m);
		
		s.clear();
		
		Rep(i,n) {
			char ca[200];
			scanf("%s",ca);
			string sa = (string) ca;
			sa+="/";
			
			string tmp = "";
			int la = SZ(sa);
			
			For(j,1,la-1) {
				tmp+=sa[j];
				if (sa[j]=='/') {
					s.insert(tmp);	
				}
			} 
		}
		
		int res = 0;
		Rep(i,m) {
			char ca[200];
			scanf("%s",ca);
			string sa = (string) ca;
			sa+="/";
			
			string tmp = "";
			int la = SZ(sa);
			
			For(j,1,la-1) {
				tmp+=sa[j];
				if (sa[j]=='/') {
					if (s.find(tmp)==s.end()) {
						res++;
						s.insert(tmp);
					}	
				}
			} 
		}
		
		printf("Case #%d: %d\n",ts,res);
	}

	return 0;
}
