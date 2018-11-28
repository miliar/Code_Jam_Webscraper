//Arek Wrobel - skater
#include <cstdio>
#include <algorithm>
#include <cmath>
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
const LL INFLL=1000000000000000000LL;

int a, b;
int dl;
int pot10;
int t[1500000];
int ilet;

LL wy;

inline int cykluj(int x){
	return pot10*(x%10)+x/10;
}
int reprezentant(int x){
	int wyn=x;
	REP(i, dl-1){
		x=cykluj(x);
		wyn=min(wyn, x);
	}
	return wyn;
}

int main()
{
	int T;
	scanf("%d", &T);
	FOR(lpt, 1, T){
		//wej
		scanf("%d%d", &a, &b);
		//prog
		wy=ilet=dl=0;
		for(int i=a; i; i/=10) ++dl;
		pot10=1;
		FOR(i, 2, dl)
			pot10*=10;
		FOR(i, a, b)
			t[ilet++]=reprezentant(i);
		sort(t, t+ilet);
		int ile=1;
		REP(i, ilet)
			if (t[i]==t[i+1])
				++ile;
			else {
				wy+=ile*LL(ile-1)/2;
				ile=1;
			}
		//wyj
		printf("Case #%d: %lld\n", lpt, wy);
	}
	return 0;
}

