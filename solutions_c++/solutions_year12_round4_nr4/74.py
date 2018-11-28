#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <cstring>
#include <assert.h>
#include <sys/time.h>
#include <fstream>
 
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
 
#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;
#define deb(x) cerr << #x << " = " << (x) << " , ";
#define debl cerr << " (L" << __LINE__ << ")"<< endl;
 
 
#define clr(a) memset((a),0,sizeof(a))
#define nclr(a) memset((a),-1,sizeof(a))
#define pb push_back
#define INRANGE(x,s,e) ((s)<=(x) && (x)<(e))
 
double pi=3.14159265358979323846;
 
using namespace std;
static const double EPS = 1e-5;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<string> vs;
 
template<typename T> std::ostream& operator<<(std::ostream& os, const vector<T>& z){
	os << "[ ";
	REP(i,z.size())os << z[i] << ", " ;
	return ( os << "]" << endl);
}
 
template<typename T> std::ostream& operator<<(std::ostream& os, const set<T>& z){
	os << "set( "; 
	EACH(p,z)os << (*p) << ", " ;
	return ( os << ")" << endl);
}
 
template<typename T,typename U> std::ostream& operator<<(std::ostream& os, const map<T,U>& z){
	os << "{ "; 
	EACH(p,z)os << (p->first) << ": " << (p->second) << ", " ;
	return ( os << "}" << endl);
}
 
template<typename T,typename U> std::ostream& operator<<(std::ostream& os, const pair<T,U>& z){
	return ( os << "(" << z.first << ", " << z.second << ",)" );
}
 
double get_time(){
	struct timeval tv;
	gettimeofday(&tv, NULL);
	return tv.tv_sec + tv.tv_usec*1e-6;
}

vector<string> m;
set<pii> es;

bool downable(const set<pii> &ns){
	bool any=false;
	EACH(pp,ns){
		pii p=*pp;
		int x=p.first, y=p.second;
		if(m[x+1][y]!='#' && !EXIST(es,pii(x+1,y)) )return false;
		if(m[x+1][y]!='#' )any=true;
	}
	return any;
}

set<pii> down(const set<pii> &ns){
	set<pii> ns2;
	EACH(pp,ns){
		pii p=*pp;
		int x=p.first, y=p.second;
		pii p2=pii(m[x+1][y]=='#' ? x : x+1, y);
		ns2.insert(p2);
	}
	return ns2;
}

set<pii> next(const set<pii> &ns, int dy){
	set<pii> ns2;
	EACH(pp,ns){
		pii p=*pp;
		int x=p.first, y=p.second;
		pii p2=pii(x,m[x][y+dy]=='#' ? y : y+dy);
		ns2.insert(p2);
	}
	return ns2;
}

ll hash(set<pii> ns){
	ll ret=0;
	EACH(pp,ns){
		pii p=*pp;
		ll x=p.first, y=p.second;
		ll g=x*100+y;
		ret=ret*123456789LL+g;
	}
	return ret;
}

void _main(istream &inp){
	int T;
	inp >> T >>ws;
	REP(tt,T){
		cout << "Case #" << tt+1 << ":" << endl;
		int h,w;
		inp >> h >> w >> ws;
		m=vector<string>();
		REP(i,h){
			string s;
			inp >> s;
			m.pb(s);
		}
		map<int,pii> ps;
		REP(x,h) REP(y,w) if('0' <= m[x][y] && m[x][y]<='9'){
			ps[m[x][y]-'0']=pii(x,y);
			m[x][y]='.';
		}
		REP(ii,ps.size()){
			int x0=ps[ii].first, y0=ps[ii].second;
			es=set<pii>();
			queue<pii> Q;
			Q.push(pii(x0,y0));
			while(!Q.empty()){
				int x=Q.front().first, y=Q.front().second; Q.pop();
				if(m[x][y]=='#' || EXIST(es,pii(x,y)))continue;
				es.insert(pii(x,y));
				Q.push(pii(x-1,y));
				Q.push(pii(x,y-1));
				Q.push(pii(x,y+1));
			}
			//debug(es);debug(es.size());
			set<pii> ns=es;
			while(true){
				bool change=false;
				REP(i,w) ns=next(ns,-1);
				set<ll> hs;
				queue<set<pii> > Q;
				Q.push(ns);
				while(!Q.empty()){
					set<pii> ns2=Q.front(); Q.pop();
					ll h=hash(ns2);
					if(EXIST(hs,h))continue;
					hs.insert(h);
					if(downable(ns2)){
						change=true;
						ns=down(ns2);
						break;
					}
					Q.push(next(ns2,-1));
					Q.push(next(ns2,1));
				}
				if(!change)break;
			}
			if(ns.size()<=1) printf("%d: %d Lucky\n", ii, es.size());
			else printf("%d: %d Unlucky\n", ii, es.size());
		}

	}
 
}
 
int main(){
	if(0){
		ifstream ifs("test.txt");
		_main(ifs);
	}
	else{
		_main(cin);
	}
	return 0;
}