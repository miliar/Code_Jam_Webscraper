#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <map>
#include <algorithm>
#include <utility>
#include <cmath>

using namespace std;

int combine[300][300], cn, destroy[300][50], proxVaga[300], qnts[300];
char comb[20], res[300][300], in[1000];
int main(){
	
	int caso = 1; int casos; scanf("%d", &casos);
	int c, d, n;
	char out[1000];
	while(casos--){
		++cn;
		printf("Case #%d: ", caso++);
		scanf("%d", &c);
		memset(proxVaga, 0, sizeof(proxVaga));
		memset(qnts, 0, sizeof(qnts));
		for(int i = 0; i < c; ++i){
			scanf("%s", comb);
			combine[comb[0]][comb[1]] = cn; res[comb[0]][comb[1]] = comb[2];
			combine[comb[1]][comb[0]] = cn; res[comb[1]][comb[0]] = comb[2];
		}
		scanf("%d", &d);
		for(int i = 0; i < d; ++i){
			scanf("%s", comb);
			destroy[comb[0]][proxVaga[comb[0]]++] = comb[1];
			destroy[comb[1]][proxVaga[comb[1]]++] = comb[0];
		}
		
		scanf("%d", &n);
		scanf("%s", in);
		int t = 0;
		for(int i = 0; i < n; ++i){
		//	printf("%d: ", i); for(int j = 0; j < t; ++j) printf("%c ", out[j]); printf("\n");
			//if( t > 0)
				//printf("%d: %c %c\n", i, out[t-1], in[i]);
			if(t > 0 && combine[out[t-1]][in[i]] == cn){
				
				qnts[out[t-1]]--;
				out[t-1] = res[out[t-1]][in[i]];
				qnts[res[out[t-1]][in[i]]]++;
			}else{
				for(int j = 0; j < proxVaga[in[i]]; ++j){
					if(qnts[ destroy[in[i]][j] ] > 0){
						
						t = 0;
				//		printf("%d: DESTROY, qnts[%d] = %d\n", i, destroy[in[i]][j], qnts[destroy[in[i]][j]]);
						memset(qnts, 0, sizeof(qnts));
						goto cont;
					}
				}
				out[t++] = in[i];
				qnts[in[i]]++;
				cont:;
			}
		}
		if(t > 0){
			printf("[%c", out[0]);
			for(int i = 1; i < t; ++i) 
				printf(", %c", out[i]);
			printf("]\n");
		}else{
			printf("[]\n");
		}
		
	}
	
	
	
	return 0;
}