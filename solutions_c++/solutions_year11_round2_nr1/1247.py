#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <list>
#include <deque>
#include <stack>
#include <sstream>
#include <fstream>

#define ll long long int
#define FOR(i,a,b) for(ll i=a;i<b;++i)
#define REP(i,n) FOR(i,0,n)
#define RFOR(i,a,b) for(ll i=b-1;i>=a;--i)
#define RREP(i,n) RFOR(i,0,n)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define INF (int)1<<30
#define vi vector<int>
#define vs vector<string>
#define pb push_back
#define mkp make_pair
#define uli unsigned long int
#define MAX (int)1e6
#define pi pair<int,int>
#define V(x) vector< x >
#define GI ({int t;scanf("%d",&t);t;})

using namespace std;
int n;
char a[101][101];
		
double WP(int i, int x) {
	int cnt = 0, win = 0;
	REP(j,n) 
		if(j!=x && a[i][j]!='.') cnt++, win+=(a[i][j]=='1');
	return (double) win/(cnt*1.0);
}
int main() {
	int t;
	cin>>t;
	REP(T,t) {
		vector<double> WPs, OWPs;
		cin>>n;
		REP(i,n)	cin>>a[i];
		cout<<"Case #"<<T+1<<":"<<endl;
		REP(i,n) {
			double OWP = 0.0;
			int cnt = 0;
			REP(j,n) 
				if(a[i][j]!='.') {
					OWP+=WP(j,i);
					cnt++;
				}
			OWP/=cnt;
			WPs.pb(WP(i,-1));
			OWPs.pb(OWP);
		}
		REP(i,n)
		{
			int cnt=0;
			double OOWP = 0.0;
			REP(j,n) if(a[i][j]!='.') cnt++, OOWP+=OWPs[j];
			cout<< 0.25* WPs[i] + 0.5* OWPs[i] + 0.25 * OOWP/cnt <<endl;
		}
	}
	return 0;
}
