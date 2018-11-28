#include <vector>
#include <map>
#include <set>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <cctype>
#include <cstring>
#include <queue>
#include <cassert>
#include <ctime>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

#define MP make_pair
#define ST first
#define ND second
#define PB push_back
#define FOR(i,a,b) for( int i=(a); i<(b); ++i)
#define FORD(i,a,b) for( int i=(a); i>(b); --i)
#define REP(i,n) for(int i=0; i<(n); ++i)
#define ALL(X) (X).begin(),(X).end()
#define SZ(X) (int)(X).size()
#define FORE(it,X) for(__typeof((X).begin()) it=(X).begin(); it!=(X).end();++it)

struct ele {
	int b,e,v;

	ele() {}
	ele(int _b,int _e,int _v)
	{
		b=_b;
		e=_e;
		v=_v;
	}

	bool operator<(ele t) const
	{
		return v < t.v;
	}
};

int X,S,R,n;
double T;
int V[2048];
int d[2048];
ele dt[1024];
int m;

int main()
{
	int tn;
	cin>>tn;

	while (tn--) {
		int N;
		scanf("%d%d%d%lf%d",&X,&S,&R,&T,&N);
		memset(V,0,sizeof(V));
		memset(d,0,sizeof(d));
		set<int> xs;
		REP(i,N) {
			scanf("%d%d%d",&dt[i].b,&dt[i].e,&dt[i].v);
			xs.insert(dt[i].b);
			xs.insert(dt[i].e);
		}
		FOR(i,N,1024)
			dt[i].b=dt[i].e=dt[i].v=-1;

		xs.insert(0);
		xs.insert(X);
		n=0;
		FORE(it,xs)
			d[n++]=*it;

		int p=0, u=0;
		REP(i,n) {
			if (dt[p].b == d[i])
				u=dt[p].v;
			if (dt[p].e == d[i]) {
				p++;
				if (dt[p].b == d[i])
					u=dt[p].v;
				else
					u=0;
			}
			V[i]=u;
		}

//		REP(i,n) cout<<d[i]<<" "; cout<<endl;
//		REP(i,n) cout<<V[i]<<" "; cout<<endl;

		vector<ele> da;
		REP(i,n-1)
			da.PB(ele(d[i],d[i+1],V[i]));
		sort(ALL(da));
//		REP(i,SZ(da))
//			cout<<da[i].b<<" "<<da[i].e<<" "<<da[i].v<<endl;

		double dp=0;
		double s,v,t;
		REP(i,n-1) {
			s=da[i].e-da[i].b;
			int VV=da[i].v;
			if (T>0) {
				v=VV+R;
				double go=v*T;
				if (go>s) { // T°¡ ³²À½
					t=s/v;
					T-=t;
					dp+=t;
				}
				else {
					s-=go;
					dp+=T; T=0;

					v=VV+S;
					t=s/v;
					dp+=t;
				}
			}
			else {
				v=VV+S;
				t=s/v;
				dp+=t;
			}
//			cout<<"t : "<<t<<endl;
		}

		static int qq=0;
		printf("Case #%d: %.10f\n",++qq,dp);
	}
	return 0;
}
