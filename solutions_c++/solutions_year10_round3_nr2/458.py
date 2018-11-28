#include <cstdio>
#include <algorithm>

using namespace std;

int tab[1001][1001];
int L, P, C;

int rek(int a, int o){
	if(tab[a][o] != -1)
		return tab[a][o];
	if(a*C >= o)
		return 0;
	tab[a][o] = 99999;
	for(int i=a; i<=o; ++i){
		tab[a][o] = min(tab[a][o], 1+max(rek(a, i), rek(i, o)));
	}
	return tab[a][o];
}

int main(){
	int tc, t;
	scanf("%d", &tc);
	for(t=0;t<tc;++t){
		memset(tab, -1, sizeof(tab));
		scanf("%d %d %d", &L, &P, &C);
		printf("Case #%d: %d\n", t+1, rek(L, P));
		fflush();
	}
}
