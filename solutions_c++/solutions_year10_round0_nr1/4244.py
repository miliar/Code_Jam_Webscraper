#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <algorithm>
#include <string>
#include <fstream>
using namespace std;

const int size = 31;
bool used[size];

int main(int argc, char *argv[])
{	
	int T, N, K, f, t;
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	scanf("%d", &T);	
	for(int j = 1; j <= T; j++){
		scanf("%d%d", &N, &K);
		memset(used, false, sizeof(used));
		for(int k = 0; k < K; k++){
			f = 0;
			while(used[f]){
				if(f == N)break;
				used[f] = !used[f];
				f++;				
			}
			used[f] = !used[f];
			/*
			for(int i = 0; i < N; i++)
				printf("%c", used[i] ? '1' : '0');
			printf("\n");
			*/
		}
		f = 0;
		while(used[f]){
			if(f == N - 1)break;
			f++;
		}
		//printf("%d\n", f);
		if(f == N - 1 && used[f])
			printf("Case #%d: ON\n", j);
		else
			printf("Case #%d: OFF\n", j);
	}
	return 0;
}
