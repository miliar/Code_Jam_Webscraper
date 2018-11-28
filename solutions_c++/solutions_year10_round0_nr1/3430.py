#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <algorithm>
#include <iostream>

using namespace std;

int N,K;
void read() {
	scanf("%d%d", &N, &K);
}

int pot2(int x) {
	int k = 1;
	while (x--) k*=2;
	return k;
}

void process() {
	int tamCiclo = pot2(N);
	
	K %= tamCiclo;
	
	printf("%s\n", K != tamCiclo-1 ? "OFF" : "ON" );
}

int main() {
	
	int T;
	scanf("%d", &T);
	for (int i = 1 ; i <= T ; i++) {
		read();
		printf("Case #%d: ", i);
		process();
	}
	
	return 0;
}
