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

const ll mod=100003;

ll ans[700][700];
ll d2[700];
ll c[700][700];

ll C(int n, int k) {
	if (n<k) return 0;
	if (k==0) return 1;
	if (n==0) return 0;
	ll &res=c[n][k];
	if (res!=-1) return res;
	res=C(n-1,k-1)+C(n-1,k);
	return res;
}

ll solve(int n, int k) {
	if (n==1) return 0;
	if (k==1) return 1;
	ll &res=ans[n][k];
	if (res!=-1) return res;
	res=0;
	for (int t=1; t<k; t++)
		res+=solve(k,t)*C(n-k-1,k-t-1);
	return res;
}

int main() {
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);

	memset(ans,-1,sizeof(ans));
	memset(c,-1,sizeof(c));
	d2[0]=1;
	for (int i=1; i<700; i++)
		d2[i]=d2[i-1]*2%mod;
	int tn;
	cin>>tn;
	for (int tst=1; tst<=tn; tst++) {
		cerr<<tst<<endl;
		printf("Case #%d: ",tst);
		int n;
		cin>>n;
		ll res=0;
		for (int i=1; i<n; i++)
			res=(res+solve(n,i))%mod;
		cout<<res<<endl;
	}

	return 0;
}
