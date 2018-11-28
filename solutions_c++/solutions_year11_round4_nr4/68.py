#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

int P,W, grau[40], adj[40][400],best,best2;

void go(int pos, long long mask,  int t1){
	//printf("pos %d %d\n", pos,t1);
	if(t1 > best)return;
	
	if(pos == 1){
		int t2 = 0;
		//printf("cheguei mas = %lld\n", mask);
		for(int i = 0; i < P; i++){
			if(mask&(1LL << i)){
			
			}else{
				bool bota = false;
				for(int j = 0; j < grau[i]; j++){
					int w = adj[i][j];
					if(w == 1)continue;
					if(mask&(1LL << w)){
						bota = true;
					}
				}
				if(bota)t2++;
			}
		}
		if(best > t1 || (best == t1 && best2 < t2)){
			best = t1;
			best2 = t2;
		}
	}else{
		for(int i = 0; i < grau[pos]; i++){
			int w = adj[pos][i];
			if(mask&(1LL << w)){
				
			}else{
				go(w,mask | (1LL << w), t1+1);
			}
		}
	}
}

int main(){
	int caso = 1;
	int casos;
	scanf("%d", &casos);
	
	for(int i = 1; i <= casos; i++){
		scanf("%d%d", &P, &W);
		
		for(int i = 0; i < P; i++)
			grau[i] = 0;
		
		for(int j = 0; j < W; j++){
			int a,b;
			scanf("%d,%d", &a, &b);
			adj[a][grau[a]++] = b;
			adj[b][grau[b]++] = a;
		}
		best = P;
		best2 = 0;
		
		go(0,1,1);
		printf("Case #%d: %d %d\n", caso++, best-2, best2+1);
	}
	
	return 0;
}