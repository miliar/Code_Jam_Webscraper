#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdio>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string.h>
#include <cassert>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define INF (int)1e9
#define EPS LD(1e-9)
#define DINF LD(1e50)

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<vector<int> > VVI;
typedef pair<int,int> PII;
typedef double LD;

const int mn=103;
int n;
LD wp[mn], owp[mn], oowp[mn];
char grid[mn][mn];

int main(){
	
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int Kase=GI;
	FOR(kase,1,Kase+1){
		n=GI;
		REP(i,n)	scanf("%s",grid[i]);
		printf("Case #%d:\n",kase);
		REP(i,n){
			int wins=0, tot=0;
			REP(j,n){
				if(grid[i][j]=='.')	continue;
				tot++;
				wins+=(grid[i][j]=='1');	
			}	
			wp[i]=LD(wins)/tot;
		}
		REP(i,n){
			owp[i]=0;
			int den=0;
			REP(j,n)	if(i!=j && grid[i][j]!='.'){
				den++;
				int wins=0, tot=0;
				REP(k,n)	if(k!=i){
					if(grid[j][k]=='.')	continue;
					tot++;
					wins+=(grid[j][k]=='1');
				}
				owp[i]+=LD(wins)/tot;
			}	
			owp[i]/=den;
		}
		REP(i,n){
			oowp[i]=0;
			int den=0;
			REP(j,n)	if(i!=j && grid[i][j]!='.')	den++, oowp[i]+=owp[j];
			oowp[i]/=den;	
		}
/*		REP(i,n)	cerr<<wp[i]<<" ";cerr<<endl;
		REP(i,n)	cerr<<owp[i]<<" ";cerr<<endl;
		REP(i,n)	cerr<<oowp[i]<<" ";cerr<<endl;
*/
		REP(i,n)	printf("%.12lf\n",0.25*(wp[i]+oowp[i])+0.5*owp[i]);
		cerr<<"Completed "<<kase<<endl;
	}
	
	cerr<<"Completed all"<<endl;
	while(1);
	return 0;
}
