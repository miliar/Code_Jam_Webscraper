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

#include<map>

char tmp[10000];
int chk[101];
int dy[101][1001];

int main()
{
	int tn;

	cin>>tn;
	FOR(qq,1,tn+1) {
		int n,m;
		int dp=0;

		cin>>n;
		map<string,int> dt;
		scanf(" ");
		REP(i,n) {
			gets(tmp);
			dt[string(tmp)]=i;
		}
		cin>>m;
		vector<string> da(m);
		scanf(" ");
		REP(i,m) {
			gets(tmp);
			da[i]=tmp;
		}

		REP(i,n) chk[i]=0;
		int ka=0;
		REP(i,m) {
			if (dt.find(da[i])==dt.end()) continue;
			int v=dt[da[i]];
			if (chk[v]==0) {
				ka++;
				chk[v]=1;
				if (ka==n) {
					while (i+1<m && da[i]==da[i+1]) i++;
					REP(j,n) chk[j]=0;
					dp++;
					chk[v]=1;
					ka=1;
				}
			}
//			REP(j,n) printf("%d ",chk[j]); cout<<endl;
//			printf("%d %d %d\n",chk[0],chk[1],chk[2]);
		}
		
		printf("Case #%d: %d\n",qq,dp);
	}
	return 0;
}
