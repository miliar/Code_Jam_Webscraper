#include <stdio.h>
#include <iostream>
#include <set>
#include <map>
#include <string>
#include <string.h>
#include <queue>
#include <algorithm>
#include <math.h>
#include <sstream>
#include <complex>
#include <fstream>
using namespace std;

void solve();
#define mp make_pair
#define pb push_back
int main(){	
    freopen("input", "r", stdin);
    freopen("output","w",stdout);
	
	int t;
	cin>>t;
	for(int i=1;i<=t;++i){
		printf("Case #%d: ",i);
		solve();
	}
    return 0;
}
typedef long long int li;
#define int li
#ifdef int
#define INT "%lld"
#else
#define INT "%ld"
#endif
typedef pair<int, int> pi;
typedef vector<int> vi;
typedef double ld;
void solve(){
	int x,s,r,T,n;
	scanf(INT INT INT INT INT,&x,&s,&r,&T,&n);
	double t=T;
	map<int,int> m; //m[v]=meters;
	m[0]=x;
	for(int i=0;i<n;++i){
		int b,e,w;
		scanf(INT INT INT,&b,&e,&w);
		m[0]-=e-b;
		m[w]+=e-b;
	}
	double ans=0;
	for(map<int,int>::iterator it=m.begin();it!=m.end();++it){
		
		//cerr<<it->first<<' '<<it->second;
		if(t>(it->second/(ld)(r+it->first))){
			ans+=it->second/(ld)(r+it->first);
			t-=it->second/(ld)(r+it->first);
		}
		else{
			double beg=t*(r+it->first);
			ans+=t;
			t=0;
			ans+=(it->second-beg)/(ld)(s+it->first);
		}
	}
	printf("%.10lf\n",ans);
}