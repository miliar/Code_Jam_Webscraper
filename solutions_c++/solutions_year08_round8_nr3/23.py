#include <algorithm>
#include <iostream>
#include <iterator>
#include <fstream>
#include <cstdlib>
#include <sstream>
#include <string>
#include <vector>
#include <bitset>
#include <math.h>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <complex>

#pragma comment(linker, "/STACK:60777216")

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<pii> vpi;
typedef pair<ld,ld> pdd;
typedef complex<ld> VEC;
typedef vector<pdd> vdd;
typedef unsigned long long ul;
typedef unsigned int UI;
typedef pair<pii,int> p3i;
typedef vector<p3i> vp3i;
typedef vector<double> vd;

#define F(i,a,b) for (int _n(b), i(a); i < _n; i++) 
#define FD(i,a,b) for (int _n(b), i(a); i >= _n; i--) 
#define R(i,n) F(i,0,n) 
#define SORT(a) sort((a).begin(),(a).end())
#define UN(v) SORT(v),v.erase(unique(v.begin(),v.end()),v.end())
#define RV(v) reverse((v).begin(),(v).end())
#define CL(a,b) memset(a,b,sizeof(a))
#define pb push_back

const int INF = 1011111111;
const double Pi =acos(-1.);
const double eps =1e-9;

int nb(int x){return x?nb(x&(x-1))+1:0;}
ll gcd(ll a,ll b){while(a&&b){if(a>b) a%=b;else b%=a;}return a+b;}
int gcd(int a,int b){while(a&&b){if(a>b) a%=b;else b%=a;}return a+b;}


int TC;
vi v[555];
int n,k,x,y;
const int MOD = 1000000009; 

ll qp(ll c,ll s){
	ll q=1;
	while(s){
		if(s&1) q*=c,q%=MOD;
		c*=c;c%=MOD;
		s>>=1;
	}
	return q;
}

ll inv(int c){
	return qp(c,MOD-2);
}

ll C(ll n,ll m){
	if(m>n) return 0;
	m=n-m;
	ll a=1;
	F(i,m+1,n+1) a*=i,a%=MOD;
	//F(i,2,n-m+1) a*=inv(i),a%=MOD;
	return a;
}

ll go(int ver,int par=-1,int c1=0,int c2=0){
	ll ans=0;
	if(par==-1)
		ans=C(k-c1-c2,v[ver].size());
	else ans=C(k-c1-c2,v[ver].size()-1);
	R(i,v[ver].size())
		if(v[ver][i]!=par){
			ans*=go(v[ver][i],ver,(par==-1 ? v[ver].size()-1 : v[ver].size()-1),1);
			ans%=MOD;
		}
	/*R(i,v[ver].size()) if(v[ver][i]!=par){
		int used=0;
		R(j,v[ver].size()) if(j!=i && v[ver][j]!=par){
			used++;
			used+=v[ver][j].size()-1;
		}\
	}*/
	return ans;
}


int main(){    
    
    freopen("input.txt","r",stdin);       
    freopen("output.txt","w",stdout);   
	cin>>TC;
	R(tc,TC){
		cout<<"Case #"<<tc+1<<": ";

		cin>>n>>k;
		R(i,n+1) v[i].clear();
		R(i,n-1){
			cin>>x>>y;
			v[x].pb(y);
			v[y].pb(x);
		}
		
		cout<<go(1,-1);

		cout<<endl;
	}
    
    return 0;
}   