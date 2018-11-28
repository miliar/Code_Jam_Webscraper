#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>

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
#define FORE(it,X) for(__typeof((X).begin()) it=(X).begin(); it!=(X).end(); ++it)

int dy[10005][2];
int gate[10005],c[10005];

int main()
{
	int tn,qq=0;

	cin>>tn;
	while (tn--) {
		int n,des;
		cin>>n>>des;
		memset(dy,31,sizeof(dy));
		memset(gate,-1,sizeof(gate));
		memset(c,-1,sizeof(c));
		REP(i,(n-1)/2)
			cin>>gate[i]>>c[i];
		FOR(i,(n-1)/2,n) {
			int a;
			cin>>a;
			dy[i][a]=0;
		}
		
		FORD(v,(n-1)/2-1,-1) {
			int v1,v2;
			v1=v*2+1,v2=v*2+2;
//			if (c[v]==0)
			if (gate[v]==1) {
				dy[v][0]=min(dy[v][0],dy[v1][0]+dy[v2][0]);
				dy[v][0]=min(dy[v][0],dy[v1][0]+dy[v2][1]);
				dy[v][0]=min(dy[v][0],dy[v1][1]+dy[v2][0]);
				dy[v][1]=min(dy[v][1],dy[v1][1]+dy[v2][1]);
			}
			else {
				dy[v][0]=min(dy[v][0],dy[v1][0]+dy[v2][0]);
				dy[v][1]=min(dy[v][1],dy[v1][0]+dy[v2][1]);
				dy[v][1]=min(dy[v][1],dy[v1][1]+dy[v2][0]);
				dy[v][1]=min(dy[v][1],dy[v1][1]+dy[v2][1]);
			}
			if (c[v]==1) {
				if (gate[v]==1) {
					dy[v][1]=min(dy[v][1],dy[v1][0]+dy[v2][1]+1);
					dy[v][1]=min(dy[v][1],dy[v1][1]+dy[v2][0]+1);
				}
				else {
					dy[v][0]=min(dy[v][0],dy[v1][0]+dy[v2][1]+1);
					dy[v][0]=min(dy[v][0],dy[v1][1]+dy[v2][0]+1);
				}
			}
//			}
		}
		printf("Case #%d: ",++qq);
		if (dy[0][des]>234234234) cout<<"IMPOSSIBLE\n";
		else cout<<dy[0][des]<<endl;
	}
	return 0;
}
