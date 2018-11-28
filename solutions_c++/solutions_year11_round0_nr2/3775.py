#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

const int ROZ = int('A');

struct duo {
	
	char a, b;
};

duo comb[28];
set<char> opp[28];
char tab[200];
char wyn[200];

int main() {
	
	int t, c, d, n;
	bool znal;
	
	scanf("%d", &t);
	
	for (int i = 1; i <= t; i++) {
		
		for (int j = 0; j < 28; j++) {
			
			opp[j].clear();
			comb[j].a = '\0';
		}
		
		scanf("%d", &c);
		
		for (int j = 0; j < c; j++) {
			
			scanf("%s", &tab);
			
			comb[tab[0]-ROZ].a = tab[1];
			comb[tab[0]-ROZ].b = tab[2];
			
			comb[tab[1]-ROZ].a = tab[0];
			comb[tab[1]-ROZ].b = tab[2];
		}
		
		scanf("%d", &d);
		
		for (int j = 0; j < d; j++) {
			
			scanf("%s", &tab);
			opp[tab[0]-ROZ].insert(tab[1]);
			opp[tab[1]-ROZ].insert(tab[0]);
		}
		
		scanf("%d %s", &n, &tab);
		
		int kon = 0;
		
		for (int j = 0; j < n; j++) {
			
			if (!kon) {
				
				wyn[kon++] = tab[j];
				
			} else if (comb[int(wyn[kon-1])-ROZ].a == tab[j]) {
				
				wyn[kon-1] = comb[wyn[kon-1]-ROZ].b;
				
				
			} else {
				
				znal = false;
				
				for (int k = 0; k < kon; k++)
					if (opp[int(wyn[k])-ROZ].find(tab[j]) != opp[int(wyn[k])-ROZ].end()) {
						
						kon = 0;
						znal = true;
						break;
					}
				
				if (!znal)
					wyn[kon++] = tab[j];
			}
		}
		
		printf("Case #%d: [", i);
		
		for (int j = 0; j < kon; j++) {
			
			printf("%c", wyn[j]);
			
			if (j != kon - 1)
				printf(", ");
		}
		
		printf("]\n");
	}
	
	return 0;
	
}
