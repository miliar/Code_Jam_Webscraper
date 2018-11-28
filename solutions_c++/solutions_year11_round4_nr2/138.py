#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>


 
using namespace std;
 
const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;
 
#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

char buf[600][600];
int feld[600][600];
int dp[600][600];
int dpx[600][600];
int dpy[600][600];
int main(){
	int tc;
	scanf("%d",&tc);
	FOR(tcc,1,tc+1){
		int R,C,D;
		scanf("%d%d%d",&R,&C,&D);
		FOR(r,0,R)scanf("%s",buf[r]);
		FOR(r,0,R)FOR(c,0,C){
			feld[r][c]=buf[r][c]-'0';
		}
		memset(dp,0,sizeof(dp));
		FOR(r,0,R)FOR(c,0,C){
			dp[r+1][c+1]=dp[r+1][c]+dp[r][c+1]-dp[r][c]+feld[r][c];
		}
		memset(dpx,0,sizeof(dpx));
		memset(dpy,0,sizeof(dpy));
		FOR(r,0,R)FOR(c,0,C){
			dpx[r+1][c+1]=dpx[r][c+1]+(dp[r+1][c+1]-dp[r][c+1])*r;
		}
		FOR(r,0,R)FOR(c,0,C){
			dpy[r+1][c+1]=dpy[r+1][c]+(dp[r+1][c+1]-dp[r+1][c])*c;
		}
		int res = -1;
		FORD(s,3,min(R,C)+1){
			FOR(r,0,R-s+1)FOR(c,0,C-s+1){
				int ma = dp[r+s][c+s-1]+dp[r][c+1]-dp[r+s][c+1]-dp[r][c+s-1]
						+dp[r+s-1][c+1]+dp[r+1][c]-dp[r+s-1][c]-dp[r+1][c+1]
						+dp[r+s-1][c+s]+dp[r+1][c+s-1]-dp[r+s-1][c+s-1]-dp[r+1][c+s];
				int mx = dpx[r+s][c+s-1]+dpx[r][c+1]-dpx[r+s][c+1]-dpx[r][c+s-1]
						+dpx[r+s-1][c+1]+dpx[r+1][c]-dpx[r+s-1][c]-dpx[r+1][c+1]
						+dpx[r+s-1][c+s]+dpx[r+1][c+s-1]-dpx[r+s-1][c+s-1]-dpx[r+1][c+s];
				int my = dpy[r+s][c+s-1]+dpy[r][c+1]-dpy[r+s][c+1]-dpy[r][c+s-1]
						+dpy[r+s-1][c+1]+dpy[r+1][c]-dpy[r+s-1][c]-dpy[r+1][c+1]
						+dpy[r+s-1][c+s]+dpy[r+1][c+s-1]-dpy[r+s-1][c+s-1]-dpy[r+1][c+s];
				mx*=2;my*=2;
//				cout << ma << " " << mx << " "<< my << " " << r << " " << c << " " << s <<endl;
				if(mx==(r*2-1+s)*ma&&my==(s+c*2-1)*ma){
					res = s;
					goto doOutput;
				}
			}
		}
doOutput:
		printf("Case #%d: ",tcc);
		if(res==-1)printf("IMPOSSIBLE\n");
		else printf("%d\n",res);
	}
	return 0;
}
