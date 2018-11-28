#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>

#define REPEAT(i,a,b) for(int i=a;i<b;++i)
#define RREPEAT(i,a,b) for(int i=a;i>=b;--i)
#define REP(i,n) REPEAT(i,0,n)
#define RREP(i,n) RREPEAT(i,n-1,0)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define INF (int)1<<30
#define vi vector<int>
#define vs vector<string>
#define pb push_back
#define mkp make_pair
#define ll long long int
#define uli unsigned long int
#define MAX (int)1e6

using namespace std;

ifstream fin ("B-small-attempt1.in");
#define cin fin
ofstream fout ("B-small.out");
#define cout fout

ll gcd(ll a,ll b) {
	return a%b?gcd(b,a%b):b;
}
int main() {
    int t=0;
    cin>>t;
    REP(T,t) {
		ll n=0,a[10],x;
		cin>>n;
		REP(i,n) cin>>a[i];
		x = a[0];
		ll GCD = 0LL;
		REP(i,n-1) {
			if(a[i+1]>a[i]) a[i]=a[i+1]-a[i];
			else a[i]=a[i]-a[i+1];
			if(a[i]>0LL) GCD = a[i];
		}
		REP(i,n-1) if(a[i]>0LL) GCD=gcd(GCD,a[i]);
		if(x%GCD==0LL) cout<<"Case #"<<T+1<<": "<<0LL<<endl;
		else cout<<"Case #"<<T+1<<": "<<GCD-(x%GCD)<<endl;
    }
    system("pause");
    return 0;
}
