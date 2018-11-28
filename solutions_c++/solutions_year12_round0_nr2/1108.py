#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <functional>
#include <cmath>
#include <sstream>
#include <ctime>
#include <memory.h>
#define forn(i,n) for (int i = 0; i < (int)(n); i++)
#define forv(i, a) for(int i=0; i<(int)a.size(); i++)
#define mset(a, val) memset(a, val, sizeof(a))
#define all(a) a.begin(),a.end()
#define mp make_pair
#define pb push_back
#define VI vector< int >
#define VS vector< string >
#define PII pair< int,int >
#define PDD pair< double,double >
#define PIS pair< int, string >
#define sqr(a) ((a)*(a))
#define cube(a) ((a)*(a)*(a))
#define pi 3.1415926535897932384626433832795
#define PI pi
#define iinf 1000000000
#define linf 1000000000000000000LL
#define sinf 10000
#define eps 1e-12
#define lng long long
#define X first
#define Y second
using namespace std;
#define prev asdprev
#define exit(a) { if (a) cerr<<"oops "<<a<<endl; exit(a); }

#define max(a, b) ((a>b)?a:b)

int n, s, p;
int a[1000], b[1000];

int solve(){
	forn(i, n) b[i]=a[i]/3+(a[i]%3?1:0);

	int ans=0;
	forn(i, n){
		if(b[i]>=p) ++ans;
		else
		if(b[i]+1>=p && b[i]!=a[i] && a[i]%3!=1 && s>0){
			--s; ++ans;
		}
	}
	
	return ans;
}

#define taska "intersection"
int main() {
#ifdef __ASD__
	freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
#else
	//freopen(taska".in", "r", stdin);freopen(taska".out", "w", stdout); freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
#endif

	int T;
	cin>>T;
	
	forn(tc, T){
		cin>>n>>s>>p;
		forn(i, n) cin>>a[i];
		
		cout<<"Case #"<<tc+1<<": "<<solve()<<endl;
	}


	return 0;
}