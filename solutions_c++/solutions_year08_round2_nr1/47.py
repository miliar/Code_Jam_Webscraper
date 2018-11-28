#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
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

typedef long long LLong;
typedef pair<LLong, LLong> PLL;
typedef vector<PLL> VPLL;

inline int Mod(LLong x) {return ((x%3)+3)%3;}

LLong C2(LLong x) {return x*(x-1)/2;}
LLong C3(LLong x) {return x*(x-1)*(x-2)/6;}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	
	int N,tcase;
	for(cin>>N,tcase=1;tcase<=N;++tcase) {
		LLong n, A, B, C, D, x0, y0 , M, X, Y;
		VPLL p;
		cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
		X = x0, Y = y0;
		p.pb(PLL(X, Y));
		for(int i = 1;i<= n-1;i++) {
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
			p.pb(PLL(X, Y));
		}
		LLong pt[3][3]={0};
		REP(i,SZ(p))
			pt[Mod(p[i].X)][Mod(p[i].Y)]++;
		LLong res=0;
		PLL p1,p2,p3;
		for(p1.X=0;p1.X<3;++p1.X)
			for(p1.Y=0;p1.Y<3;++p1.Y)
				for(p2.X=0;p2.X<3;++p2.X)
					for(p2.Y=0;p2.Y<3;++p2.Y) 
						for(p3.X=0;p3.X<3;++p3.X)
							for(p3.Y=0;p3.Y<3;++p3.Y) 
						if(p1<=p2&&p2<=p3&&(p1.X+p2.X+p3.X)%3==0&&(p1.Y+p2.Y+p3.Y)%3==0) {
							if(p1==p2&&p1==p3) // all equal
								res+=C3(pt[p1.X][p1.Y]);
							else if(p1==p2)
								res+=C2(pt[p1.X][p1.Y])*pt[p3.X][p3.Y];
							else if(p1==p3)
								res+=C2(pt[p1.X][p1.Y])*pt[p2.X][p2.Y];
							else if(p2==p3)
								res+=C2(pt[p2.X][p2.Y])*pt[p1.X][p1.Y];
							else res+=pt[p1.X][p1.Y]*pt[p2.X][p2.Y]*pt[p3.X][p3.Y];
						}
		cout<<"Case #"<<tcase<<": "<<res<<endl;
	}
	
	fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
	return 0;
} 
