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
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	int tn;
	cin>>tn;
	for (int tst=1; tst<=tn; tst++) {
		printf("Case #%d: ",tst);
		ll n,k;
		cin>>n>>k;
		if (k%(1<<n)==(1<<n)-1)
			cout<<"ON\n";
		else
			cout<<"OFF\n";
	}

	return 0;
}
