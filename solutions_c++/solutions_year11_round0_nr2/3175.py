//Arek Wrobel - skater
#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long LL;
#define REP(I, N) for(int I=0; I<(N); ++I)
#define FOR(I, M, N) for(int I=(M); I<=(N); ++I)
#define FORD(I, M, N) for(int I=(M); I>=(N); --I)

int c, d, n;
char tc[26][26];
bool td[26][26];
char s[120];

int wyn[120];
int wy;

int main()
{
	int T;
	char pom[4];
	scanf("%d", &T);
	FOR(lpt, 1, T){
		REP(i, 26) REP(j, 26)
			tc[i][j]=td[i][j]=0;
		//wej
		scanf("%d", &c);
		REP(i, c){
			scanf("%s", pom);
			for (int j=0; pom[j]; ++j)
				pom[j]-='A';
			tc[pom[0]][pom[1]]=tc[pom[1]][pom[0]]=pom[2];
		}
		scanf("%d", &d);
		REP(i, d){
			scanf("%s", pom);
			for (int j=0; pom[j]; ++j)
				pom[j]-='A';
			td[pom[0]][pom[1]]=td[pom[1]][pom[0]]=true;
		}
		scanf("%d", &n);
		scanf("%s", s);
		for (int j=0; s[j]; ++j)
			s[j]-='A';
		//prog
		wy=0;
		REP(v, n){
			wyn[wy++]=s[v];
			while(wy>1 && tc[wyn[wy-2]][wyn[wy-1]]){
				wyn[wy-2]=tc[wyn[wy-2]][wyn[wy-1]];
				--wy;
			}
			for (int i=0; i<wy-1; ++i)
				if (td[wyn[wy-1]][wyn[i]]){
					wy=0;
					break;
				}
		}
		//wyj
		printf("Case #%d: [", lpt);
		if (wy>0){
			printf("%c", wyn[0]+'A');
			for (int i=1; i<wy; ++i)
				printf(", %c", wyn[i]+'A');
		}
		printf("]\n");
	}
	return 0;
}

