#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
#include <cassert>
using namespace std;

#define PB push_back
#define MP make_pair

#define rep(i,n) for(int i=0;i<(n);++i)
#define REP(i,n) for(int i=1;i<=(n);++i)
#define FOR(i,l,h) for(int i=(l);i<=(h);++i)
#define FORD(i,h,l) for(int i=(h);i>=(l);--i)
#define print(expr) cout<<(#expr)<<" : "<<(expr)<<endl

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long int64;
typedef pair<int,int> pii;
#define tr(it,c) for(auto it=(c).begin(); it!=(c).end(); ++it)
#define all(c) (c).begin(), (c).end()

void setIO(string s)
{
	string inF=s+".in";
	string outF=s+".out";
	freopen(inF.c_str(),"r",stdin);
	freopen(outF.c_str(),"w",stdout);
}

void solve(void);
int main(void)
{
	setIO("B-large");
	int T; cin>>T;
	cout<<fixed<<setprecision(1);
	REP(Case,T)
	{
		cout<<"Case #"<<Case<<": ";
		solve();
	}
}

bool chg=false;
int n,w,l;
pii rr[10000];
int r[10000];
double ansx[10000], ansy[10000];
const int inf=0x3fffffff;
void pt(double a,double b)
{
	if(chg) cout<<b<<' '<<a<<' '; 
	else cout<<a<<' '<<b<<' ';
	assert(a<=w); assert(b<=l);
}

void solve()
{
	cin>>n>>w>>l;
	chg=false;
	if(w>l) chg=true,swap(w,l);
	rep(i,n) cin>>rr[i].first, rr[i].second=i;
	sort(rr,rr+n,greater<pii>());
	rep(i,n) r[i]=rr[i].first;
	int width=0, cl=-r[0], cw=inf;
	rep(i,n)
	{
		if(cw+r[i]>w || i==0)
		{
			cl+=width+r[i];
			cw=r[i];
			width=r[i];
			ansx[rr[i].second]=0;
			ansy[rr[i].second]=cl;
		}
		else
		{
			ansx[rr[i].second]=cw+r[i];
			ansy[rr[i].second]=cl;
			cw+=2*r[i];
		}
	}
	rep(i,n) pt(ansx[i],ansy[i]);
	cout<<endl;
}