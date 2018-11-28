#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <queue>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;


struct Sit {
	map<string, int> mapa;
};
Sit sits[100000];
int next;
int total;

int N,M;
char input[40000];
char temp[40000];

int novo() {
	sits[next].mapa.clear();
	next++;
	return next-1;
}


void inserir(int no, int i) {
	if (input[i]) {
		int j = 0;
		i++;
		while (input[i] != '/' && input[i] != 0) {
			temp[j++] = input[i++];
		}
		temp[j] = 0;
		string s(temp);
		if (sits[no].mapa.find(s) != sits[no].mapa.end()) {
			inserir(sits[no].mapa[s], i); 
		} else {
			//printf("novo %s\n", temp);
			total++;
			inserir(sits[no].mapa[s] = novo(), i); 
		}
	}
}

int process() {
	scanf("%d%d", &N, &M);
	next = 1;
	total = 0;
	sits[0].mapa.clear();
	for (int i = 0 ; i < N ; i++) {
		//printf("N i %d\n", i);
		scanf("%s", input);
		inserir(0,0);
	}
	total = 0;
	for (int i = 0 ; i < M ; i++) {
		//printf("M i %d\n", i);
		scanf("%s", input);
		inserir(0,0);
	}
	return total;
}

int main() {
	
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int T;
	scanf("%d", &T);
	for (int i = 0 ; i < T ; i++) {
		printf("Case #%d: %d\n", i+1, process());
	}
	
	return 0;
}
