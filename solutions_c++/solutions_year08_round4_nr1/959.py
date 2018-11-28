#include <cstdio>
#include <algorithm>
using namespace std;

#define MAX_NODES	(12000)
#define CHOLERNIE_DUZO	(1<<29)

static int nodes;
static struct {
	char gate, changable;
	int cost[2];
} val[MAX_NODES*2 + 1];

int main() {
	int _N; scanf("%d",&_N);
	for(int _Ni=1;_Ni<=_N;_Ni++) {
		int V;
		scanf("%d%d",&nodes,&V);
		for(int i=1;i<=((nodes-1)/2);i++) {
			int G,C;
			scanf("%d%d",&G,&C);
			val[i].gate = G?'&':'|';
			val[i].changable = C;
			val[i].cost[0] = CHOLERNIE_DUZO;
			val[i].cost[1] = CHOLERNIE_DUZO;
		}
		for(int i=((nodes-1)/2)+1;i<=nodes;i++) {
			int V;
			scanf("%d",&V);
			val[i].gate = '#';
			val[i].changable = 0;
			val[i].cost[0] = CHOLERNIE_DUZO;
			val[i].cost[1] = CHOLERNIE_DUZO;
			val[i].cost[V] = 0;
		}
		for(int i=((nodes-1)/2);i>=1;i--) {
			int vcost[2][2];
			for(int x=0;x<2;x++) 
			for(int y=0;y<2;y++) 
				vcost[x][y] = val[2*i].cost[x]+val[2*i+1].cost[y];
			if(val[i].gate=='&' || val[i].changable) {
				int C = (val[i].gate!='&')?1:0;
				val[i].cost[0] = std::min(val[i].cost[0], vcost[0][0]+C);
				val[i].cost[0] = std::min(val[i].cost[0], vcost[0][1]+C);
				val[i].cost[0] = std::min(val[i].cost[0], vcost[1][0]+C);
				val[i].cost[1] = std::min(val[i].cost[1], vcost[1][1]+C);
			}
			if(val[i].gate=='|' || val[i].changable) {
				int C = (val[i].gate!='|')?1:0;
				val[i].cost[0] = std::min(val[i].cost[0], vcost[0][0]+C);
				val[i].cost[1] = std::min(val[i].cost[1], vcost[0][1]+C);
				val[i].cost[1] = std::min(val[i].cost[1], vcost[1][0]+C);
				val[i].cost[1] = std::min(val[i].cost[1], vcost[1][1]+C);
			}
		}
		int res = val[1].cost[V];
		if(res>=CHOLERNIE_DUZO) {
			printf("Case #%d: IMPOSSIBLE\n",_Ni);
		} else {
			printf("Case #%d: %d\n",_Ni,res);
		}
	}
	return 0;
}

