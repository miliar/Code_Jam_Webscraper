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

char x[] = "welcome to code jam";
char a[555];
int n;
int s[555][22];

int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	
	int st;
	scanf("%d",&st);
	gets(a);
	For(ts,1,st) {
		gets(a);
		
		int n = strlen(a);
		
		memset(s,0,sizeof(s));
		s[0][0]=1;
		For(i,1,n) {
			Rep(j,20) s[i][j]=s[i-1][j];
			For(j,1,19) if (a[i-1]==x[j-1]) {
				s[i][j]+=s[i-1][j-1];
				if (s[i][j]>=10000) s[i][j]-=10000;
			}
		}
		
		string res = i2s(s[n][19]);
		while (SZ(res)<4) res = "0"+res;
		
		cout<<"Case #"<<ts<<": "<<res<<endl;
	}

	return 0;
}
