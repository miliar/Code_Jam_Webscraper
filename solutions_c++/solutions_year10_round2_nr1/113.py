#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(v) (int(v.size()))
#define pch putchar
#define gch getchar()
#define FORD(i,a,b) for (int i=(a); i<=(b); i++)
#define FORP(i,a,b) for (int i=(a); i>=(b); i--)
#define REP(i,n) for (int i=0; i<(n); i++)
#define clean(v) memset(v,0,sizeof(v))

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <map>

using namespace std;

template<typename T> T sqr(const T& c) {return c*c;} 

typedef long long ll;
typedef double lf;

vector< map<string,int> > tr;

string s, tmp;
int ans;

void add(string &s, int uk, int v, bool create) {
	if (uk==sz(s)) return;
	uk++;
	tmp.clear(); while (uk<sz(s) && s[uk] != '/') tmp.pb(s[uk]), uk++;
	if (tr[v].find(tmp)==tr[v].end()) {
		if (create) ans++;
		tr[v][tmp] = sz(tr);
		tr.pb(map<string,int>());
		add(s,uk,sz(tr)-1,create);
	} else
		add(s,uk,tr[v][tmp],create);
}

int main() {
	int tests, n, m;
	scanf("%d\n",&tests);
	FORD(curTest,1,tests) {
		tr.clear();
		tr.pb(map<string,int>());
		scanf("%d%d\n",&n,&m);
		//cerr << n << ' ' << m << '\n';
		REP(i,n) {
			//cerr << s << '\n';
			getline(cin,s);
			add(s,0,0,0);
		}
		ans = 0;
		REP(i,m) {
  			//cerr << s << '\n';
			getline(cin,s);
			add(s,0,0,1);
		}
		printf("Case #%d: %d\n",curTest,ans);
	}
}
