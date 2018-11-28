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

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	int tn;
	cin>>tn;

	for (int tst=0; tst<tn; tst++) {
		printf("Case #%d: ",tst+1);
		int n;
		cin>>n;
		vector<ll> a(n), b(n);
		for (int i=0; i<n; i++) cin>>a[i];
		for (int i=0; i<n; i++) cin>>b[i];
		sort(all(a));
		sort(all(b));
		reverse(all(b));
		ll res=0;
		for (int i=0; i<n; i++)
			res+=a[i]*b[i];
		cout<<res<<endl;
	}


	return 0;
}
