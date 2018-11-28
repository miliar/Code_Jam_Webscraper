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

int dt[16][16];
int r,c,d;
double vx,vy;

int main()
{
	int tn;

	cin>>tn;
	while (tn--) {
		cin>>r>>c>>d;
		REP(i,r) REP(j,c) {
			scanf("%1d",&dt[i][j]);
			dt[i][j]+=d;
		}

		int dp=0;
		FOR(s,3,min(r,c)+1) {
			REP(i,r-s+1) REP(j,c-s+1) {
				double cy,cx,wy,wx;
				cy=i+(s-1)/2.0;
				cx=j+(s-1)/2.0;
				wy=wx=0;
				FOR(y,i,i+s) FOR(x,j,j+s) {
					if (y==i && x==j) continue;
					if (y==i+s-1 && x==j) continue;
					if (y==i && x==j+s-1) continue;
					if (y==i+s-1 && x==j+s-1) continue;

					vx=x-cx;
					vy=y-cy;
					wx+=vx*dt[y][x];
					wy+=vy*dt[y][x];
				}

				wy=fabs(wy);
				wx=fabs(wx);
				if (wy<1e-7 && wx<1e-7) {
					dp=s;
//					cout<<i<<", "<<j<<endl;
				}
			}
		}
		

		static int qq=0;
		printf("Case #%d: ",++qq);
		if (dp==0)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",dp);
	}

	return 0;
}
