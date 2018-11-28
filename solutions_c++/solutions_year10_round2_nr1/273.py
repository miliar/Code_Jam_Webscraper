#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;

#define sz(v) ((int) (v).size())
#define all(v) (v).begin(), (v).end()
#define mp make_pair
#define pb push_back
#define forn(i,n) for (int i=0; i<n; i++)

typedef long long ll;
typedef long long int64;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<string> vs;

template<typename T> T abs(T x) { return x>0 ? x : -x; }
template<typename T> T sqr(T x) { return x*x;          }

const int max_n=1000*1000;

map<string,int> next[max_n];
int cur;
int res;

vs split(string s) {
	forn(i,sz(s)) if (s[i]=='/') s[i]=' ';
	istringstream in(s);
	vs res;
	string tmp;
	while (in>>tmp) res.pb(tmp);
	return res;
}

void process(string s, int add) {
	vs v=split(s);
	int at=0;
	forn(i,sz(v)) {
		if (next[at].find(v[i])!=next[at].end())
			at=next[at][v[i]];
		else {
			cur++;
			res+=add;
			next[at][v[i]]=cur;
			at=cur;
		}
	}
}


int main() {
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	int tn;
	cin>>tn;
	for (int tst=1; tst<=tn; tst++) {
		cerr<<tst<<endl;
		printf("Case #%d: ",tst);
		forn(i,max_n) next[i].clear();
		cur=0;
		int n,m;
		cin>>n>>m;
		res=0;
		forn(i,n) {
			string s;
			cin>>s;
			process(s,0);
		}
		forn(i,m) {
			string s;
			cin>>s;
			process(s,1);
		}
		cout<<res<<endl;

	}

	return 0;
}
