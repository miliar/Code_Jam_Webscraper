#define _CRT_SECURE_NO_DEPRECATE
#pragma comment (linker,"/STACK:64000000")

#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

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
	for (int tst=1; tst<=tn; tst++) {
		printf("Case #%d: ",tst);
		int n;
		cin>>n;
		vi a;
		for (int i=0; i<n; i++) {
			int c=-1;
			for (int j=0; j<n; j++) {
				char x;
				do {
					cin>>x;
				} while (x<=' ');
				if (x=='1')
					c=j;
			}
			a.pb(c);
		}
		int res=0;
		for (;;) {
			int i=0;
			while (i<n && a[i]<=i) i++;
			if (i==n) break;
			int j=i;
			while (j<n && a[j]>i) j++;
			assert(j<n);
			for (int t=j; t>i; t--) {
				swap(a[t],a[t-1]);
				res++;
			}
		}
		cout<<res<<endl;
	}

	return 0;
}
