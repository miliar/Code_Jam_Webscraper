#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdlib>

using namespace std;

#define sz(v) ((int)(v).size())
#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<string> vs;

template<class T>T abs(T x) { return (x>0) ? x : -x; }
template<class T>T sqr(T x) { return x*x;            }

int n,k;
vi a[200];
int g[200][200];
bool used[200];
int r[200];

bool Less(vi a, vi b) {
	for (int i=0; i<sz(a); i++)
		if (a[i]>=b[i]) return false;
	return true;
}

bool dfs(int v) {
	if (used[v]) return false;
	used[v]=true;
	for (int i=0; i<n; i++)
		if (g[v][i])
			if (r[i]==-1 || dfs(r[i])) {
				r[i]=v;
				return true;
			}
	return false;
}

int matching() {
	memset(r,-1,sizeof(r));
	memset(used,false,sizeof(used));
	int res=0;
	for (int i=0; i<n; i++) 
		if (dfs(i)) {
			res++;
			memset(used,false,sizeof(used));
		}
	return res;
}

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);

	int tn;
	cin>>tn;
	for (int tst=1; tst<=tn; tst++) {
		printf("Case #%d: " ,tst);
		cin>>n>>k;
		for (int i=0; i<n; i++) {
			a[i].clear();
			for (int j=0; j<k; j++) {
				int tmp;
				cin>>tmp;
				a[i].pb(tmp);
			}
		}
		memset(g,0,sizeof(g));
		for (int i=0; i<n; i++)
			for (int j=0; j<n; j++)
				if (Less(a[i],a[j]))
					g[i][j]=true;
		int res=n-matching();
		cout<<res<<endl;
	}

	return 0;
}
