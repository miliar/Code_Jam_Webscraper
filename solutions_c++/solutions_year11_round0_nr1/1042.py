#include <cstdio>
#include <cstdlib>

using namespace std;

int main() {
	int T, N;
	int p;
	int tot;
	scanf("%d", &T);
	char code[10];
	int rid;
	int pos[2];
	int stepb[2];
	
	
	for(int ti=0; ti<T; ti++) {
		scanf("%d", &N);
		tot = 0;
		pos[0] = 1;
		pos[1] = 1;
		stepb[0] = 0;
		stepb[1] = 0;
		
		for(int i=0; i<N; i++) {
			scanf("%s", code);
			scanf("%d", &p);
			
			int rid = (code[0]=='B') ? 0 : 1;
			int orid = 1 - rid;
						
			int mv = abs(pos[rid] - p) - stepb[orid];
			if (mv<0)
				mv=0;
			stepb[orid] = 0;
			pos[rid] = p;
			
			mv++;
			
			//printf("Sek=%d rid=%d mv=%d\n", i, rid, mv);
			
			tot += mv;
			
			stepb[rid] += mv;			
		}
		
		
		printf("Case #%d: %d\n", ti+1, tot);
	}
	
	return 0;
}

