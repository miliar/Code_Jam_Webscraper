#include <iostream>

using namespace std;

int rank[100];
int mask;
int n;

int cache[100];

void processMask(){
	int cnt = 0;
	for (int i = 0; i < n; i++)
		rank[i] = -1;
	for (int i = 2; i < n; i++){
		if (mask & (1 << i)){
			rank[i] = ++cnt;									
		}
	}
	/*for (int i = 0; i < n; i++)
		printf("%d ",rank[i]);
	printf("\n");
	printf("%d\n",cnt);*/
	rank[n] = ++cnt;	
}

bool prove(int n){
	while (rank[n] != -1){
		//printf("%d %d\n",n,rank[n]);
		n = rank[n];
	}
	return n == 1;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t; scanf("%d",&t);
	for (int tt = 0; tt < t; tt++){
		fprintf(stderr,"%d\n",tt);
		scanf("%d",&n);
		if (cache[n]){
			printf("Case #%d: %d\n",tt+1,cache[n]);
			continue;
		}
		int ans = 0;
		for (mask = 0; mask < (1 << n); mask++){
			//printf("%d\n",mask);
			processMask();
			if (prove(n)) ans++;
		}
		cache[n] = (ans / 4) % 100003;
		printf("Case #%d: %d\n",tt+1,cache[n]);
	}

	return 0;
}