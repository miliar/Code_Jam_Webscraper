#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cmath>
#include <ctime>
#include <cassert>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <complex>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <iterator>
#include <functional>
#include <utility>
#include <algorithm>
#include <numeric>
#include <typeinfo>

using namespace std;

#define dump(n) cout<<"# "<<#n<<"="<<(n)<<endl
#define repi(i,a,b) for(int i=int(a);i<int(b);i++)
#define rep(i,n) repi(i,0,n)
#define iter(c) __typeof((c).begin())
#define foreach(i,c) for(iter(c) i=(c).begin();i!=(c).end();++i)
#define allof(c) (c).begin(),(c).end()
#define mp make_pair

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int,int> pii;

struct Corridor{
	int b,e,w;
	Corridor(){}
	Corridor(int b,int e,int w):b(b),e(e),w(w){}
	bool operator<(Corridor c)const{
		return w<c.w;
	}
};

void solve()
{
	int x,s,r,t,n; cin>>x>>s>>r>>t>>n;
	vector<Corridor> cs(n);
	rep(i,n) cin>>cs[i].b>>cs[i].e>>cs[i].w;
	sort(allof(cs));
	
	double rx=x; // remain x
	rep(i,n) rx-=cs[i].e-cs[i].b;
	double rt=t,res=0; // remain t,result
	if(rx/r>rt){
		res+=rt+(rx-r*rt)/s;
		rt=0;
	}
	else{
		res+=rx/r;
		rt-=rx/r;
	}
	
	rep(i,n){
		double len=cs[i].e-cs[i].b;
		int w=cs[i].w;
		if((double)len/(w+r)>rt){
			res+=rt+(len-(w+r)*rt)/(s+w);
			rt=0;
		}
		else{
			res+=len/(w+r);
			rt-=len/(w+r);
		}
	}
	
	printf("%.10f\n",res);
}

int main()
{
	int cases; scanf("%d ",&cases);
	rep(i,cases){
		printf("Case #%d: ",i+1);
		solve();
	}
	
	return 0;
}
