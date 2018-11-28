
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


typedef vector<int> VI;
typedef long long ll;
typedef vector<ll> VL;
typedef vector<string> VS;

string i2s(int x) { ostringstream o; o<<x; return o.str(); }
int s2i(string s) { int x; istringstream i(s); i>>x; return x; }

int a, b, p;
bool vs[1111];
int x[1111], sl;

int ok(int a, int b) {
	Rep(i,sl) if (a%x[i]==0 && b%x[i]==0) return true;
	return false;
}

bool nt(int a) {
	int i = 2;
	while (i*i<=a) {
		if (a%i==0) return false;
		i++;
	}
	return true;
}

void dfs(int i) {
	vs[i]=true;
	For(j,a,b) if (!vs[j]) {
		if (ok(j,i)) dfs(j);
	}
}

int main() {
	freopen("b0.in","r",stdin);
	freopen("b0.out","w",stdout);
	
	int st;
	cin>>st;
	For(ts,1,st) {
		cin>>a>>b>>p;
		sl = 0;
		For(i,p,b) if (nt(i)) x[sl++]=i;
		
		memset(vs,false,sizeof(vs));
		int res = 0;
		For(i,a,b) if (!vs[i]) {
			res++;
			dfs(i);
		}
		cout<<"Case #"<<ts<<": "<<res<<endl;
	}

	return 0;
}
