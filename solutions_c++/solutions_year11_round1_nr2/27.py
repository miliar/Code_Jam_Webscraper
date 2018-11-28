#include <cstdio>
#include <utility>
#include <cstring>
#include <algorithm>

using namespace std;

char str[10010][20];
char ordem[50];
pair<int,int> values[10100];
int res[10100], maior;

void rec(int ini, int fim, int pos, int peso){
	
	//printf("%d %d %d %d %s\n", ini, fim, pos,peso, str[values[ini].second]);
	
	if(ini == fim) {
		res[values[ini].second] = peso;
		if(peso > maior)
			maior = peso;
		return;
	}
	
	bool tem = false;
	for(int i = ini; i <= fim; i++){
		for(int j  = 0; str[values[i].second][j] != 0; j++){
			if(str[values[i].second][j] == ordem[pos])
				tem = true;
		}
	}
	for(int i = ini; i <= fim; i++){
		int val = 0;
		for(int j  = 0; str[values[i].second][j] != 0; j++){
			val *= 2;
			val += (str[values[i].second][j] == ordem[pos]);
		}
		values[i].first = val;
	}
	sort(values + ini, values + fim + 1);
	
	int ant = ini;
	int ac;
	for(int j = ini; j <= fim; j++){
		
		if(j > ini && values[j].first != values[j-1].first){
			if(tem && values[ant].first == 0)ac = 1;
			else ac = 0;
			
			rec(ant, j-1, pos+1, peso + ac);
			ant = j;
		}
	}
	if(tem && values[ant].first == 0)ac = 1;
	else ac = 0;
	rec(ant, fim, pos+1, peso+ac);
}

void process(){
	int N, M;
	
	scanf("%d%d", &N, &M);
	
	for(int i = 0; i < N; i++){
		scanf("%s", str[i]);
	}
	
	for(int i = 0; i < M; i++){
		for(int j= 0; j < N; j++){
			values[j].second = j;
			values[j].first = strlen(str[j]);
		}
		sort(values, values + N);
		scanf("%s", ordem);
		int ant = 0;
		maior = 0;
		for(int j = 0; j < N; j++){
			if(j > 0 && values[j].first != values[j-1].first){
				rec(ant, j-1, 0, 0);
				ant = j;
			}
		}
		rec(ant, N-1, 0, 0);
		for(int j = 0; j < N; j++){
			if(res[j] == maior){
				printf(" %s", str[j]);
				break;
			}
		}
	}
}

int main(){
	
	int casos;
	
	scanf("%d", &casos);
	
	for(int i = 1; i <= casos; i++){
		printf("Case #%d:", i);
		process();
		printf("\n");
	}
	
	return 0;
}