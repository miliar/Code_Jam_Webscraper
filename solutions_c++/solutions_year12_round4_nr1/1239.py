#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <queue>
#include <algorithm>

#define MAXN 20010

using namespace std;

struct No {
	int vine, alt;
	No(int a = 0, int b = 0) { vine = a, alt = b; }
	bool operator< (const No &node) const { return alt < node.alt; }
};

int n, D;
int pos[MAXN];
int tam[MAXN];

bool mark[MAXN];

priority_queue<No> fila;

int main() {
	int t;
	int caso = 0;
	scanf("%d", &t);
	while(t--) {
		scanf("%d", &n);
		for(int i = 0; i < n; ++i)
			scanf("%d%d", &pos[i], &tam[i]);
		scanf("%d", &D);
		
		while(!fila.empty()) fila.pop();
		memset(mark, false, sizeof(mark));
		
		fila.push( No(0, pos[0]) );
		bool solved = false;
		while(!fila.empty()) {
			No atual = fila.top();
			fila.pop();
			
			if(mark[atual.vine]) continue;
			mark[atual.vine] = true;
			
//			printf("< %d %d\n", atual.vine, atual.alt);
			if(D - pos[atual.vine] <= atual.alt) { solved = true; break; }
			
			for(int i = atual.vine + 1; i < n; ++i) {
				if(mark[i]) continue;
				if(pos[i] - pos[atual.vine] <= atual.alt) {
					fila.push( No(i, min(tam[i], pos[i] - pos[atual.vine])) );
				} else break;
			}
			
		}
		
		if(!solved) printf("Case #%d: NO\n", ++caso);
		else printf("Case #%d: YES\n", ++caso);
	}
	
	return 0;
}


