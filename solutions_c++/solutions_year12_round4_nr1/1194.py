#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
using namespace std;
typedef long long ll;
typedef unsigned long long hash;
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define N 20000

int n, D;

struct No{
	int d, l;
	int id;
	
	bool operator<(const No& a) const{
		return d < a.d;
	}
}nos[N];

int bs(int st, int tam){
	int ini = st, meio, fim = n - 1, best = -1;
	
	while(ini <= fim){
		int meio = (ini+fim) / 2;
		if(nos[meio].d - nos[st].d > tam){
			fim = meio - 1;
		}else{
			best = meio;
			ini = meio + 1;
		}
	}
	
	return best;
}

int best[N];


set<No> heap;

int main(){
	int casos;
	scanf( "%d", &casos );
	
	for(int t = 1; t <= casos; ++t){
		scanf("%d", &n );
		for(int i = 0; i < n; ++i){
			scanf("%d%d",&nos[i].d, &nos[i].l);
			nos[i].id = i;
		}
		
		scanf("%d", &D);
		
		memset(best, -1, sizeof best);
		best[0] = nos[0].d;
		bool chegou = false;
		for(int i = 0; i < n && !chegou; ++i){
			heap.insert(nos[i]);
			while(!heap.empty()){
				int id = (*heap.begin()).id;
				if(best[id] == -1 || best[id] < nos[i].d - nos[id].d){
					heap.erase(heap.begin());
				}else break;
			}
			
			if(heap.empty()==false){
				int j = (*heap.begin()).id;
				best[i] = max(best[i], min(nos[i].d - nos[j].d, nos[i].l));
						
				if(best[i] + nos[i].d >= D) chegou = true;
			}
		}
		
		printf("Case #%d: ", t);
		if(chegou){
			printf( "YES\n");
		}else printf("NO\n");
	}
}

