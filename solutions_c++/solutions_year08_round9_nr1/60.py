#define _CRT_SECURE_NO_DEPRECATE
#pragma comment (linker,"/STACK:64000000")

#include <iostream>
#include <sstream>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <cctype>
#include <cassert>

using namespace std; 

#define sz(v) ((int) (v).size())
#define all(v) (v).begin(), (v).end()
#define mp make_pair
#define pb push_back

typedef double D;
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> ii;

template<typename T> T abs(T x) { return x>0 ? x : -x; }
template<typename T> T sqr(T x) { return x*x;          }

const int max_n=5000+218;

int n;
int a[max_n],b[max_n],c[max_n];
int add[11000];

int solve(vi b, vi c, int s) {
	memset(add,0,sizeof(add));
	int res=0;
	for (int i=0; i<sz(b); i++) {
		int l=b[i];
		int r=s-c[i];
		if (l<=r) {
			add[l]++;
			add[r+1]--;
		}
	}
	int cur=0;
	for (int i=0; i<10000+2; i++) {
		res=max(res,cur);
		cur+=add[i];
	}
	return res;
}

int main() {
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	int tn;
	cin>>tn;
	for (int tst=0; tst<tn; tst++) {
		cerr<<tst<<endl;
		printf("Case #%d: ",tst+1);
		cin>>n;
		for (int i=0; i<n; i++)
			cin>>a[i]>>b[i]>>c[i];
		int res=0;
		for (int A=0; A<=10000; A++) {
			vi bb,cc;
			for (int i=0; i<n; i++)
				if (a[i]<=A) {
					bb.pb(b[i]);
					cc.pb(c[i]);
				}
			res=max(res,solve(bb,cc,10000-A));
		}
		cout<<res<<endl;
	}

	return 0;
}
