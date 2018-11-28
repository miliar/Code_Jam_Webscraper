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
typedef pair<lint,lint> pint;
#define All(s) s.begin(),s.end()
#define rAll(s) s.rbegin(),s.rend()
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
lint q[210],r[210],s[210];
vector <pint> p,cl;
int it;lint f,m,inf=1000000000000010000LL;
lint pl(lint a,lint b){return min(a+b,inf);}
lint mul(lint a,lint b){
	if(inf/b<a) return inf;return b*a;
}
lint cal3(lint days){
	if(days>r[it]) return inf;
	int ite=lower_bound(r,r+it+1,days)-r-1;
	lint ret=pl(q[ite],mul(days-r[ite],s[ite]));
	return ret;
}
lint cal2(lint turn,lint num){
	lint div=turn/num,mo=turn%num,ret=mul(num,f);
	//cout<<div<<' '<<mo<<' '<<cal3(div+1)<<' '<<cal3(div)<<endl;
	ret=pl(ret,mul(mo,cal3(div+1)));
	ret=pl(ret,mul(num-mo,cal3(div)));
	return ret;
}
bool cal(lint turn){
	if(turn<1) return false;
	lint lo=1,hi=min(inf,turn),i;
	while(hi>lo+2){
		lint le=(hi+lo)/2,ri=le+1;
		if(cal2(turn,le)<cal2(turn,ri)) hi=ri;else lo=le;
	}
	REP(i,lo,hi+1){
		if(cal2(turn,i)<=m) return true;
	}
	return false;
}
int main()
{
	int i,t,n,j;lint a,b;
	cin>>t;
	rep(i,t){
		cin>>m>>f>>n;it=0;p=cl;
		rep(j,n){
			cin>>a>>b;
			p.pb(mp(a,b+1));
		}
		sort(All(p));
		lint now=0,now2=0;q[0]=r[0]=0;it=0;
		rep(j,n){
			if(now<p[j].se){
				now2=pl(now2,mul(p[j].fi,p[j].se-now));
				s[it]=p[j].fi;it++;
				q[it]=now2;r[it]=p[j].se;
				now=p[j].se;
			}
		}
		lint lo=0,hi=inf;
		while(hi>lo){
			lint mi=(lo+hi+1)/2;
			if(cal(mi)) lo=mi;else hi=mi-1;
		}
		//cout<<cal2(8,2)<<endl;
		printf("Case #%d: ",i+1);cout<<lo<<endl;
	}
	return 0;
}
