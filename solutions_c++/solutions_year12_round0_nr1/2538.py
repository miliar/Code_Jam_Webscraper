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
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	
	string decoder = "yhesocvxduiglbkrztnwjpfmaq";
	
	string s;
	int n;
	scanf("%d",&n);
	getline(cin, s);
	For(i,1,n) {
		getline(cin, s);
		Rep(j,SZ(s)) if (s[j]!=' ') s[j]=decoder[s[j]-'a'];
		
		cout<<"Case #"<<i<<": "<<s<<endl;
	}

	return 0;
}
