#include <cstdio>
#include <algorithm>

using namespace std;

int permu[1000];
int big[200][200], small[200][200];

int used[1001];
int N, M;
int check( int n) {
	used[n] = 1;
	for( int i=1; i<=M; i++){
		if( small[n][i] == 1 && big[permu[n]][permu[i]] == 1 && used[i] == 0){
			if( check( i ) == 0)
				return 0;
		}
		if( small[n][i] == 1 && big[permu[n]][permu[i]] == 0)
			return 0;
	}
	return 1;
}
int main()
{
	int ccN;
	scanf("%d", &ccN);
	for( int cc=0; cc < ccN; cc++ ){
		memset(big,0,sizeof(big));
		memset(small,0,sizeof(small));
		scanf("%d", &N);
		int a, b;
		for(int i=1; i<=N; i++)
			permu[i] = i;
		for(int i=0; i<N-1; i++){
			scanf("%d %d", &a, &b);
			big[a][b] = 1;
			big[b][a] = 1;
		}
		scanf("%d", &M);
		for(int i=0; i<M-1; i++){
			scanf("%d %d", &a, &b);
			small[a][b] = 1;
			small[b][a] = 1;
		}
		printf("Case #%d: ", cc+1);
		do{
			memset(used,0,sizeof(used));
			if(check( 1 ) == 1){
				printf("YES\n");
				goto START;
				break;
			}
		}while( next_permutation(  permu+1, permu + N +1));
		printf("NO\n");
START:		a = 0;
	}	
	return 0;
}
