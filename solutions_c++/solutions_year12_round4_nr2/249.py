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
typedef pair<int,int> pint;
#define All(s) s.begin(),s.end()
#define rAll(s) s.rbegin(),s.rend()
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
//vector <double> x,y;
int r[1100],x[1100],y[1100];
double eps=1e-10;int w,h;
double tw(double a){return a*a;}
int cal(int pos,int it){
	int i,f=0;vector <pint> q;
	rep(i,it){
		if(pos-x[i]>eps+r[it]+r[i]) continue;
		double dif=sqrt(tw(r[it]+r[i])-tw(pos-x[i]));
		int di=(int)(dif+1.0-eps);
		q.pb(mp(y[i]-di,-1));q.pb(mp(y[i]+di,1));
	}
	q.pb(mp(0,1));q.pb(mp(h,-1));sort(All(q));
	rep(i,q.size()-1){
		f+=q[i].se;if(f>0) return q[i].fi;
	}
	return -1;
}
int main()
{
	int i,j,k,t,n;
	cin>>t;
	rep(i,t){
		cin>>n>>w>>h;
		rep(j,n) cin>>r[j];
		x[0]=y[0]=0;
		REP(j,1,n){
			int lo=0,hi=w+1;
			while(hi>lo){
				int mi=(hi+lo)/2;
				if(cal(mi,j)>-1) hi=mi;else lo=mi+1;
			}
			if(hi>w) cerr<<"aaaa"<<endl;
			x[j]=hi;y[j]=cal(hi,j);
		}
		printf("Case #%d:",i+1);
		rep(j,n){
			printf(" %d %d",x[j],y[j]);
		}
		printf("\n");
	}
	return 0;
}
