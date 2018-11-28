#include <cstdio>
#define REP(i,n) for (int i=1;i<=n;++i)
using namespace std;

int T,a[5][5],s[4];

int Get() {
	char c=getchar();
	if (c=='X') return 1;
	if (c=='O') return 2;
	if (c=='T') return 3;
	if (c=='.') return 0;
}

bool Check() {
	if (s[1]+s[3]==4) {puts("X won");return true;}
	if (s[2]+s[3]==4) {puts("O won");return true;}
	return false;
}

void Work() {
	REP(i,4) {
		s[1]=s[2]=s[3]=0;
		REP(j,4) ++s[a[i][j]];
		if (Check()) return;
		s[1]=s[2]=s[3]=0;
		REP(j,4) ++s[a[j][i]];
		if (Check()) return;
	}
	s[1]=s[2]=s[3]=0;
	REP(i,4) ++s[a[i][i]];
	if (Check()) return;
	s[1]=s[2]=s[3]=0;
	REP(i,4) ++s[a[i][5-i]];
	if (Check()) return;
	int tmp=0;
	REP(i,4) REP(j,4) if (a[i][j]) ++tmp;
	if (tmp==16) {puts("Draw");return;}
	puts("Game has not completed");
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	REP(T_T,T) {
		printf("Case #%d: ",T_T);
		getchar();
		REP(i,4) {
			REP(j,4) a[i][j]=Get();
			getchar();
		}
		Work();
	}
	return 0;
}
