#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <queue>
#include <iostream>
#include <iterator>
#include <math.h>
#include <cstdio>
#include <cstdlib>
#include <sstream>

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long ll;

int r,c;
vector<string> field;

struct qpos {
	int r,c,r1,c1,r2,c2,d1,d2;
	qpos(int r=0,int c=0,int r1=0,int c1=0,int r2=0,int c2=0,int d1=0,int d2=0):
		r(r),c(c),r1(r1),c1(c1),r2(r2),c2(c2),d1(d1),d2(d2) {}
	bool operator<(const qpos &q)const {
		if(r<q.r)return true;
		if(r>q.r)return false;
		if(c<q.c)return true;
		if(c>q.c)return false;
		if(r1<q.r1)return true;
		if(r1>q.r1)return false;
		if(c1<q.c1)return true;
		if(c1>q.c1)return false;
		if(r2<q.r2)return true;
		if(r2>q.r2)return false;
		if(c2<q.c2)return true;
		if(c2>q.c2)return false;
		if(d1<q.d1)return true;
		if(d1>q.d1)return false;
		if(d2<q.d2)return true;
		if(d2>q.d2)return false;
		return false;
	}
};

map<qpos,int> dist;

PII dir[4]={PII(1,0),PII(0,1),PII(-1,0),PII(0,-1)};

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int n,test;
	
	for(cin>>n,test=1;test<=n;++test) {
		cin>>r>>c;
		field.resize(r);
		REP(i,r) {
			cin>>field[i];
			field[i]="#"+field[i]+"#";
		}
		field.insert(field.begin(),string(c+2,'#'));
		field.push_back(string(c+2,'#'));
		PII beg,targ;
		r+=2;c+=2;
		dist.clear();
		REP(i,r)REP(j,c)
			if(field[i][j]=='O')beg=PII(i,j);
			else if(field[i][j]=='X')targ=PII(i,j);
		vector<qpos> q[2];
		int cur=0,nxt=1;
		q[cur].pb(qpos(beg.X,beg.Y,-1,-1,-1,-1,5,5));
		int cdist=0;
		try {
			while(!q[cur].empty()) {
				q[nxt].clear();
				while(!q[cur].empty()) {
					qpos c=q[cur].back();q[cur].pop_back();
					qpos n;
					if(dist[c]!=cdist)continue;
					if(c.r==targ.X&&c.c==targ.Y)throw cdist;
					REP(d,4) {
						// moving
						n=c;n.r+=dir[d].X;n.c+=dir[d].Y;
						if(field[n.r][n.c]!='#'&&(!dist.count(n)||dist[n]>cdist+1)) {
							q[nxt].pb(n);
							dist[n]=cdist+1;
						}
						else if(field[n.r][n.c]=='#'&&n.r1==n.r&&n.c1==n.c&&d==n.d1&&n.d2<4) {
							n.r=n.r2+dir[n.d2^2].X;
							n.c=n.c2+dir[n.d2^2].Y;
							if(!dist.count(n)||dist[n]>cdist+1) {
								q[nxt].pb(n);
								dist[n]=cdist+1;							
							}
						}
						else if(field[n.r][n.c]=='#'&&n.r2==n.r&&n.c2==n.c&&d==n.d2&&n.d1<4) {
							n.r=n.r1+dir[n.d1^2].X;
							n.c=n.c1+dir[n.d1^2].Y;
							if(!dist.count(n)||dist[n]>cdist+1) {
								q[nxt].pb(n);
								dist[n]=cdist+1;							
							}
						}
						// shoting portal 1
						n=c;n.r1=n.r;n.c1=n.c;n.d1=d;
						while(field[n.r1][n.c1]!='#') {n.r1+=dir[d].X;n.c1+=dir[d].Y;}
						if(n.r1!=n.r2||n.c1!=n.c2||n.d1!=n.d2) {
							if(!dist.count(n)||dist[n]>cdist) {
								q[cur].pb(n);
								dist[n]=cdist;							
							}
						}
						// shoting portal 2
						n=c;n.r2=n.r;n.c2=n.c;n.d2=d;
						while(field[n.r2][n.c2]!='#') {n.r2+=dir[d].X;n.c2+=dir[d].Y;}
						if(n.r1!=n.r2||n.c1!=n.c2||n.d1!=n.d2) {
							if(!dist.count(n)||dist[n]>cdist) {
								q[cur].pb(n);
								dist[n]=cdist;							
							}
						}
						
					}
				}
				cdist++;
				swap(cur,nxt);
			}
			cout<<"Case #"<<test<<": THE CAKE IS A LIE"<<endl;
		}catch(int d) {
			cout<<"Case #"<<test<<": "<<d<<endl;
		}
		//REP(i,SZ(field))cerr<<field[i]<<endl;
	}
	
	fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
	return 0;
} 
