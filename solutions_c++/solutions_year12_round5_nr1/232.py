#include <stdio.h>
#include <map>
#include <algorithm>
#include <string>
using namespace std;

int N;
pair<int, int> g[1024];
//int P[1024];

void run(int fall){
	printf("Case #%d:", fall);
	scanf("%d", &N);
	int x;
	for(int i=0;i<N;i++){
		scanf("%d", &x);
	}
	for(int i=0;i<N;i++){
		scanf("%d", &x);
		g[i] = make_pair(-x, i);
	}
	sort(g, g+N);
	for(int i=0;i<N;i++){
		printf(" %d", g[i].second);
	}
	printf("\n");
}


int main(){
	int T;
	scanf("%d", &T);
	for(int i=0;i<T;i++){
		run(i+1);
	}	
}