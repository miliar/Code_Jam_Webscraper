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
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);

	int tn;
	cin>>tn;
	for (int tst=1; tst<=tn; tst++) {
		printf("Case #%d: ",tst);
		int r,k,n;
		cin>>r>>k>>n;
		vi c(n);
		forn (i,n) cin>>c[i];
		vi add(n),to(n);
		forn (i,n) {
			if (i%100==0)
				cerr<<"i="<<i<<endl;
			int cnt=0;
			int j=i;
			while (cnt<n && add[i]+c[j]<=k) {
				add[i]+=c[j];
				cnt++;
				j=(j+1)%n;
			}
			to[i]=j;
		}
		int at=0;
		ll res=0;
		forn (it,r) {
			res+=add[at];
			at=to[at];
		}
		cout<<res<<endl;
	}

	return 0;
}

