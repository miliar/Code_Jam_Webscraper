#pragma comment(linker, "/STACK:65777216")

#include <algorithm>
#include <iostream>
#include <string>
#include<sstream>
#include<string.h>
#include <cstdio>
#include <vector>
#include <bitset>
#include <cmath>
#include <queue>
#include<stack>
#include <set>
#include <map>
#include<ctime>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef unsigned long long ull;

#define FOR(i,a,b) for (int i(a); i < (b); i++) 
#define REP(i,n) FOR(i,0,n) 
#define SORT(v) sort((v).begin(),(v).end())
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define CL(a,b) memset(a,b,sizeof(a))
#define pb push_back

int b[1111],e[1111];
int w[1111];

int main(){ 
#ifdef LocalHost
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif

	int tc;
	cin>>tc;
	REP(TC,tc){
		int x,s,r,n;
		double t;
		cin>>x>>s>>r>>t>>n;
		REP(i,n) cin>>b[i]>>e[i]>>w[i];
		vector<pii> v;
		REP(i,n) REP(j,i) if(b[i]<b[j]){
			swap(b[i],b[j]);
			swap(e[i],e[j]);
			swap(w[i],w[j]);
		}
		v.pb(pii(s,b[0]));
		v.pb(pii(s,x-e[n-1]));
		REP(i,n) v.pb(pii(s+w[i],e[i]-b[i]));
		FOR(i,1,n) v.pb(pii(s,b[i]-e[i-1]));
		SORT(v);
		double res = 0;
		REP(i,v.size()){
			double q = v[i].second / double(v[i].first + r - s);
			q = min(q, (double)t);
			res += q;
			t -= q;
			res += (v[i].second - (v[i].first + r - s) * q) / double(v[i].first);
		}
		printf("Case #%d: %.10lf\n",TC+1,res);
	}


/*#ifdef LocalHost
	cout<<endl<<endl<<clock()<<endl;
#endif*/
	return 0;
}