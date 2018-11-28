#include <stdio.h>

#define REP(i,n) for (int i=0,_n=n; i<_n; i++)
#define FOR(i,a,b) for (int i=a,_n=b; i<=_n; i++)

char m[100][100];
int nTC,R,C;

bool can(){
	REP(i,R) REP(j,C){
		if (m[i][j]=='#'){
			if (!(i+1<R && j+1<C)) return false;
			if (m[i][j+1]!='#') return false;
			if (m[i+1][j]!='#') return false;
			if (m[i+1][j+1]!='#') return false;
			m[i][j] = '/';
			m[i][j+1] = '\\';
			m[i+1][j] = '\\';
			m[i+1][j+1] = '/';
		}
	}
	return true;
}

int main(){
	scanf("%d",&nTC);
	FOR(TC,1,nTC){
		printf("Case #%d:\n",TC);
		scanf("%d %d",&R,&C);
		REP(i,R) scanf("%s",m[i]);

		if (can()){
			REP(i,R) puts(m[i]);
		} else {
			puts("Impossible");
		}
	}
}
