#include <iostream>
#include <cmath>
#include <vector>
#include <cstring>
#include <queue>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <map>
using namespace std;
typedef unsigned long long int uint64;
#define MAXN 1010

int N;
struct G{
	int p, l, id;
};
G g[MAXN];

int CMP(const void *a, const void *b){
	G x = *(G*)a;
	G y = *(G*)b;
	if( x.p < y.p ) return 1;
	else if( x.p == y.p ){
		if( x.id > y.id ) return 1;
		return -1;
	}
	return -1;

}

int main() {
	//freopen("input", "r", stdin);

	//
	int caseid = 1;
	int cases;
	scanf("%d", &cases);
	while (cases--) {

		// read
		scanf("%d", &N);
		for (int i = 0; i < N; i++){
			scanf("%d", &g[i].l);
		}
		for (int i = 0; i < N; i++){
			scanf("%d", &g[i].p);
			g[i].id = i;
		}

		qsort(g, N, sizeof(G), CMP);

		printf("Case #%d:", caseid++);
		for (int i = 0; i < N; i++){

			printf(" %d", g[i].id);
		}
		printf("\n");
	}

	return 0;
}
