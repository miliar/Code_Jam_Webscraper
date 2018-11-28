#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <utility>
#include <map>
#include <queue>
#include <set>
#include <vector>


using namespace std;


int main(int argc, char* argv[]){
	int T, N, K;
	int table[31];
	table[0] = 1;
	for (int i = 1; i<31; i++)
		table[i] = table[i-1] * 2;
	scanf("%d", &T);
	for (int i = 0; i<T; i++){
		scanf("%d%d", &N, &K);
		printf("Case #%d: ", i+1);
		if ((K+1) % table[N] == 0)
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}

