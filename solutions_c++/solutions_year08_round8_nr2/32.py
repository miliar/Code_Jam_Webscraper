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
int nm=0;
map<string,int> C;
int getN(string c){
	if(C[c]) return C[c];
	nm++;
	return C[c]=nm;
}
int n;
int c[333],a[333],b[333];
vi v[333];

bool  u[333];
int   D[333];

int go(int ver){
	if(a[ver]==1) return 1;
	if(u[ver]) return D[ver];
	int vl=INF;
	R(i,v[ver].size()) vl=min(vl,go(v[ver][i]));
	return D[ver]=vl+1;
}
int main(){    
    
    freopen("input.txt","r",stdin);       
    freopen("output.txt","w",stdout);   
	cin>>TC;
	R(tc,TC){
		cout<<"Case #"<<tc+1<<": ";

		cin>>n;
		C.clear();
		R(i,n){
			string col;
			cin>>col;
			c[i]=getN(col);
			cin>>a[i]>>b[i];
		}
	
		int mn=INF;			
		F(c1,1,nm+1) F(c2,c1,nm+1) F(c3,c2,nm+1){
			R(i,n) v[i].clear();
			R(i,n) if(c[i]==c1 || c[i]==c2 || c[i]==c3)
				R(j,n) if(c[j]==c1 || c[j]==c2 || c[j]==c3)
					if(b[i]>b[j] && a[i]<=b[j]+1)
						v[i].pb(j);
			CL(u,false);
			R(i,n) if(b[i]==10000)
				mn=min(go(i),mn);			
		}
		if(mn==INF) cout<<"IMPOSSIBLE";
		else cout<<mn;	
		cout<<endl;
	}
    
    return 0;
}   