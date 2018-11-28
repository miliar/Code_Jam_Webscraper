#include "bignum.h"
#include<iostream>
#include<list>
#include<queue>
#include<vector>
#include<set>
#include<map>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<cstring>
#include<algorithm>
#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,a,b) for(i=(a);i<(b);++i)
#define PB push_back
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<LL> VLL;
const int dx[]={-1,0,1,0,-1,-1,1,1};
const int dy[]={0,1,0,-1,-1,1,-1,1};
bool s[1000][1000],s2[1000][1000];
const int Q=1000*1000;
int x[Q],y[Q];
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int _T,T;
	scanf("%d",&_T);
	REP(T,_T) {
		printf("Case #%d: ",T+1);
		int rr,x1,y1,x2,y2;
		scanf("%d",&rr);
		int i;
		memset(s,0,sizeof(s));
		int l=0,r=0;
		REP(i,rr) {
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			int p,q;
			FOR(p,x1,x2+1) FOR(q,y1,y2+1) {
				if (!s[q][p]) {
					x[r]=q;
					y[r++]=p;
					r%=Q;
					s[q][p]=true;
				}
			}
		}
		int ans=0;
		while (1) {
			++ans;
			int j;
/*			REP(i,20) {
				REP(j,20)
				cout<<s[i][j];
				cout<<endl;
			}
			cout<<endl;*/
			memcpy(s2,s,sizeof(s));
			int t,r2=r;
			bool tt=false;
			int p,q;
			REP(p,101) REP(q,101) if (s2[p][q]) {
				if (!s2[p+1][q] && s2[p+1][q-1]) {
					s[p+1][q]=true;
					tt=true;
				}
				if (!s2[p][q+1] && s2[p-1][q+1]) {
					s[p][q+1]=true;
					tt=true;
				}
				if (s2[p-1][q] || s2[p][q-1]) {
					tt=true;
				} else {
					s[p][q]=false;
				}
			}
			if (!tt) break;
			//memcpy
		}
		printf("%d\n",ans);
	}
}
