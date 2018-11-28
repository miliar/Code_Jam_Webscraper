#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<cmath>
#include<string>
#include<cstring>
#include<cctype>
#include<algorithm>
#include<vector>
#include<bitset>
#include<queue>
#include<stack>
#include<utility>
#include<list>
#include<set>
#include<map>

using namespace std;

#define eps 1e-9
#define INF INT_MAX
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).end(),(v).begin()
#define mp make_pair
#define pb push_back

#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define REPSZ(i,v) REP(i,SZ(v))
#define CLEAR(t) memset((t),0,sizeof(t))

typedef pair < int, int > pii;
typedef long long LL;
#define MAX 105

string mat[MAX];
vector<pair<int,int> > WP;
vector<double>OWP,OOWP, RTI;
int N;
void calcWP(){
	REP(i,N){
		int total = 0;
		int win = 0;
		REP(j,N){
			if(mat[i][j]=='1'){
				total++;
				win ++;
			}else if(mat[i][j]=='0'){
				total++;
			}
		}
		WP.pb(mp(win,total));
	}
}
void calcOWP(){
	REP(i,N){
		double sum = 0;
		int tot = 0;
		REP(j,N){
			if(mat[j][i]=='1'){
				sum+=((WP[j].first-1)/((WP[j].second-1)*1.0));
				tot++;
			}else if(mat[j][i]=='0'){
				sum+=((WP[j].first)/((WP[j].second-1)*1.0));
				tot++;
			}
		}
		OWP.pb(sum/(tot*1.0));
	}
}
void calcOOWP(){
	REP(i,N){
		double sum = 0;
		int tot = 0;
		REP(j,N){
			if(mat[j][i]=='1' || mat[j][i]=='0'){
				tot++;
				sum+=OWP[j];
			}
		}
		OOWP.pb(sum/(tot*1.0));
	}
}
void calcRTI(){
// RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
	REP(i,N){
		double val = 0.25*(WP[i].first/(WP[i].second*1.0))+0.5*OWP[i]+0.25*OOWP[i];
		RTI.pb(val);
	}
}
void run1(int caso){

	cin >> N;

	REP(i,N){
		cin >> mat[i];
	}
	WP.clear();OWP.clear();OOWP.clear();RTI.clear();
	calcWP();
	calcOWP();
	calcOOWP();
	calcRTI();

	printf("Case #%d:\n",caso);
	REP(i,N){
		printf("%0.9lf\n",RTI[i]);
	}
}
int main()
{
	int T; scanf("%d",&T);
	FORE(i,1,T) run1(i);
	return 0;
}
