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

int main() {
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);

	int tn;
	cin>>tn;
	for (int tst=1; tst<=tn; tst++) {
		cerr<<tst<<endl;
		printf("Case #%d: ",tst);
		int n,k,b,t;
		cin>>n>>k>>b>>t;
		vi x(n),v(n);
		forn(i,n) cin>>x[i];
		forn(i,n) cin>>v[i];
		vector<ii> a(n);
		forn(i,n) a[i]=mp(x[i],v[i]);
		sort(all(a));
		reverse(all(a));
		int cur=0;
		int res=0;
		forn(i,n) {
			int x=a[i].first;
			int v=a[i].second;
			if (x+v*t<b) {
				if (cur<k)
					res+=k-cur;
			} else
				cur++;
		}
		if (cur<k)
			cout<<"IMPOSSIBLE\n";
		else
			cout<<res<<endl;
	}

	return 0;
}
