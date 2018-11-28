#include<vector>
#include<cmath>
#include<map>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<string>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<set>
#include<stack>
#include<bitset>
#include<functional>
#include<cstdlib>
#include<ctime>
#include<queue>
#include<deque>
#include<complex>
using namespace std;
#define pb push_back
#define pf push_front
typedef long long lint;
typedef complex<double> pt;
#define mp make_pair
#define fi first
#define se second
typedef pair<double,int> pint;
#define All(s) s.begin(),s.end()
#define rAll(s) s.rbegin(),s.rend()
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
int p[1100],l[1100];
int main()
{
	int i,j,t,n;
	cin>>t;
	rep(i,t){
		cin>>n;
		rep(j,n) scanf("%d",&l[j]);
		rep(j,n) scanf("%d",&p[j]);
		vector <pint> q;
		rep(j,n) q.pb(mp(-1.0*p[j]*l[j],j));
		sort(All(q));
		printf("Case #%d:",i+1);
		rep(j,n){
			printf(" %d",q[j].se);
		}
		cout<<endl;
	}
	return 0;
}
