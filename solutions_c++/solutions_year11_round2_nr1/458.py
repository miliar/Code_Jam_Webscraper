//Arek Wrobel - skater
#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long LL;
#define REP(I, N) for(int I=0; I<(N); ++I)
#define FOR(I, M, N) for(int I=(M); I<=(N); ++I)
#define FORD(I, M, N) for(int I=(M); I>=(N); --I)

int n;
char t[100][100];

int wp;
int x;

double OWP;
int X;

double owp[100];

double WP;

int main()
{
	int T;
	scanf("%d", &T);
	FOR(lpt, 1, T){
		//wej
		scanf("%d", &n);
		REP(i, n)
			REP(j, n)
				scanf(" %c", &t[i][j]);
		//prog/wyj
		printf("Case #%d:\n", lpt);
		REP(v, n){
			OWP=X=0;
			REP(i, n) if (t[v][i]!='.'){
				wp=x=0;
				REP(j, n) if (j!=v && t[i][j]!='.'){
					if (t[i][j]=='1') ++wp;
					++x;
				}
				OWP+=wp/double(x);
				++X;
			}
			owp[v]=OWP/X;
		}
		REP(v, n){
			wp=x=0;
			REP(i, n) if (t[v][i]!='.'){
				if (t[v][i]=='1') ++wp;
				++x;
			}
			WP=wp/double(x);
			OWP=x=0;
			REP(i, n) if (t[v][i]!='.'){
				OWP+=owp[i];
				++x;
			}
			OWP=OWP/x;
			printf("%.8lf\n", 0.25*WP + 0.5*owp[v] + 0.25*OWP);
		}
	}
	return 0;
}

