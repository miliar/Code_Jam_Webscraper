//Arek Wrobel - skater
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
#define REP(I, N) for(int I=0; I<(N); ++I)
#define FOR(I, M, N) for(int I=(M); I<=(N); ++I)
#define FORD(I, M, N) for(int I=(M); I>=(N); --I)
#define FOREACH(IT, CON) for(__typeof(CON.begin()) IT=CON.begin(); IT!=CON.end(); ++IT)
#define ST first
#define ND second
#define MP make_pair
#define PB push_back
const int INF=1000000000;

int x, s, r, t, n;
PII tab[1009];
int left;
double time;
double wy;

int main()
{
	double a;
	int v;
	int b, e;
	int T;
	scanf("%d", &T);
	FOR(lpt, 1, T){
		//wej
		scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
		left=x;
		REP(i, n){
			scanf("%d%d%d", &b, &e, &tab[i].ST);
			tab[i].ND=e-b;
			left-=tab[i].ND;
		}
		if (left){
			tab[n].ST=0;
			tab[n].ND=left;
			++n;
		}
		//prog
		sort(tab, tab+n);
		wy=0.0;
		time=t;
		//REP(i, n) printf("%d: %d %d\n", i, tab[i].ST, tab[i].ND);
		for(v=0; v<n; ++v){
			if (time*(r+tab[v].ST)<=tab[v].ND){
				wy+=time;
				wy+=(tab[v].ND-(time*(r+tab[v].ST)))/(s+tab[v].ST);
				++v;
				break;
			} else {
				a=tab[v].ND/(double)(r+tab[v].ST);
				wy+=a;
				time-=a;
			}
			//printf("%d: %lf %lf\n", v, time, wy);
		}
		for(; v<n; ++v)
			wy+=tab[v].ND/(double)(s+tab[v].ST);
		//wyj
		printf("Case #%d: %.7lf\n", lpt, wy);
	}
	return 0;
}

