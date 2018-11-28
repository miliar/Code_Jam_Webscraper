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
#define eps 1e-9
#define lng long long
#define X first
#define Y second
using namespace std;
#define prev asdprev
#define exit(a) { if (a) cerr<<"oops "<<a<<endl; exit(a); }

#define max(a, b) ((a>b)?a:b)
#define min(a, b) ((a<b)?a:b)

const int MAXN=2050000;

int a[50];
int b[MAXN];
int b2[MAXN];
int n;

void rev(int pos, vector<int> &ans){

	while(pos!=0){
		ans.pb(b[pos]);
		pos=pos-a[b[pos]];
	}
}

void printans(int tc, vector<int> &a1, vector<int> &a2){
	cout<<"Case #"<<tc<<": \n";
	forv(i, a1) cout<<a[a1[i]]<<" ";
	cout<<'\n';
	forv(i, a2) cout<<a[a2[i]]<<" ";
	cout<<'\n';
}

void solve(int tc){
	mset(b, -1);
	b[0]=0;

	forn(i, n){
		memcpy(b2, b, sizeof(b));
		forn(num, MAXN){
			if(b[num]<0) continue;
				
			int to=num+a[i];
			
			if(b[to]<0) b2[to]=i;
			else{
				vector<int> a1, a2;

				rev(to, a1);
				rev(num, a2);
				a2.pb(i);
				
				printans(tc, a1, a2);

				return;
			}
		}
		memcpy(b, b2, sizeof(b));
	}

	cout<<"Case #"<<tc<<": Impossible\n";
}

#define taska "intersection"
int main() {
#ifdef __ASD__
	freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
#else
	//freopen(taska".in", "r", stdin);freopen(taska".out", "w", stdout); freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
#endif
	ios_base::sync_with_stdio(false);

	int T;

	cin>>T;
	forn(tc, T){
		cin>>n;
		forn(i, n) cin>>a[i];

		solve(tc+1);
	}


	return 0;
}