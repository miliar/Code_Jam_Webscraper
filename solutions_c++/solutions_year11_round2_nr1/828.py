#include <stdio.h>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i=0,_n=n; i<_n; i++)
#define FOR(i,a,b) for (int i=a,_n=b; i<=_n; i++)

char P[111][111];
int nTC,N;

double WP(int team, int exclude){
	double nP=0, nW=0;
	REP(i,N) if (team!=i && i!=exclude){
		if (P[team][i]=='.') continue;
		if (P[team][i]=='1') nW += 1.0;
		nP += 1.0;
	}
	if (nP > 0) return nW / nP;
	return -1;
}

double OWP(int team){
	double n=0, sum=0;
	REP(i,N) if (team!=i){
		if (P[team][i]=='.') continue;
		double wp = WP(i, team);
		if (wp < -0.5) continue;
		sum += wp;
		n += 1.0;
	}
	if (n > 0) return sum / n;
	return -1;
}

double OOWP(int team){
	double n=0, sum=0;
//	printf("oowping %d\n",team);
	REP(i,N) if (team!=i){
		if (P[team][i]=='.') continue;
		double owp = OWP(i);
		if (owp < -0.5) continue;
//		printf("owp %d = %lf\n",i,owp);
		sum += owp;
		n += 1.0;
	}
	if (n > 0) return sum / n;
	return 0;
}

double RPI(int team){
//	printf("%d %lf %lf %lf\n",team,WP(team,-1), OWP(team), OOWP(team));
	return 0.25 * max(0.0, WP(team,-1)) + 0.50 * max(0.0, OWP(team)) + 0.25 * OOWP(team);
}

int main(){
	scanf("%d",&nTC);
	FOR(TC,1,nTC){
		scanf("%d",&N);
		REP(i,N) scanf("%s",P[i]);
//		REP(i,N) puts(P[i]);
		printf("Case #%d:\n",TC);
		REP(i,N) printf("%.9lf\n",RPI(i));
		fflush(stdout);
	}
}
