#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>

# define INF 0x3f3f3f3f

# define MAXN 

using namespace std;

int T;
int tc = 1;
int N, M;

char linha[128];
vector <int> dir[1024];
vector <int> proc[1024];
map<string, int> mapa;

int main (void){
	scanf("%d", &T);
	while(T--){
		printf("Case #%d: ", tc++);
		scanf("%d%d", &N, &M);
		mapa.clear();
		int cnt = 0;
		for(int i = 0;i<N;i++){
			dir[i].clear();
			scanf(" %s", linha);
			// puts(linha);
			char *str = strtok(linha, "/");
			while(str != NULL){
				if(mapa.find(str) == mapa.end()) mapa[str] = cnt++;
				dir[i].push_back(mapa[str]);
				str = strtok(NULL, "/");
			}
		}
		for(int i = 0;i<M;i++){
			proc[i].clear();
			scanf(" %s", linha);
			char *str = strtok(linha, "/");
			while(str != NULL){
				if(mapa.find(str) == mapa.end()) mapa[str] = cnt++;
				// printf("%d ", mapa[str]);
				proc[i].push_back(mapa[str]);
				str = strtok(NULL, "/");
			}
		}
		int soma = 0;
		for(int i = 0;i<M;i++){
			int menor;
			int t1 = proc[i].size();
			menor = t1;
			for(int j = 0;j<N;j++){
				int t2 = dir[j].size();
				int k = 0;
				while(k< t1 && k < t2){
					if(proc[i][k] != dir[j][k]) break;
					k++;
				}
				menor = min(menor, t1-k);
			}
			dir[N] = proc[i];
			N++;
			soma += menor;
		}
		printf("%d\n", soma);
	}
	return 0;
}