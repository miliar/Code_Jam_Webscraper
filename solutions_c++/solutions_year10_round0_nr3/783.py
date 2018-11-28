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

ifstream fin ("C-large.in");
#define cin fin
ofstream fout ("C-large.out");
#define cout fout
ll R,k,N,a[1001],b[1001],visited[1001],moves[1001],cnt[1001],start;
ll process(ll i) {
	ll total=0;
	REP(j,N) {
		cnt[i]=total;
		total+=a[(i+j)%N];
		if(total>k) return (i+j+N)%N;
	}
	cnt[i]=total;
	return (i+N)%N;;
}
ll go(ll k, ll pos) {
	if(visited[k]!=-1) {
		start = visited[k];
		return pos;
	}
	visited[k]=pos;
	moves[pos]=cnt[k];
	if(pos>0) moves[pos]+=moves[pos-1];
	return go(b[k],pos+1);
}
int main() {
    ll t=0;
    cin>>t;
    REP(T,t) {
		cin>>R>>k>>N;
		REP(i,N) cin>>a[i],visited[i]=-1,moves[i]=0;
		REP(i,N) b[i]=process(i);
		ll end = go(0,0);
		ll sub = start==0?0:moves[start-1];
		ll cyclecount = moves[end-1]-sub;
		ll cyclelength = end-start;
		ll ans = 0LL;
		if(R>start) {
			ans=moves[start-1] + cyclecount * (ll)((R - start)/cyclelength) + moves[(R - start)%cyclelength + start - 1] - sub;
		}
		else ans=moves[R-1];
		cout<<"Case #"<<T+1<<": "<<ans<<endl;
    }
    system("pause");
    return 0;
}
