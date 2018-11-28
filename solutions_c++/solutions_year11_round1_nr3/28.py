#include <cstdio>
#include <queue>
#include <set>
#include <cstring>
#include <algorithm>

using namespace std;

struct Carta{
	int c,s,t, indice;
	
	bool operator < (const Carta &ot) const {
		if(t < ot.t)return true;
		else if(t > ot.t)return false;
		if(c < ot.c)return true;
		else if(c > ot.c)return false;
		return s < ot.s;
	}
	
}cartas[100];

priority_queue< Carta > heap;
set<int> indices;

int get(int turnos){
	vector<int> vetor;
	int res = 0;
	for(set<int>::iterator it = indices.begin(); it != indices.end(); it++){
		vetor.push_back(cartas[*it].s);
	}
	sort(vetor.begin(), vetor.end());
	for(int i = vetor.size()-1; i >= 0 && turnos > 0; i--,turnos--){
		res += vetor[i];
	}
	return res;
}

void process(){
	int N,M;
	
	indices.clear();
	while(!heap.empty())heap.pop();
	
	scanf("%d", &N);
	for(int i = 0; i < N; i++){
		scanf("%d%d%d", &cartas[i].c, &cartas[i].s, &cartas[i].t);
		cartas[i].indice = i;
	}
	scanf("%d", &M);
	for(int i = 0; i < M; i++){
		scanf("%d%d%d", &cartas[N+i].c, &cartas[N+i].s, &cartas[N+i].t);
		cartas[N+i].indice = N+i;
	}
	for(int i = 0; i < N; i++){
		heap.push(cartas[i]);
		indices.insert(i);
	}	
	int turnos = 1;
	int score = 0;
	int deck = N;
	int best = 0;
	
	
	while(turnos > 0 && !heap.empty()){
		best = max(best, score + get(turnos));
		
		Carta atual = heap.top();
		//printf("atual = %d %d %d\n", atual.c, atual.s, atual.t);
		heap.pop();		
		indices.erase(atual.indice);
		
		if(atual.c >= 1 && deck < N+M){
			heap.push(cartas[deck]);
			indices.insert(deck);
			deck++;
		}
		
		score += atual.s;
		turnos += atual.t;
		
		turnos--;
	}
	printf(" %d", best);
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