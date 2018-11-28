#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <set>
#include <algorithm>

#define MAXN 110

using namespace std;

int pot[10];

int size(int x) {
	int resp = 0;
	while(x) ++resp, x /= 10;
	return resp;
}

set< pair<int, int> > conj;

int main() {
	pot[0] = 1;
	for(int i = 1; i < 10; ++i) pot[i] = 10 * pot[i - 1];
	
	int casos;
	scanf("%d", &casos);
	for(int caso = 1; caso <= casos; ++caso) {
		int aa, bb, ans = 0;
		scanf("%d%d", &aa, &bb);
		conj.clear();
		int len = size(aa);
		for(int j = aa; j <= bb; ++j) {
//			printf("%d:\n", j);
			for(int k = 0; k < len; ++k) {
				int ii = (j / pot[k]) + (j % pot[k]) * pot[len - k];
//				printf("\tpot %d: %d\n", k, ii);
				
				if(j < ii && ii <= bb) conj.insert( pair<int, int>(j, ii) );
			}
		}

		ans = conj.size();
//		printf("> %d\n", conj.size());
		printf("Case #%d: %d\n", caso, ans);
	}
	
	return 0;
}


