#include <iostream>
#include <algorithm>
#include <utility>
#include <sstream>
#include <vector>
#include <set>
using namespace std;

typedef __int64 ll;
typedef pair<int,int> ii;
#define sz(x) (int)(x).size()
#define pb push_back
#define clr(x) (x).clear()
#define all(x) (x).begin(), (x).end()

bool p[1001];
vector<int> s[1001];
int group[1001];
void sieve() {
	int N = 1000;
	for(int i=1;i<=N;++i) p[i] = true;
	for(int i=1;i<=N;++i) s[i].clear();
	s[2].pb(2);
	memset(s, 0, sizeof s);
	for(int i=2;i<=N;i++) if(p[i]) {
		s[i].pb(i);
		for(int j=i*2;j<=N;j+=i) {
			p[j] = false;
			s[j].pb(i);
		}
	}
}

int _find(int u) {
	if(group[u]==u) return u;
	return _find(group[u]);
}

void _union(int u, int v) {
	int ru = _find(u);
	int rv = _find(v);
	group[ru] = rv;
}

int chk(int i, int j, int P) {
	int k, l;
	for(k=0;k<s[i].size();++k) for(l=0;l<s[j].size();++l) {
		if(s[i][k]==s[j][l]&&s[i][k]>=P) return s[i][k];
	}
	return P - 1;
}
int main() {
	sieve();
	int C;
	int A, B, P;
	for(int i=10;i<=20;++i) {
		cerr << i << ": ";
		for(int j=0;j<s[i].size();++j) cerr << s[i][j] << " ";
		cerr << endl;
	}
	cin >> C;
	for(int cc=1;cc<=C;++cc) {
		cin >> A >> B >> P;
		int ret = B-A+1;
		for(int i=A;i<=B;++i) group[i] = i;
		for(int i=A;i<=B;++i) { 
			for(int j=i+1;j<=B;++j) {
				int p = chk(i,j,P);
				if(p>=P) {
				   	if(_find(i)!=_find(j)) {
						--ret;
						_union(i,j);
					}
				}
			}
		}
		printf("Case #%d: %d\n",cc,ret);
	}
}
