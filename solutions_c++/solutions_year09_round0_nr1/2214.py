#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <cmath>
#include <queue>

#define FOR(i, n) for(int i=0; i<(n); i++)
#define DFOR(i, n) for(int i=(n)-1; i>=0; i--)
#define CLR(a, b) memset(a, sizeof(a), b)
#define MIN(a, b) ((a)<(b) ? (a):(b))
#define MAX(a, b) ((a)>(b) ? (a):(b))
#define SQR(x) ((x)*(x))
#define ABS(x) ((x)>0 ? (x) : -(x))
#define LL long long
#define VI vector<int>
#define PII pair<int, int>
#define FI first
#define SE second
#define PB push_back
#define MP make_pair
#define ALL(x) x.begin(), x.end()

using namespace std;

void init(){
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);
}

int l, d, n;
string s[5000];
string v[15];

void solve(){
	cin >> l >> d >> n;
	FOR(i, d) cin >> s[i];
	FOR(i, n){
		printf("Case #%d: ", i+1);
		string ss;
		cin >> ss;
		FOR(j, l) v[j] = "";
		int ans = 0;
		int j=0, pos = 0;
		while(j<ss.length()){
			if(ss[j]!='(') { v[pos++] = ss[j++]; continue;}
			j++;
			while(ss[j]!=')') v[pos] = v[pos]+ss[j++];
			pos++;
			j++;
		}
		
		FOR(j, d){
			bool f = true;			
			FOR(k, s[j].length())
				if(v[k].find(s[j][k])==string::npos){ f =false;break;}
			if(f) ans++;
		}
		printf("%d", ans);
		printf("\n");
	}
}

int main(){
    init();
    solve();
    return 0;
}