#include <cstdio>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <cassert>
#include <ctime>
#include <iostream>
#include <utility>
#include <algorithm>
#include <limits>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <bitset>
#include <stack>
#include <complex>
#include <tr1/unordered_set>
#include <tr1/unordered_map>

#define mp(x,y) make_pair(x,y)
#define pb(x) push_back(x)
#define fs first
#define sc second
#define sz(x) (int((x).size()))
#define all(x) ((x).begin()),((x).end())
#define rep(i,n) for(int (i)=0;(i)<(n);(i)++)
#define fab(i,a,b) for(int (i)=(a);(i)<=(b);(i)++)
#define fba(i,b,a) for(int (i)=(b);(i)>=(a);(i)--)
#define MAX(a,x) a=max(a,x)
#define MIN(a,x) a=min(a,x)

using namespace std;
using namespace std::tr1;

const double eps = 1e-10, inf = 1e10;
typedef long long ll;

#define MAXN 2000000

int A, B;
vector<int> adj[MAXN+10];

void solve(int test)
{
	printf("Case #%d: ", test);
	scanf("%d%d", &A, &B);
	set< pair<int,int> > db;
	fab(i, A, B) {
		rep(j, sz(adj[i]))
			if (adj[i][j] <= B)
				db.insert(make_pair(i, adj[i][j]));
	}
	printf("%d\n", sz(db));
}

int p10[] = {1,10,100,1000,10000,100000,1000000,10000000};

int digits(int x)
{
	rep(i, 8) if (p10[i] >= x) return i+1;
	return -1;
}

int main()
{
    int cifre = 0;
    fab(i, 1, MAXN) {
		//cerr << "Numero: " << i << "\n";
		rep(j, 8) if (p10[j] == i) {
			cifre ++;
			break;
		}
		int p = i, newp;
		fab(j, 1, cifre-1) {
			newp = (p % p10[j]) * p10[cifre-j] + (p / p10[j]);
			//cerr << "\t" << newp << "\n";
			if (digits(p) != digits(newp) || p == newp) continue;
			adj[min(p, newp)].pb(max(p, newp));
		}
	}
	fab(i, 1, MAXN) {
		set<int> a( adj[i].begin(), adj[i].end() );
		adj[i].clear();
		for (set<int>::iterator it=a.begin(); it!=a.end(); it++) adj[i].pb(*it);
	}
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int t;
	scanf("%d", &t);
	rep(i, t) solve(i+1);
}
